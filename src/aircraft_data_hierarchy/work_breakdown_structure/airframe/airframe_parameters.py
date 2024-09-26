from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum

# Assuming CommonBaseModel and Spline are defined elsewhere
from ...common_base_model import CommonBaseModel, Metadata
from aircraft_data_hierarchy.work_breakdown_structure.airframe.airframe_geometry import (
    Body, Spline
)

# ToDo: This entire set of classes needs to be refactored because:
# 1. many parameters belong in other MSoSA branches like Behavior
# 2. many parameters need to be separated and collected by component

# Group I - Reference Data

# ToDo: Move this class to Behavior?...or is it already redundant with something in DaveML

class ReferenceData(CommonBaseModel):
    roughness: Optional[float] = Field(None, alias="RougHgt", ge=0., le=0.02, description="Equivalent Sand Surface roughness height")
    reference_area: Optional[float] = Field(None, alias="Sref", gt=0., description="Reference area (ft^2)")
    reference_length: Optional[float] = Field(None, alias="Cbar", gt=0., description="Longitudinal reference length (ft)")
    lateral_reference: Optional[float] = Field(None, alias="BLref", gt=0., description="Lateral reference length (ft)")

    @field_validator('roughness')
    def roughness_valid(cls, v):
        if v is not None and not (0 <= v <= 0.02):
            raise ValueError('roughness must be between 0 and 0.02')
        return v

# Group II - Basic Configuration Definition

# ToDo: Move this class to Behavior?...is it already redundant with comething in DaveML

class FlightConditions(CommonBaseModel):
    """
    Represents flight conditions for aerodynamic calculations.

    Attributes:
        loop_control (Optional[int]): Loop Control: 1 - Altitude and Mach, 2 - Mach Only, 3 - Altitude Only.
        qty_machs (Optional[int]): Number of Mach numbers.
        machs (List[Optional[float]]): Ascending order of Freestream Mach numbers.
        velocities (List[Optional[float]]): Ascending order of Freestream Velocities.
        qty_alphas (Optional[int]): Number of angles-of-attack.
        alphas (List[Optional[float]]): Ascending order of angles-of-attack.
        reynolds_indicies (List[Optional[float]]): Reynolds number per unit length at Freestream conditions.
        qty_altitudes (Optional[int]): Number of altitudes.
        altitudes (List[Optional[float]]): Geometric Altitudes.
        static_pressures (List[Optional[float]]): Freestream static pressure.
        static_temperatures (List[Optional[float]]): Freestream static temperature.
        transonic_mach (Optional[float]): Transonic Onset Mach number.
        supersonic_mach (Optional[float]): Supersonic Onset Mach number.
        hypersonic_flag (Optional[bool]): Hypersonic flag: true - Hypersonic analysis at all Mach > 1.4.
        transition_flag (Optional[bool]): Transition flag: 0 - None, 1 - Transition Strips or Full Flight.
        weight (Optional[float]): Aircraft Weight.
        flight_path_angle (Optional[float]): Flight path Angle.
    """
    loop_control: Optional[int] = Field(1, gt=0, lt=4, description="Loop Control: 1 - Altitude and Mach, 2 - Mach Only, 3 - Altitude Only")
    qty_machs: Optional[int] = Field(None, ge=0, description="Number of Mach numbers")
    machs: List[Optional[float]] = Field(default_factory=list, description="Ascending order of Freestream Mach numbers")
    velocities: List[Optional[float]] = Field(default_factory=list, description="Ascending order of Freestream Velocities")
    qty_alphas: Optional[int] = Field(None, ge=0, description="Number of angles-of-attack")
    alphas: List[Optional[float]] = Field(default_factory=list, description="Ascending order of angles-of-attack")
    reynolds_indicies: List[Optional[float]] = Field(default_factory=list, description="Reynolds number per unit length at Freestream conditions")
    qty_altitudes: Optional[int] = Field(None, ge=0, description="Number of altitudes")
    altitudes: List[Optional[float]] = Field(default_factory=list, description="Geometric Altitudes")
    static_pressures: List[Optional[float]] = Field(default_factory=list, description="Freestream static pressure")
    static_temperatures: List[Optional[float]] = Field(default_factory=list, description="Freestream static temperature")
    transonic_mach: Optional[float] = Field(0.6, ge=0.6, lt=0.99, description="Transonic Onset Mach number")
    supersonic_mach: Optional[float] = Field(1.4, ge=1.01, lt=1.4, description="Supersonic Onset Mach number")
    hypersonic_flag: Optional[bool] = Field(False, description="Hypersonic flag: true - Hypersonic analysis at all Mach > 1.4")
    transition_flag: Optional[bool] = Field(False, description="Transition flag: 0 - None, 1 - Transition Strips or Full Flight")
    weight: Optional[float] = Field(None, ge=0, description="Aircraft Weight")
    flight_path_angle: Optional[float] = Field(None, gt=0, lt=2, description="Flight path Angle")

    @field_validator('machs', 'velocities', 'alphas', 'reynolds_indicies', 'altitudes', 'static_pressures', 'static_temperatures')
    @classmethod
    def list_must_be_non_negative(cls, v: List[Optional[float]]) -> List[Optional[float]]:
        """
        Validate that all list values are non-negative.

        Args:
            v (List[Optional[float]]): The list to validate.

        Returns:
            List[Optional[float]]: The validated list.

        Raises:
            ValueError: If any value in the list is negative.
        """
        if v is not None and any(item is not None and item < 0 for item in v):
            raise ValueError("All list values must be non-negative")
        return v

    @model_validator(mode='before')
    def validate_list_lengths(cls, values):
        """
        Validate that the length of lists matches their corresponding quantity fields.

        Args:
            values (dict): The current values of the model.

        Returns:
            dict: The validated values.

        Raises:
            ValueError: If the length of a list doesn't match its corresponding quantity field.
        """
        qty_fields = {'qty_machs': 'machs', 'qty_alphas': 'alphas', 'qty_altitudes': 'altitudes'}
        for qty_field, list_field in qty_fields.items():
            qty = values.get(qty_field)
            lst = values.get(list_field)
            if qty is not None and lst is not None and len(lst) != qty:
                raise ValueError(f"Length of {list_field} must match {qty_field}")
        return values

class ConfigurationLayout(CommonBaseModel):
    center_of_gravity_station: Optional[float] = Field(None, description="Airplane Center-of-Gravity station - in")
    center_of_gravity_waterline: Optional[float] = Field(None, description="Airplane Center-of-Gravity waterline - in")
    canard_apex_station: Optional[float] = Field(None, ge=0, description="Longitudinal station of the canard apex")
    canard_apex_waterline: Optional[float] = Field(None, description="Vertical waterline of the canard apex")
    canard_hinge_station: Optional[float] = Field(None, description="Station of canard hinge axis")
    canard_angle_of_incidence: Optional[float] = Field(None, description="Angle of incidence of canard")
    wing_apex_station: Optional[float] = Field(None, ge=0, description="Longitudinal location of the wing apex")
    wing_apex_waterline: Optional[float] = Field(None, description="Vertical location of the wing apex")
    wing_hinge_station: Optional[float] = Field(None, description="Station of wing hinge axis")
    wing_angle_of_incidence: Optional[float] = Field(None, description="Angle of incidence of the wing")
    horizontal_apex_station: Optional[float] = Field(None, ge=0, description="Longitudinal location of the horizontal tail apex")
    horizontal_apex_waterline: Optional[float] = Field(None, description="Vertical location of the horizontal tail apex")
    horizontal_hinge_station: Optional[float] = Field(None, description="Station of horizontal hinge axis")
    horizontal_angle_of_incidence: Optional[float] = Field(None, description="Angle of incidence of the horizontal tail")
    vertical_apex_station: Optional[float] = Field(None, ge=0, description="Longitudinal location of the vertical tail apex")
    vertical_apex_waterline: Optional[float] = Field(None, description="Vertical location of the vertical tail apex")
    vertical_cant: Optional[float] = Field(None, description="Cant angle of the vertical tail")
    vertical_offset: Optional[float] = Field(None, description="Lateral location of the vertical tail")
    vertical_above: Optional[bool] = Field(True, description="Flag indicating if the vertical tail is above (true) or below (false) reference plane")
    fin_apex_station: Optional[float] = Field(None, ge=0, description="Longitudinal location of the ventral fin apex")
    fin_apex_waterline: Optional[float] = Field(None, description="Vertical location of the ventral fin apex")
    fin_cant: Optional[float] = Field(None, description="Cant angle of the fin")
    fin_offset: Optional[float] = Field(None, description="Lateral location of the fin")
    model_scale: Optional[float] = Field(None, gt=0, description="Scale factor for model")

    @field_validator('center_of_gravity_station', 'center_of_gravity_waterline', 
                     'canard_apex_station', 'canard_apex_waterline', 'canard_hinge_station', 'canard_angle_of_incidence', 
                     'wing_apex_station', 'wing_apex_waterline', 'wing_angle_of_incidence',
                     'horizontal_apex_station', 'horizontal_apex_waterline', 'horizontal_hinge_station', 'horizontal_angle_of_incidence',
                     'vertical_apex_station', 'vertical_apex_waterline', 'vertical_cant', 'vertical_offset', 'vertical_above',
                     'fin_apex_station', 'fin_apex_waterline', 'fin_cant', 'fin_offset',
                     'model_scale', mode='before')
    def check_values_not_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Values must be non-negative or positive")
        return v

class Airfoil(CommonBaseModel):
    spline: Optional[Spline] = Field(
        None,
        description="A spline defining the contour of the airfoil section.",
    )

    @field_validator("spline")
    def validate_spline(cls, value: Optional[Spline]) -> Spline:
        if value is None:
            raise ValueError("The spline defining the airfoil contour must be provided.")
        return value

    input_type: Optional[int] = Field(None, ge=0, description="Input Type: 1 - Upper and Lower, 2 - Camber and Thickness")
    qty_coordinates: Optional[int] = Field(None, ge=0, description="Number of points")
    x_coordinates: List[Optional[float]] = Field(default_factory=list, description="X-coordinates")
    z_upper: List[Optional[float]] = Field(default_factory=list, description="Upper surface Z-coordinates")
    z_lower: List[Optional[float]] = Field(default_factory=list, description="Lower surface Z-coordinates")
    camber_line: List[Optional[float]] = Field(default_factory=list, description="Mean line coordinates")
    thickness_profile: List[Optional[float]] = Field(default_factory=list, description="Thickness distribution")
    inboard_rLEoC: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Leading edge radius")
    inboard_ToCmax: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Maximum Thickness-to-chord ratio")
    inboard_XoC_for_ToCmax: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Chordwise fraction of ToCmax")
    inboard_closure_angle: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Trailing Edge Closure angle")
    inboard_TE_ToC: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Trailing Edge Thickness-to-chord ratio")
    inboard_LE_droop: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Leading Edge droop angle")
    inboard_ZoCmax: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Maximum Camber-to-chord ratio")
    inboard_XoC_for_ZoCmax: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Chordwise fraction of ZoCmax")
    inboard_TE_droop: Optional[float] = Field(None, ge=0, description="Inboard Airfoil Trailing Edge droop angle")
    outboard_rLEoC: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Leading edge radius")
    outboard_ToCmax: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Maximum Thickness-to-chord ratio")
    outboard_XoC_for_ToCmax: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Chordwise fraction of ToCmax")
    outboard_closure_angle: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Trailing Edge Closure angle")
    outboard_TE_ToC: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Trailing Edge Thickness-to-chord ratio")
    outboard_LE_droop: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Leading Edge droop angle")
    outboard_ZoCmax: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Maximum Camber-to-chord ratio")
    outboard_XoC_for_ZoCmax: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Chordwise fraction of ZoCmax")
    outboard_TE_droop: Optional[float] = Field(None, ge=0, description="Outboard Airfoil Trailing Edge droop angle")

class PlanformType(Enum):
    RECTANGULAR = 1
    ELLIPTICAL = 2
    SWEPT = 3

class LiftingSurface(CommonBaseModel):
    tip_chord: Optional[float] = Field(None, ge=0, description="Tip chord")
    outboard_panel_semi_span: Optional[float] = Field(None, ge=0, description="Outboard panel semi-span")
    exposed_panel_semi_span: Optional[float] = Field(None, ge=0, description="Exposed panel semi-span from side-of-body")
    total_panel_semi_span: Optional[float] = Field(None, ge=0, description="Theoretical panel semi-span from centerline")
    breakpoint_chord: Optional[float] = Field(None, ge=0, description="Chord at break point")
    root_chord: Optional[float] = Field(None, ge=0, description="Root chord")
    inboard_panel_sweep: Optional[float] = Field(None, description="Inboard panel sweep angle")
    outboard_panel_sweep: Optional[float] = Field(None, description="Outboard panel sweep angle")
    reference_chord_fraction: Optional[float] = Field(0.25, gt=0, lt=1, description="Reference chord fraction for inboard and outboard sweep angles")
    twist_angle: Optional[float] = Field(None, description="Twist angle, negative leading edge rotated down")
    inboard_panel_dihedral: Optional[float] = Field(None, description="Inboard panel dihedral angle")
    outboard_panel_dihedral: Optional[float] = Field(None, description="Outboard panel dihedral angle")
    planform_type: Optional[PlanformType] = Field(None, description="Planform type: 1.0 Straight tapered, 2.0 - Double Delta, 3.0 - Cranked")
    shock_impengement_area: Optional[float] = Field(None, ge=0, description="Fuselage portion covered by shock zone emanating from root of horizontal")
    extended_shock_impengement_area: Optional[float] = Field(None, ge=0, description="Extended Fuselage portion covered by shock zone emanating from root of horizontal")
    distance_between_CG_and_centroid: Optional[float] = Field(None, description="Longitudinal Distance between CG and centroid of stabilizer")
    vertical_panel_exposed_root_chord: Optional[float] = Field(None, ge=0, description="Exposed Vertical Panel Area of Wing exposed root chord")
    vertical_panel_not_influenced_by_wing: Optional[float] = Field(None, ge=0, description="Exposed Vertical Panel Area not influenced by Wing or Horizontal")
    horizontal_panel_exposed_root_chord: Optional[float] = Field(None, ge=0, description="Exposed Vertical Panel Area of Horizontal exposed root chord")

    @field_validator('tip_chord', 'outboard_panel_semi_span', 'exposed_panel_semi_span', 'total_panel_semi_span', 'breakpoint_chord', 'root_chord', 'shock_impengement_area', 'extended_shock_impengement_area', 'vertical_panel_exposed_root_chord', 'vertical_panel_not_influenced_by_wing', 'horizontal_panel_exposed_root_chord', mode='before')
    def check_non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Values must be non-negative")
        return v

    @field_validator('reference_chord_fraction', mode='before')
    def check_chstat_range(cls, v):
        if v is not None and (v <= 0 or v >= 1):
            raise ValueError("Reference chord fraction must be between 0 and 1")
        return v

class TwinVerticalTail(CommonBaseModel):
    span_above: Optional[float] = Field(None, description="Vertical Panel Span above lifting surface")
    total_span: Optional[float] = Field(None, description="Vertical Panel Span")
    body_depth: Optional[float] = Field(None, description="Fuselage depth at MAC/4")
    separation: Optional[float] = Field(None, description="Distance between Vertical tails")
    planform_area: Optional[float] = Field(None, description="Planform Area of one vertical tail")
    closure_angle: Optional[float] = Field(None, description="Trailing Edge Closure Angle of Vertical tail")
    lateral_arm: Optional[float] = Field(None, description="Vertical Tail lateral arm aft of CG")
    vertical_arm: Optional[float] = Field(None, description="Vertical Tail Moment Arm above CG")

    @field_validator('span_above', 'total_span', 'body_depth', 'separation', 'planform_area', 'closure_angle', 'lateral_arm', 'vertical_arm', mode='before')
    def check_values_not_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError('Values must not be negative')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "span_above": 1.5,
                "total_span": 0.5,
                "body_depth": 2.0,
                "separation": 0.3,
                "planform_area": 1.0,
                "closure_angle": 0.8,
                "lateral_arm": 0.2,
                "vertical_arm": 0.1
            }
        }
    }

class GroundEffectsDefinition(CommonBaseModel):
    heights: List[Optional[float]] = Field(default_factory=list, description="Ground heights")
    qty_heights: Optional[int] = Field(None, description="Number of grid heights")

    @field_validator('heights', mode='before')
    def check_grdht_values(cls, v):
        if v is not None and any(item is not None and (item < 0.0 or item > 1000.0) for item in v):
            raise ValueError('Grid height must be between 0 and 1000')
        return v

    @field_validator('qty_heights', mode='before')
    def check_ngh_value(cls, v, values):
        heights = len(values.data['heights']) if 'heights' in values.data else 0
        if v is not None and v != heights:
            raise ValueError('qty_heights must equal the number of grid heights provided')
        return v

    model_config = {
        "str_min_length": 1,
        "str_strip_whitespace": True,
        "json_schema_extra": {
            "example": {
                "qty_heights": 5,
                "heights": [100.0, 200.0, 300.0, 400.0, 500.0]
            }
        }
    }

class FlapType(Enum):
    NONE = 0
    PLAIN = 1
    SINGLE = 2
    FOWLER = 3
    DOUBLE = 4
    TRIPLE = 0
    SPLIT = 5
    LE_FLAP = 6
    LE_SLATS = 7
    KRUEGER = 8

class NoseType(Enum):
    ROUND = 1
    ELLIPTIC = 2
    SHARP = 3

class BlowingType(Enum):
    NONE = 0
    PURE = 1
    IBF = 2
    EBF = 3
    COMBINED = 4

class SymmetricFlap(CommonBaseModel):
    flap_type: Optional[FlapType] = Field(None, description="Flap type: 1 - Plain, 2 - Single, 3 - Fowler, 4 - Double, 0 - Triple, 5 - Split, 6 - LE_Flap, 7 - LE_Slats, 8 - Krueger")
    nose_type: Optional[NoseType] = Field(None, description="Nose type: 1 - Round, 2 - Elliptic, 3 - Sharp")
    blowing_type: Optional[BlowingType] = Field(None, description="Blowing type: 0 - None, 1 - Pure, 2 - IBF, 3 - EBF, 4 - Mech Jet")
    balance_chord_ratio: Optional[float] = Field(None, description="Average balance chord ratio")
    hinge_thickness_to_chord_ratio: Optional[float] = Field(None, description="Average thickness-to-Chord ratio at hinge line")
    qty_deflections: Optional[int] = Field(None, description="Number of deflection angles")
    deflections: List[Optional[float]] = Field(default_factory=list, description="Leading edge deflections")
    inboard_chord_ratio: List[Optional[float]] = Field(default_factory=list, description="Chord ratio at flap inboard edge")
    outboard_chord_ratio: List[Optional[float]] = Field(default_factory=list, description="Chord ratio at flap outboard edge")
    inboard_span_ratio: List[Optional[float]] = Field(default_factory=list, description="Span ratio at flap inboard edge")
    outboard_span_ratio: List[Optional[float]] = Field(default_factory=list, description="Span ratio at flap outboard edge")
    inboard_fowler_action: List[Optional[float]] = Field(default_factory=list, description="Fowler action of inboard flap")
    outboard_fowler_action: List[Optional[float]] = Field(default_factory=list, description="Fowler action of outboard flap")
    jet_deflection: List[Optional[float]] = Field(default_factory=list, description="Jet deflection angles")
    EBF_jet_deflection_angles: List[Optional[float]] = Field(default_factory=list, description="EBF Jet deflection angles")
    jet_efflux: Optional[float] = Field(None, description="2D jet efflux coefficient")
    flap_Lift_increment: List[Optional[float]] = Field(default_factory=list, description="Lift Coefficient increment due to flap deflection")
    flap_Pitch_increment: List[Optional[float]] = Field(default_factory=list, description="Pitching Moment Coefficient increment due to flap deflection")

    @field_validator('balance_chord_ratio', 'hinge_thickness_to_chord_ratio', 'jet_efflux', mode='before')
    def check_values_not_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError('Values must not be negative')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "balance_chord_ratio": 0.1,
                "hinge_thickness_to_chord_ratio": 0.2,
                "qty_deflections": 2,
                "deflections": [10.0, 20.0],
                "inboard_chord_ratio": [0.1, 0.2],
                "outboard_chord_ratio": [0.3, 0.4],
                "inboard_span_ratio": [0.5, 0.6],
                "outboard_span_ratio": [0.7, 0.8],
                "inboard_fowler_action": [0.9, 1.0],
                "outboard_fowler_action": [1.1, 1.2],
                "jet_deflection": [1.3, 1.4],
                "EBF_jet_deflection_angles": [1.5, 1.6],
                "jet_efflux": 1.7,
                "flap_Lift_increment": [1.8, 1.9],
                "flap_Pitch_increment": [2.0, 2.1]
            }
        }
    }

class ControlType(Enum):
    FLAP = 1
    PLUG = 2
    SLOT = 3
    AILERON = 4
    STABILIZER = 5

class AsymmetricControl(CommonBaseModel):
    control_type: Optional[ControlType] = Field(None, description="Control type identifier: 1 - FLAP, 2 - PLUG, 3 - SLOT, 4 - AILERON, 5 - STABILIZER")
    qty_deflections: Optional[int] = Field(None, description="Number of control deflections")
    inboard_aileron_chord_ratio: Optional[float] = Field(None, description="Inboard aileron chord ratio")
    outboard_aileron_chord_ratio: Optional[float] = Field(None, description="Outboard aileron chord ratio")
    inboard_span_ratio: Optional[float] = Field(None, description="Inboard span ratio")
    outboard_span_ratio: Optional[float] = Field(None, description="Outboard span ratio")
    left_deflection: List[Optional[float]] = Field(default_factory=list, description="Left side deflection angles")
    right_deflection: List[Optional[float]] = Field(default_factory=list, description="Right side deflection angles")
    deflector_height_chord_ratio: List[Optional[float]] = Field(default_factory=list, description="Deflector height to chord ratio")
    spoiler_height_ratio: List[Optional[float]] = Field(default_factory=list, description="Spoiler height to chord ratio")
    spoiler_chord_ratio: List[Optional[float]] = Field(default_factory=list, description="Spoiler chord ratio")
    hingeline_chord_ratio: Optional[float] = Field(None, description="Hingeline chord ratio")

    @field_validator('inboard_aileron_chord_ratio', 'outboard_aileron_chord_ratio', 'inboard_span_ratio', 'outboard_span_ratio', 'hingeline_chord_ratio', mode='before')
    def check_values_not_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError('Values must not be negative')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "control_type": ControlType.AILERON,
                "qty_deflections": 2,
                "inboard_aileron_chord_ratio": 0.1,
                "outboard_aileron_chord_ratio": 0.2,
                "inboard_span_ratio": 0.3,
                "outboard_span_ratio": 0.4,
                "left_deflection": [10.0, 20.0],
                "right_deflection": [15.0, 25.0],
                "deflector_height_chord_ratio": [0.05, 0.06],
                "spoiler_height_ratio": [0.07, 0.08],
                "spoiler_chord_ratio": [0.09, 0.1],
                "hingeline_chord_ratio": 0.11
            }
        }
    }

class BodyShape(Enum):
    """
    Enumeration of body shape types.
    """
    CONICAL = 1
    OGIVE = 2
    ELLIPTICAL = 3

class TailShape(Enum):
    """
    Enumeration of tail shape types.
    """
    FLAT = 1
    ROUND = 2
    POINTED = 3

class Body(CommonBaseModel):
    """
    Represents the parameters of a body.

    Attributes:
        qty_cross_sections (Optional[int]): Number of cross-sections.
        stations (List[Optional[float]]): Axial stations.
        cross_sectional_areas (List[Optional[float]]): Cross-sectional areas at stations.
        cross_sectional_perimeters (List[Optional[float]]): Perimeters at stations.
        max_halfbredth (List[Optional[float]]): Maximum Halfbredth at stations.
        crown_line (List[Optional[float]]): Crown line height at stations.
        keel_line (List[Optional[float]]): Keel Line height at stations.
        nose_type (Optional[BodyShape]): Type of nose geometry.
        aftbody_type (Optional[BodyShape]): Type of aftbody geometry.
        nose_length (Optional[float]): Nose length.
        aftbody_length (Optional[float]): Afterbody length.
        nose_bluntness (Optional[float]): Diameter of nose bluntness.
        area_rule (Optional[int]): Area Ruling: 1 - Straight Wing, None, 2 - Swept Wing, None, 3 - area ruled.
    """
    qty_cross_sections: Optional[int] = Field(None, ge=1, description="Number of cross-sections")
    stations: List[Optional[float]] = Field(default_factory=list, description="Axial stations")
    cross_sectional_areas: List[Optional[float]] = Field(default_factory=list, description="Cross-sectional areas at stations")
    cross_sectional_perimeters: List[Optional[float]] = Field(default_factory=list, description="Perimeters at stations")
    max_halfbredth: List[Optional[float]] = Field(default_factory=list, description="Maximum Halfbredth at stations")
    crown_line: List[Optional[float]] = Field(default_factory=list, description="Crown line height at stations")
    keel_line: List[Optional[float]] = Field(default_factory=list, description="Keel Line height at stations")
    nose_type: Optional[BodyShape] = Field(None, description="Type of nose geometry: 1 - Conical, 2 - Ogive")
    aftbody_type: Optional[BodyShape] = Field(None, description="Type of aftbody geometry: 1 - Conical, 2 - Ogive")
    nose_length: Optional[float] = Field(None, ge=0, description="Nose length")
    aftbody_length: Optional[float] = Field(None, ge=0, description="Afterbody length")
    nose_bluntness: Optional[float] = Field(None, ge=0, description="Diameter of nose bluntness")
    area_rule: Optional[int] = Field(None, ge=0, description="Area Ruling: 1 - Straight Wing, None, 2 - Swept Wing, None, 3 - area ruled")

    @field_validator('stations', 'cross_sectional_areas', 'cross_sectional_perimeters', 'max_halfbredth', 'crown_line', 'keel_line')
    @classmethod
    def validate_non_negative(cls, v: List[Optional[float]]) -> List[Optional[float]]:
        """
        Validate that all values in the list are non-negative.

        Args:
            v (List[Optional[float]]): The list of values to validate.

        Returns:
            List[Optional[float]]: The validated list of values.

        Raises:
            ValueError: If any value in the list is negative.
        """
        if v is not None and any(item is not None and item < 0 for item in v):
            raise ValueError("Values must be non-negative")
        return v

    @model_validator(mode='before')
    def validate_list_length(cls, values):
        """
        Validate that the length of lists matches the number of cross-sections.

        Args:
            values (dict): The current values of the model.

        Returns:
            dict: The validated values.

        Raises:
            ValueError: If the length of any list doesn't match the number of cross-sections.
        """
        qty_cross_sections = values.get('qty_cross_sections')
        if qty_cross_sections is not None:
            for field in ['stations', 'cross_sectional_areas', 'cross_sectional_perimeters', 'max_halfbredth', 'crown_line', 'keel_line']:
                if len(values.get(field, [])) != qty_cross_sections:
                    raise ValueError(f"Length of {field} must match qty_cross_sections")
        return values

class LowAspectRatioWingBody(CommonBaseModel):
    body_centroid_height: Optional[float] = Field(None, description="Height of Base Area Centroid above reference plane")
    reference_area: Optional[float] = Field(None, description="Planform Reference area")
    sharpness: Optional[float] = Field(None, description="Sharp Leading Edge Parameter")
    frontal_area: Optional[float] = Field(None, description="Projected Frontal Area at zero normal force.")
    aspect_ratio: Optional[float] = Field(None, description="Round leading edge parameter")
    effective_radius: Optional[float] = Field(None, description="Parameter related to leading edge")
    lower_surface_angle: Optional[float] = Field(None, description="Lower surface angle of round leading edge wing")
    reference_length: Optional[float] = Field(None, description="Length parameter")
    wetted_area: Optional[float] = Field(None, description="Wetted area excluding base area")
    base_perimeter: Optional[float] = Field(None, description="Perimeter of base")
    base_area: Optional[float] = Field(None, description="Base area")
    base_max_height: Optional[float] = Field(None, description="Maximum height of base")
    base_max_span: Optional[float] = Field(None, description="Maximum span of base")
    base_aft_of_lifting_surface: Optional[bool] = Field(None, description="True - Portions of base aft of lifting surface, False - Entire base is aft of lifting surface")
    center_of_gravity_station: Optional[float] = Field(None, description="Center of gravity along X-axis")
    semi_apex_angle: Optional[float] = Field(None, description="Wing semi-apex angle")
    rounded_nose_flag: Optional[bool] = Field(None, description="True - Rounded nose, False - Sharp Nose")
    total_side_area: Optional[float] = Field(None, description="Total Side area")
    nose_side_area: Optional[float] = Field(None, description="Side area forward of 20% body length")
    distance_to_side_centroid: Optional[float] = Field(None, description="Axial distance from nose to side area centroid")
    distance_to_planform_centroid: Optional[float] = Field(None, description="Axial distance from nose to planform area centroid")

    @field_validator('body_centroid_height', 'reference_area', 'sharpness', 'frontal_area', 'aspect_ratio', 'effective_radius', 'lower_surface_angle', 'reference_length', 'wetted_area', 'base_perimeter', 'base_area', 'base_max_height', 'base_max_span', 'center_of_gravity_station', 'semi_apex_angle', 'total_side_area', 'nose_side_area', 'distance_to_side_centroid', 'distance_to_planform_centroid', mode='before')
    def check_values_not_negative(cls, v):
        if isinstance(v, float) and v < 0:
            raise ValueError('Numeric values must not be negative')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "body_centroid_height": 0.0,
                "reference_area": 1.2,
                "sharpness": 0.01,
                "frontal_area": 0.3,
                "aspect_ratio": 0.5,
                "effective_radius": 0.6,
                "lower_surface_angle": 0.7,
                "reference_length": 0.8,
                "wetted_area": 0.9,
                "base_perimeter": 1.0,
                "base_area": 1.1,
                "base_max_height": 1.2,
                "base_max_span": 1.3,
                "base_aft_of_lifting_surface": True,
                "center_of_gravity_station": 1.4,
                "semi_apex_angle": 1.5,
                "rounded_nose_flag": False,
                "total_side_area": 1.6,
                "nose_side_area": 1.7,
                "distance_to_side_centroid": 1.8,
                "distance_to_planform_centroid": 1.9
            }
        }
    }

class TransverseJetControl(CommonBaseModel):
    qty_time: Optional[int] = Field(None, description="Number of time history values")
    time: List[Optional[float]] = Field(default_factory=list, description="Time values")
    control_force: List[Optional[float]] = Field(default_factory=list, description="Control force required to trim")
    altitudes: List[Optional[float]] = Field(default_factory=list, description="Altitude values")
    boundary_layer_state: List[Optional[bool]] = Field(default_factory=list, description="Boundary Layer at Jet: True - Laminar, False - Turbulent")
    nozzle_exit_mach_number: Optional[float] = Field(None, description="Nozzle Exit Mach Number")
    jet_vacuum_specific_impulse: Optional[float] = Field(None, description="Jet vacuum specific impulse")
    nozzle_span: Optional[float] = Field(None, description="Span of nozzle normal to flow")
    nozzle_inclination: Optional[float] = Field(None, description="Nozzle centerline axis inclination relative to surface normal")
    propellant_specific_heat: Optional[float] = Field(None, description="Specific heat ratio of propellant")
    nozzle_discharge_coefficient: Optional[float] = Field(None, description="Nozzle Discharge coefficient")
    nozzle_distance_from_leading_edge: Optional[float] = Field(None, description="Nozzle distance from plate leading edge")

    @field_validator('time', 'control_force', 'altitudes', mode='before')
    def lists_must_match_qty_time(cls, v, values):
        qty_time = values.data['qty_time'] if 'qty_time' in values.data else None
        print("qty_time: ", qty_time)
        if qty_time is not None and len(v) != qty_time:
            raise ValueError(f'Length of {values.field_name} must match qty_time')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "qty_time": 3,
                "time": [0.1, 0.2, 0.3],
                "control_force": [1.0, 1.1, 1.2],
                "altitudes": [5.0, 5.1, 5.2],
                "boundary_layer_state": [True, False, True],
                "nozzle_exit_mach_number": 0.8,
                "jet_vacuum_specific_impulse": 300.0,
                "nozzle_span": 0.5,
                "nozzle_inclination": 15.0,
                "propellant_specific_heat": 1.4,
                "nozzle_discharge_coefficient": 0.98,
                "nozzle_distance_from_leading_edge": 2.0
            }
        }
    }

class HypersonicFlapControl(CommonBaseModel):
    altitude: Optional[float] = Field(None, description="Altitude")
    hingeline_chord_ratio: Optional[float] = Field(None, description="Distance from leading edge to hingeline to chord ratio")
    wall_to_freestream_temperature_ratio: Optional[float] = Field(None, description="Wall temperature to free stream static temperature ratio")
    control_chord_ratio: Optional[float] = Field(None, description="Control surface chord length")
    qty_deflections: Optional[int] = Field(None, description="Number of flap deflection values")
    deflections: List[Optional[float]] = Field(default_factory=list, description="Control deflection angles")
    boundary_layer_state: List[Optional[bool]] = Field(default_factory=list, description="Boundary Layer State: True - Laminar, False - Turbulent")

    @field_validator('deflections', mode='before')
    def check_deflections_length(cls, v, values):
        qty_deflections =  values.data['qty_deflections'] if 'qty_deflections' in values.data else None
        if qty_deflections is not None and len(v) != qty_deflections:
            raise ValueError(f'Length of deflections must match qty_deflections')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "altitude": 10.0,
                "hingeline_chord_ratio": 0.5,
                "wall_to_freestream_temperature_ratio": 1.0,
                "control_chord_ratio": 0.02,
                "boundary_layer_state": [True, False],
                "qty_deflections": 2,
                "deflections": [0.1, 0.2]
            }
        }
    }

# ToDo: Should the following parameters be moved into 'propulsion_parameters.py'

class EngineType(Enum):
    PISTON = 1
    TURBOPROP = 2

class PropellerPowerProperties(CommonBaseModel):
    thrust_incidence_angle: Optional[float] = Field(None, ge=0, description="Angle of incidence of the Engine thrust axis")
    qty_engines: Optional[int] = Field(None, ge=0, description="Number of engines (specific to propellers).")
    qty_blades: Optional[int] = Field(None, ge=0, description="Number of blades per engine.")
    counter_rotating: Optional[bool] = Field(None, description="True - Counter Rotating, False - Non-Counter Rotating")
    prop_radius: Optional[float] = Field(None, ge=0, description="Propeller radius.")
    rotation_direction: Optional[bool] = Field(None, description="Propeller rotation direction 1 - Clockwise, 2 - Counter-clockwise")
    thrust_coefficient: Optional[float] = Field(None, ge=0, description="Thrust coefficient of propeller.")
    hub_buttline: Optional[float] = Field(None, description="Lateral buttline of propeller")
    hub_station: Optional[float] = Field(None, description="Axial station of propeller.")
    hub_waterline: Optional[float] = Field(None, description="Vertical waterline of propeller.")
    blade_chord_ratio: List[Optional[float]] = Field(default_factory=list, description="Blade chord ratio vs fraction of radius")
    blade_angle: List[Optional[float]] = Field(default_factory=list, description="Blade angle vs fraction of radius")
    normal_force_factor: Optional[float] = Field(None, ge=0, description="Empirical Normal Force Factor")

    @field_validator('thrust_incidence_angle', 'prop_radius', 'thrust_coefficient', 'normal_force_factor', mode='before')
    def check_non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Values must be non-negative")
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "thrust_incidence_angle": 5.0,
                "qty_engines": 2,
                "qty_blades": 4,
                "counter_rotating": True,
                "prop_radius": 1.5,
                "rotation_direction": True,
                "thrust_coefficient": 0.8,
                "hub_buttline": 0.5,
                "hub_station": 2.0,
                "hub_waterline": 1.0,
                "blade_chord_ratio": [0.1, 0.2, 0.3],
                "blade_angle": [15.0, 20.0, 25.0],
                "normal_force_factor": 1.2
            }
        }
    }

class JetEngineType(Enum):
    TURBOJET = 1
    TURBOFAN = 2
    RAMJET = 3

class JetPowerProperties(CommonBaseModel):
    qty_engines: Optional[int] = Field(None, ge=0, description="Number of jet engines.")
    centerline_buttline: Optional[float] = Field(None, description="Lateral buttline of jet engine centerline.")
    thrust_incidence_angle: Optional[float] = Field(None, ge=0, description="Angle-of-Incidence of Engine thrust line")
    thrust_coefficient: Optional[float] = Field(None, ge=0, description="Thrust coefficient for jet engine.")
    inlet_area: Optional[float] = Field(None, ge=0, description="Jet inlet area.")
    inlet_station: Optional[float] = Field(None, description="Axial station of Jet Engine Inlet")
    exhaust_diameter: Optional[float] = Field(None, ge=0, description="Jet engine exhaust diameter.")
    exhaust_station: Optional[float] = Field(None, description="Axial station of jet engine exhaust.")
    exhaust_waterline: Optional[float] = Field(None, description="Vertical waterline of jet engine exhaust.")
    exhaust_exit_angle: Optional[float] = Field(None, description="Jet exhaust angle with respect to the freestream.")
    exhaust_exit_velocity: Optional[float] = Field(None, ge=0, description="Jet exhaust velocity.")
    exhaust_static_temperature: Optional[float] = Field(None, description="Jet exhaust static temperature.")
    exhaust_total_pressure: Optional[float] = Field(None, ge=0, description="Jet Exhaust Total Pressure")
    ambient_temperature: Optional[float] = Field(None, description="Ambient temperature")
    ambient_static_pressure: Optional[float] = Field(None, description="Ambient static pressure.")

    @field_validator('thrust_incidence_angle', 'thrust_coefficient', 'inlet_area', 'exhaust_diameter', 'exhaust_exit_velocity', 'exhaust_total_pressure', mode='before')
    def validate_non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Values must be non-negative")
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "qty_engines": 2,
                "centerline_buttline": 0.5,
                "thrust_incidence_angle": 5.0,
                "thrust_coefficient": 0.8,
                "inlet_area": 1.2,
                "inlet_station": 2.0,
                "exhaust_diameter": 0.6,
                "exhaust_station": 3.0,
                "exhaust_waterline": 1.0,
                "exhaust_exit_angle": 15.0,
                "exhaust_exit_velocity": 300.0,
                "exhaust_static_temperature": 1500.0,
                "exhaust_total_pressure": 101325.0,
                "ambient_temperature": 288.15,
                "ambient_static_pressure": 101325.0
            }
        }
    }

# ToDo: This aerodynamics Data seems to belong in 'Behavior' and is redundant with DaveML?

class AerodynamicsData(CommonBaseModel):
    # Body
    CLalpha_body: List[Optional[float]] = Field(default_factory=list, description="Body lift curve slope vs Angle-of-attack, per deg")
    CMalpha_body: List[Optional[float]] = Field(default_factory=list, description="Body pitching moment slope vs Angle-of-attack, per deg")
    CD_body: List[Optional[float]] = Field(default_factory=list, description="Body drag coefficient vs Angle-of-attack, per deg")
    CL_body: List[Optional[float]] = Field(default_factory=list, description="Body lift coefficient vs Angle-of-attack, per deg")
    CM_body: List[Optional[float]] = Field(default_factory=list, description="Body pitching moment coefficient vs Angle-of-attack")

    # Canard
    ALPOC: Optional[float] = Field(None, description="Canard Zero Lift Angle-of-Attack, deg")
    ALPLC: Optional[float] = Field(None, description="Canard Angle-of-Attack where lift becomes non-linear, deg")
    ACLMC: Optional[float] = Field(None, description="Canard Angle-of-Attack for Maximum Lift, deg")
    CLMC: Optional[float] = Field(None, description="Canard Maximum Lift Coefficient")
    CLAC: List[Optional[float]] = Field(default_factory=list, description="Canard lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAC: List[Optional[float]] = Field(default_factory=list, description="Canard pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDC: List[Optional[float]] = Field(default_factory=list, description="Canard drag coefficient vs Angle-of-Attack")
    CLC: List[Optional[float]] = Field(default_factory=list, description="Canard lift coefficient vs Angle-of-Attack.")
    CMC: List[Optional[float]] = Field(default_factory=list, description="Canard pitching moment coefficient vs Angle-of-Attack")

    # Wing
    ALPOW: Optional[float] = Field(None, description="Wing Zero Lift Angle-of-Attack, deg")
    ALPLW: Optional[float] = Field(None, description="Wing Angle-of-Attack where lift becomes non-linear, deg")
    ACLMW: Optional[float] = Field(None, description="Wing Angle-of-Attack for Maximum Lift, deg")
    CLMW: Optional[float] = Field(None, description="Wing Maximum Lift Coefficient")
    CLAW: List[Optional[float]] = Field(default_factory=list, description="Wing lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAW: List[Optional[float]] = Field(default_factory=list, description="Wing pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDW: List[Optional[float]] = Field(default_factory=list, description="Wing drag coefficient vs Angle-of-Attack")
    CLW: List[Optional[float]] = Field(default_factory=list, description="Wing lift coefficient vs Angle-of-Attack.")
    CMW: List[Optional[float]] = Field(default_factory=list, description="Wing pitching moment coefficient vs Angle-of-Attack")

    # Horizontal Tail
    ALPOH: Optional[float] = Field(None, description="Horizontal Tail Zero Lift Angle-of-Attack")
    ALPLH: Optional[float] = Field(None, description="Horizontal Angle-of-Attack where lift becomes non-linear, deg")
    ACLMH: Optional[float] = Field(None, description="Horizontal Angle-of-Attack for Maximum Lift, deg")
    CLMH: Optional[float] = Field(None, description="Horizontal Maximum Lift Coefficient")
    CLAH: List[Optional[float]] = Field(default_factory=list, description="Horizontal lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAH: List[Optional[float]] = Field(default_factory=list, description="Horizontal pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDH: List[Optional[float]] = Field(default_factory=list, description="Horizontal drag coefficient vs Angle-of-Attack")
    CLH: List[Optional[float]] = Field(default_factory=list, description="Horizontal lift coefficient vs Angle-of-Attack.")
    CMH: List[Optional[float]] = Field(default_factory=list, description="Horizontal pitching moment coefficient vs Angle-of-Attack")

    # Vertical Tail
    ALPOV: Optional[float] = Field(None, description="Vertical Tail Zero Lift Angle-of-Attack")
    ALPLV: Optional[float] = Field(None, description="Vertical Angle-of-Attack where lift becomes non-linear, deg")
    ACLMV: Optional[float] = Field(None, description="Vertical Angle-of-Attack for Maximum Lift, deg")
    CLMV: Optional[float] = Field(None, description="Vertical Maximum Lift Coefficient")
    CLAV: List[Optional[float]] = Field(default_factory=list, description="Vertical lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAV: List[Optional[float]] = Field(default_factory=list, description="Vertical pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDV: List[Optional[float]] = Field(default_factory=list, description="Vertical drag coefficient vs Angle-of-Attack")
    CLV: List[Optional[float]] = Field(default_factory=list, description="Vertical lift coefficient vs Angle-of-Attack.")
    CMV: List[Optional[float]] = Field(default_factory=list, description="Vertical pitching moment coefficient vs Angle-of-Attack")

    # Fin
    ALPOF: Optional[float] = Field(None, description="Fin Tail Zero Lift Angle-of-Attack")
    ALPLF: Optional[float] = Field(None, description="Fin Angle-of-Attack where lift becomes non-linear, deg")
    ACLMF: Optional[float] = Field(None, description="Fin Angle-of-Attack for Maximum Lift, deg")
    CLMF: Optional[float] = Field(None, description="Fin Maximum Lift Coefficient")
    CLAF: List[Optional[float]] = Field(default_factory=list, description="Fin lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAF: List[Optional[float]] = Field(default_factory=list, description="Fin pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDF: List[Optional[float]] = Field(default_factory=list, description="Fin drag coefficient vs Angle-of-Attack")
    CLF: List[Optional[float]] = Field(default_factory=list, description="Fin lift coefficient vs Angle-of-Attack.")
    CMF: List[Optional[float]] = Field(default_factory=list, description="Fin pitching moment coefficient vs Angle-of-Attack")

    # Wing-Body
    CLAWB: List[Optional[float]] = Field(default_factory=list, description="Wing-Body lift curve slope coefficient vs Angle-of-Attack, per deg")
    CMAWB: List[Optional[float]] = Field(default_factory=list, description="Wing-Body pitching moment slope coefficient vs Angle-of-attack, per deg")
    CDWB: List[Optional[float]] = Field(default_factory=list, description="Wing-Body drag coefficient vs Angle-of-Attack")
    CLWB: List[Optional[float]] = Field(default_factory=list, description="Wing-Body lift coefficient vs Angle-of-Attack.")
    CMWB: List[Optional[float]] = Field(default_factory=list, description="Wing-Body pitching moment coefficient vs Angle-of-Attack")

    DEODA: List[Optional[float]] = Field(default_factory=list, description="Downwash gradient vs Angle-of-Attack")
    EPSLON: List[Optional[float]] = Field(default_factory=list, description="Downwash angle vs Angle-of-Attack")
    QHOQINF: List[Optional[float]] = Field(default_factory=list, description="Horizontal to Freestream Dynamic Pressure Ratio vs Angle-of-Attack")

    @model_validator(mode='before')
    def check_list_lengths(cls, values):
        """
        Validates that all lists have the same length to ensure consistency in experimental data points.
        """
        list_lengths = [len(values[field]) for field in values if isinstance(values[field], list)]
        if len(set(list_lengths)) > 1:
            raise ValueError("All lists must have the same length.")
        return values

    @field_validator('CLalpha_body', 'CMalpha_body', 'CD_body', 'CL_body', 'CM_body', 'CLAC', 'CMAC', 'CDC', 'CLC', 'CMC', 'CLAW', 'CMAW', 'CDW', 'CLW', 'CMW', 'CLAH', 'CMAH', 'CDH', 'CLH', 'CMH', 'CLAV', 'CMAV', 'CDV', 'CLV', 'CMV', 'CLAF', 'CMAF', 'CDF', 'CLF', 'CMF', 'CLAWB', 'CMAWB', 'CDWB', 'CLWB', 'CMWB', 'DEODA', 'EPSLON', 'QHOQINF', mode='before')
    def validate_non_negative(cls, v):
        """
        Ensures that coefficient values are non-negative, where applicable.
        """
        if isinstance(v, list):
            for item in v:
                if item is not None and item < 0:
                    raise ValueError("Coefficient values must be non-negative.")
        else:
            if v is not None and v < 0:
                raise ValueError("Coefficient values must be non-negative.")
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "CLalpha_body": [0.1, 0.2, 0.3],
                "CMalpha_body": [0.01, 0.02, 0.03],
                "CD_body": [0.001, 0.002, 0.003],
                "CL_body": [0.1, 0.2, 0.3],
                "CM_body": [0.01, 0.02, 0.03],
                "ALPOC": 0.5,
                "ALPLC": 1.0,
                "ACLMC": 1.5,
                "CLMC": 0.8,
                "CLAC": [0.1, 0.2, 0.3],
                "CMAC": [0.01, 0.02, 0.03],
                "CDC": [0.001, 0.002, 0.003],
                "CLC": [0.1, 0.2, 0.3],
                "CMC": [0.01, 0.02, 0.03],
                "ALPOW": 0.5,
                "ALPLW": 1.0,
                "ACLMW": 1.5,
                "CLMW": 0.8,
                "CLAW": [0.1, 0.2, 0.3],
                "CMAW": [0.01, 0.02, 0.03],
                "CDW": [0.001, 0.002, 0.003],
                "CLW": [0.1, 0.2, 0.3],
                "CMW": [0.01, 0.02, 0.03],
                "ALPOH": 0.5,
                "ALPLH": 1.0,
                "ACLMH": 1.5,
                "CLMH": 0.8,
                "CLAH": [0.1, 0.2, 0.3],
                "CMAH": [0.01, 0.02, 0.03],
                "CDH": [0.001, 0.002, 0.003],
                "CLH": [0.1, 0.2, 0.3],
                "CMH": [0.01, 0.02, 0.03],
                "ALPOV": 0.5,
                "ALPLV": 1.0,
                "ACLMV": 1.5,
                "CLMV": 0.8,
                "CLAV": [0.1, 0.2, 0.3],
                "CMAV": [0.01, 0.02, 0.03],
                "CDV": [0.001, 0.002, 0.003],
                "CLV": [0.1, 0.2, 0.3],
                "CMV": [0.01, 0.02, 0.03],
                "ALPOF": 0.5,
                "ALPLF": 1.0,
                "ACLMF": 1.5,
                "CLMF": 0.8,
                "CLAF": [0.1, 0.2, 0.3],
                "CMAF": [0.01, 0.02, 0.03],
                "CDF": [0.001, 0.002, 0.003],
                "CLF": [0.1, 0.2, 0.3],
                "CMF": [0.01, 0.02, 0.03],
                "CLAWB": [0.1, 0.2, 0.3],
                "CMAWB": [0.01, 0.02, 0.03],
                "CDWB": [0.001, 0.002, 0.003],
                "CLWB": [0.1, 0.2, 0.3],
                "CMWB": [0.01, 0.02, 0.03],
                "DEODA": [0.1, 0.2, 0.3],
                "EPSLON": [0.1, 0.2, 0.3],
                "QHOQINF": [0.1, 0.2, 0.3]
            }
        }
    }

class Parameters(CommonBaseModel):
    reference_data: Optional[ReferenceData] = Field(None, description="Reference data for the component.")
    flight_conditions: Optional[FlightConditions] = Field(None, description="Flight conditions for the component.")
    configuration_layout: Optional[ConfigurationLayout] = Field(None, description="Configuration layout for the component.")
    airfoil: Optional[Airfoil] = Field(None, description="Parameters of the airfoil.")
    lifting_surface: Optional[LiftingSurface] = Field(None, description="Parameters of the lifting surface.")
    twin_vertical_tail: Optional[TwinVerticalTail] = Field(None, description="Parameters of the twin vertical tail.")
    ground_effects_definition: Optional[GroundEffectsDefinition] = Field(None, description="Ground effects definition.")
    symmetric_flap: Optional[SymmetricFlap] = Field(None, description="Geometry of symmetric flaps.")
    asymmetric_control: Optional[AsymmetricControl] = Field(None, description="Geometry of asymmetric controls.")
    body: Optional[Body] = Field(None, description="Parameters of the body.")
    low_aspect_ratio_wing_body: Optional[LowAspectRatioWingBody] = Field(None, description="Parameters of the low aspect ratio wing body.")
    transverse_jet_control: Optional[TransverseJetControl] = Field(None, description="Parameters of the transverse jet control.")
    hypersonic_flap_control: Optional[HypersonicFlapControl] = Field(None, description="Parameters of the hypersonic flap control.")
    propeller_power_properties: Optional[PropellerPowerProperties] = Field(None, description="Properties of the propeller power.")
    jet_power_properties: Optional[JetPowerProperties] = Field(None, description="Properties of the jet power.")
    aerodynamics_data: Optional[AerodynamicsData] = Field(None, description="Aerodynamics data for the component.")

