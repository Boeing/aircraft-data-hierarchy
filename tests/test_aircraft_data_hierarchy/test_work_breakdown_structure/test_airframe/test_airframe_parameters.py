import unittest
from pydantic import ValidationError
from typing import List, Optional
from enum import Enum

# Import the models from the provided code
from aircraft_data_hierarchy.work_breakdown_structure.airframe.airframe_parameters import (
    ReferenceData, FlightConditions, ConfigurationLayout, Airfoil,
    PlanformType, LiftingSurface, TwinVerticalTail,
    GroundEffectsDefinition, FlapType, NoseType, BlowingType, SymmetricFlap,
    ControlType, AsymmetricControl, BodyShape,
    TailShape, Body, LowAspectRatioWingBody, TransverseJetControl,
    HypersonicFlapControl, EngineType, PropellerPowerProperties, JetEngineType,
    JetPowerProperties, AerodynamicsData
)

from aircraft_data_hierarchy.work_breakdown_structure.airframe.airframe_geometry import Point, Spline

class TestPydanticModels(unittest.TestCase):

    def test_reference_data(self):
        # Test valid data
        data = {
            "RougHgt": 0.01,
            "Sref": 100.0,
            "Cbar": 10.0,
            "BLref": 5.0
        }
        model = ReferenceData(**data)
        self.assertEqual(model.roughness, 0.01)
        self.assertEqual(model.reference_area, 100.0)
        self.assertEqual(model.reference_length, 10.0)
        self.assertEqual(model.lateral_reference, 5.0)

        # Test invalid roughness
        data["RougHgt"] = 0.03
        with self.assertRaises(ValidationError):
            ReferenceData(**data)

    def test_flight_conditions(self):
        # Test valid data
        data = {
            "loop_control": 2,
            "qty_machs": 2,
            "machs": [0.5, 0.8],
            "velocities": [300.0, 400.0],
            "qty_alphas": 2,
            "alphas": [5.0, 10.0],
            "reynolds_indicies": [1e6, 2e6],
            "qty_altitudes": 2,
            "altitudes": [10000.0, 20000.0],
            "static_pressures": [101325.0, 90000.0],
            "static_temperatures": [288.15, 273.15],
            "transonic_mach": 0.7,
            "supersonic_mach": 1.2,
            "hypersonic_flag": True,
            "transition_flag": True,
            "weight": 50000.0,
            "flight_path_angle": 1.0
        }
        model = FlightConditions(**data)
        self.assertEqual(model.loop_control, 2)
        self.assertEqual(model.qty_machs, 2)
        self.assertEqual(model.machs, [0.5, 0.8])
        self.assertEqual(model.velocities, [300.0, 400.0])
        self.assertEqual(model.qty_alphas, 2)
        self.assertEqual(model.alphas, [5.0, 10.0])
        self.assertEqual(model.reynolds_indicies, [1e6, 2e6])
        self.assertEqual(model.qty_altitudes, 2)
        self.assertEqual(model.altitudes, [10000.0, 20000.0])
        self.assertEqual(model.static_pressures, [101325.0, 90000.0])
        self.assertEqual(model.static_temperatures, [288.15, 273.15])
        self.assertEqual(model.transonic_mach, 0.7)
        self.assertEqual(model.supersonic_mach, 1.2)
        self.assertTrue(model.hypersonic_flag)
        self.assertTrue(model.transition_flag)
        self.assertEqual(model.weight, 50000.0)
        self.assertEqual(model.flight_path_angle, 1.0)

        # Test invalid machs
        data["machs"] = [-0.5, 0.8]
        with self.assertRaises(ValidationError):
            FlightConditions(**data)

    def test_configuration_layout(self):
        # Test valid data
        data = {
            "center_of_gravity_station": 10.0,
            "center_of_gravity_waterline": 5.0,
            "canard_apex_station": 15.0,
            "canard_apex_waterline": 7.0,
            "canard_hinge_station": 20.0,
            "canard_angle_of_incidence": 2.0,
            "wing_apex_station": 25.0,
            "wing_apex_waterline": 10.0,
            "wing_hinge_station": 30.0,
            "wing_angle_of_incidence": 3.0,
            "horizontal_apex_station": 35.0,
            "horizontal_apex_waterline": 12.0,
            "horizontal_hinge_station": 40.0,
            "horizontal_angle_of_incidence": 4.0,
            "vertical_apex_station": 45.0,
            "vertical_apex_waterline": 15.0,
            "vertical_cant": 5.0,
            "vertical_offset": 2.0,
            "vertical_above": True,
            "fin_apex_station": 50.0,
            "fin_apex_waterline": 20.0,
            "fin_cant": 6.0,
            "fin_offset": 3.0,
            "model_scale": 1.0
        }
        model = ConfigurationLayout(**data)
        self.assertEqual(model.center_of_gravity_station, 10.0)
        self.assertEqual(model.center_of_gravity_waterline, 5.0)
        self.assertEqual(model.canard_apex_station, 15.0)
        self.assertEqual(model.canard_apex_waterline, 7.0)
        self.assertEqual(model.canard_hinge_station, 20.0)
        self.assertEqual(model.canard_angle_of_incidence, 2.0)
        self.assertEqual(model.wing_apex_station, 25.0)
        self.assertEqual(model.wing_apex_waterline, 10.0)
        self.assertEqual(model.wing_hinge_station, 30.0)
        self.assertEqual(model.wing_angle_of_incidence, 3.0)
        self.assertEqual(model.horizontal_apex_station, 35.0)
        self.assertEqual(model.horizontal_apex_waterline, 12.0)
        self.assertEqual(model.horizontal_hinge_station, 40.0)
        self.assertEqual(model.horizontal_angle_of_incidence, 4.0)
        self.assertEqual(model.vertical_apex_station, 45.0)
        self.assertEqual(model.vertical_apex_waterline, 15.0)
        self.assertEqual(model.vertical_cant, 5.0)
        self.assertEqual(model.vertical_offset, 2.0)
        self.assertTrue(model.vertical_above)
        self.assertEqual(model.fin_apex_station, 50.0)
        self.assertEqual(model.fin_apex_waterline, 20.0)
        self.assertEqual(model.fin_cant, 6.0)
        self.assertEqual(model.fin_offset, 3.0)
        self.assertEqual(model.model_scale, 1.0)

        # Test invalid canard_apex_station
        data["canard_apex_station"] = -15.0
        with self.assertRaises(ValidationError):
            ConfigurationLayout(**data)

    def test_airfoil_geometry(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0)
        ]
        spline = Spline(points=points)
        data = {
            "spline": spline
        }
        model = Airfoil(**data)
        self.assertEqual(model.spline, spline)

        # NOTE: Data is optional
        # # Test missing spline
        # data = {}
        # with self.assertRaises(ValidationError):
        #     Airfoil(**data)

    def test_airfoil_parameters(self):
        # Test valid data
        data = {
            "input_type": 1,
            "qty_coordinates": 3,
            "x_coordinates": [0.0, 0.5, 1.0],
            "z_upper": [0.1, 0.2, 0.3],
            "z_lower": [0.0, -0.1, -0.2],
            "camber_line": [0.05, 0.1, 0.15],
            "thickness_profile": [0.1, 0.2, 0.3],
            "inboard_rLEoC": 0.01,
            "inboard_ToCmax": 0.1,
            "inboard_XoC_for_ToCmax": 0.2,
            "inboard_closure_angle": 0.3,
            "inboard_TE_ToC": 0.01,
            "inboard_LE_droop": 0.02,
            "inboard_ZoCmax": 0.03,
            "inboard_XoC_for_ZoCmax": 0.04,
            "inboard_TE_droop": 0.05,
            "outboard_rLEoC": 0.01,
            "outboard_ToCmax": 0.1,
            "outboard_XoC_for_ToCmax": 0.2,
            "outboard_closure_angle": 0.3,
            "outboard_TE_ToC": 0.01,
            "outboard_LE_droop": 0.02,
            "outboard_ZoCmax": 0.03,
            "outboard_XoC_for_ZoCmax": 0.04,
            "outboard_TE_droop": 0.05
        }
        model = Airfoil(**data)
        self.assertEqual(model.input_type, 1)
        self.assertEqual(model.qty_coordinates, 3)
        self.assertEqual(model.x_coordinates, [0.0, 0.5, 1.0])
        self.assertEqual(model.z_upper, [0.1, 0.2, 0.3])
        self.assertEqual(model.z_lower, [0.0, -0.1, -0.2])
        self.assertEqual(model.camber_line, [0.05, 0.1, 0.15])
        self.assertEqual(model.thickness_profile, [0.1, 0.2, 0.3])
        self.assertEqual(model.inboard_rLEoC, 0.01)
        self.assertEqual(model.inboard_ToCmax, 0.1)
        self.assertEqual(model.inboard_XoC_for_ToCmax, 0.2)
        self.assertEqual(model.inboard_closure_angle, 0.3)
        self.assertEqual(model.inboard_TE_ToC, 0.01)
        self.assertEqual(model.inboard_LE_droop, 0.02)
        self.assertEqual(model.inboard_ZoCmax, 0.03)
        self.assertEqual(model.inboard_XoC_for_ZoCmax, 0.04)
        self.assertEqual(model.inboard_TE_droop, 0.05)
        self.assertEqual(model.outboard_rLEoC, 0.01)
        self.assertEqual(model.outboard_ToCmax, 0.1)
        self.assertEqual(model.outboard_XoC_for_ToCmax, 0.2)
        self.assertEqual(model.outboard_closure_angle, 0.3)
        self.assertEqual(model.outboard_TE_ToC, 0.01)
        self.assertEqual(model.outboard_LE_droop, 0.02)
        self.assertEqual(model.outboard_ZoCmax, 0.03)
        self.assertEqual(model.outboard_XoC_for_ZoCmax, 0.04)
        self.assertEqual(model.outboard_TE_droop, 0.05)

        # TODO Need to validate coordinates first
        # # Test invalid x_coordinates
        # data["x_coordinates"] = [-0.1, 0.5, 1.0]
        # with self.assertRaises(ValidationError):
        #     Airfoil(**data)



    def test_lifting_surface_parameters(self):
        # Test valid data
        data = {
            "tip_chord": 1.0,
            "outboard_panel_semi_span": 2.0,
            "exposed_panel_semi_span": 3.0,
            "total_panel_semi_span": 4.0,
            "breakpoint_chord": 5.0,
            "root_chord": 6.0,
            "inboard_panel_sweep": 7.0,
            "outboard_panel_sweep": 8.0,
            "reference_chord_fraction": 0.25,
            "twist_angle": 9.0,
            "inboard_panel_dihedral": 10.0,
            "outboard_panel_dihedral": 11.0,
            "planform_type": PlanformType.RECTANGULAR,
            "shock_impengement_area": 12.0,
            "extended_shock_impengement_area": 13.0,
            "distance_between_CG_and_centroid": 14.0,
            "vertical_panel_exposed_root_chord": 15.0,
            "vertical_panel_not_influenced_by_wing": 16.0,
            "horizontal_panel_exposed_root_chord": 17.0
        }
        model = LiftingSurface(**data)
        self.assertEqual(model.tip_chord, 1.0)
        self.assertEqual(model.outboard_panel_semi_span, 2.0)
        self.assertEqual(model.exposed_panel_semi_span, 3.0)
        self.assertEqual(model.total_panel_semi_span, 4.0)
        self.assertEqual(model.breakpoint_chord, 5.0)
        self.assertEqual(model.root_chord, 6.0)
        self.assertEqual(model.inboard_panel_sweep, 7.0)
        self.assertEqual(model.outboard_panel_sweep, 8.0)
        self.assertEqual(model.reference_chord_fraction, 0.25)
        self.assertEqual(model.twist_angle, 9.0)
        self.assertEqual(model.inboard_panel_dihedral, 10.0)
        self.assertEqual(model.outboard_panel_dihedral, 11.0)
        self.assertEqual(model.planform_type, PlanformType.RECTANGULAR)
        self.assertEqual(model.shock_impengement_area, 12.0)
        self.assertEqual(model.extended_shock_impengement_area, 13.0)
        self.assertEqual(model.distance_between_CG_and_centroid, 14.0)
        self.assertEqual(model.vertical_panel_exposed_root_chord, 15.0)
        self.assertEqual(model.vertical_panel_not_influenced_by_wing, 16.0)
        self.assertEqual(model.horizontal_panel_exposed_root_chord, 17.0)

        # Test invalid reference_chord_fraction
        data["reference_chord_fraction"] = 1.5
        with self.assertRaises(ValidationError):
            LiftingSurface(**data)

    def test_twin_vertical_tail(self):
        # Test valid data
        data = {
            "span_above": 1.5,
            "total_span": 0.5,
            "body_depth": 2.0,
            "separation": 0.3,
            "planform_area": 1.0,
            "closure_angle": 0.8,
            "lateral_arm": 0.2,
            "vertical_arm": 0.1
        }
        model = TwinVerticalTail(**data)
        self.assertEqual(model.span_above, 1.5)
        self.assertEqual(model.total_span, 0.5)
        self.assertEqual(model.body_depth, 2.0)
        self.assertEqual(model.separation, 0.3)
        self.assertEqual(model.planform_area, 1.0)
        self.assertEqual(model.closure_angle, 0.8)
        self.assertEqual(model.lateral_arm, 0.2)
        self.assertEqual(model.vertical_arm, 0.1)

        # Test invalid span_above
        data["span_above"] = -1.5
        with self.assertRaises(ValidationError):
            TwinVerticalTail(**data)

    def test_ground_effects_definition(self):
        # Test valid data
        data = {
            "qty_heights": 5,
            "heights": [100.0, 200.0, 300.0, 400.0, 500.0]
        }
        model = GroundEffectsDefinition(**data)
        self.assertEqual(model.qty_heights, 5)
        self.assertEqual(model.heights, [100.0, 200.0, 300.0, 400.0, 500.0])

        # Test invalid heights
        data["heights"] = [-100.0, 200.0, 300.0, 400.0, 500.0]
        with self.assertRaises(ValidationError):
            GroundEffectsDefinition(**data)

        # Test mismatched qty_heights
        data = {
            "qty_heights": 4,
            "heights": [100.0, 200.0, 300.0, 400.0, 500.0]
        }
        with self.assertRaises(ValidationError):
            GroundEffectsDefinition(**data)

    def test_symmetric_flap_geometry(self):
        # Test valid data
        data = {
            "flap_type": FlapType.PLAIN,
            "nose_type": NoseType.ROUND,
            "blowing_type": BlowingType.NONE,
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
        model = SymmetricFlap(**data)
        self.assertEqual(model.flap_type, FlapType.PLAIN)
        self.assertEqual(model.nose_type, NoseType.ROUND)
        self.assertEqual(model.blowing_type, BlowingType.NONE)
        self.assertEqual(model.balance_chord_ratio, 0.1)
        self.assertEqual(model.hinge_thickness_to_chord_ratio, 0.2)
        self.assertEqual(model.qty_deflections, 2)
        self.assertEqual(model.deflections, [10.0, 20.0])
        self.assertEqual(model.inboard_chord_ratio, [0.1, 0.2])
        self.assertEqual(model.outboard_chord_ratio, [0.3, 0.4])
        self.assertEqual(model.inboard_span_ratio, [0.5, 0.6])
        self.assertEqual(model.outboard_span_ratio, [0.7, 0.8])
        self.assertEqual(model.inboard_fowler_action, [0.9, 1.0])
        self.assertEqual(model.outboard_fowler_action, [1.1, 1.2])
        self.assertEqual(model.jet_deflection, [1.3, 1.4])
        self.assertEqual(model.EBF_jet_deflection_angles, [1.5, 1.6])
        self.assertEqual(model.jet_efflux, 1.7)
        self.assertEqual(model.flap_Lift_increment, [1.8, 1.9])
        self.assertEqual(model.flap_Pitch_increment, [2.0, 2.1])

        # Test invalid balance_chord_ratio
        data["balance_chord_ratio"] = -0.1
        with self.assertRaises(ValidationError):
            SymmetricFlap(**data)

    def test_asymmetric_control_geometry(self):
        # Test valid data
        data = {
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
        model = AsymmetricControl(**data)
        self.assertEqual(model.control_type, ControlType.AILERON)
        self.assertEqual(model.qty_deflections, 2)
        self.assertEqual(model.inboard_aileron_chord_ratio, 0.1)
        self.assertEqual(model.outboard_aileron_chord_ratio, 0.2)
        self.assertEqual(model.inboard_span_ratio, 0.3)
        self.assertEqual(model.outboard_span_ratio, 0.4)
        self.assertEqual(model.left_deflection, [10.0, 20.0])
        self.assertEqual(model.right_deflection, [15.0, 25.0])
        self.assertEqual(model.deflector_height_chord_ratio, [0.05, 0.06])
        self.assertEqual(model.spoiler_height_ratio, [0.07, 0.08])
        self.assertEqual(model.spoiler_chord_ratio, [0.09, 0.1])
        self.assertEqual(model.hingeline_chord_ratio, 0.11)

        # Test invalid inboard_aileron_chord_ratio
        data["inboard_aileron_chord_ratio"] = -0.1
        with self.assertRaises(ValidationError):
            AsymmetricControl(**data)

        # Test mismatched deflection lengths
        data["left_deflection"] = [10.0]
        with self.assertRaises(ValidationError):
            AsymmetricControl(**data)

    def test_body_parameters(self):
        # Test valid data
        data = {
            "qty_cross_sections": 3,
            "stations": [0.1, 0.5, 0.9],
            "cross_sectional_areas": [1.0, 2.0, 3.0],
            "cross_sectional_perimeters": [4.0, 5.0, 6.0],
            "max_halfbredth": [7.0, 8.0, 9.0],
            "crown_line": [10.0, 11.0, 12.0],
            "keel_line": [13.0, 14.0, 15.0],
            "nose_type": BodyShape.CONICAL,
            "aftbody_type": BodyShape.OGIVE,
            "nose_length": 16.0,
            "aftbody_length": 17.0,
            "nose_bluntness": 18.0,
            "area_rule": 1
        }
        model = Body(**data)
        self.assertEqual(model.qty_cross_sections, 3)
        self.assertEqual(model.stations, [0.1, 0.5, 0.9])
        self.assertEqual(model.cross_sectional_areas, [1.0, 2.0, 3.0])
        self.assertEqual(model.cross_sectional_perimeters, [4.0, 5.0, 6.0])
        self.assertEqual(model.max_halfbredth, [7.0, 8.0, 9.0])
        self.assertEqual(model.crown_line, [10.0, 11.0, 12.0])
        self.assertEqual(model.keel_line, [13.0, 14.0, 15.0])
        self.assertEqual(model.nose_type, BodyShape.CONICAL)
        self.assertEqual(model.aftbody_type, BodyShape.OGIVE)
        self.assertEqual(model.nose_length, 16.0)
        self.assertEqual(model.aftbody_length, 17.0)
        self.assertEqual(model.nose_bluntness, 18.0)
        self.assertEqual(model.area_rule, 1)

        # Test invalid stations
        data["stations"] = [-0.1, 0.5, 0.9]
        with self.assertRaises(ValidationError):
            Body(**data)

    def test_low_aspect_ratio_wing_body(self):
        # Test valid data
        data = {
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
        model = LowAspectRatioWingBody(**data)
        self.assertEqual(model.body_centroid_height, 0.0)
        self.assertEqual(model.reference_area, 1.2)
        self.assertEqual(model.sharpness, 0.01)
        self.assertEqual(model.frontal_area, 0.3)
        self.assertEqual(model.aspect_ratio, 0.5)
        self.assertEqual(model.effective_radius, 0.6)
        self.assertEqual(model.lower_surface_angle, 0.7)
        self.assertEqual(model.reference_length, 0.8)
        self.assertEqual(model.wetted_area, 0.9)
        self.assertEqual(model.base_perimeter, 1.0)
        self.assertEqual(model.base_area, 1.1)
        self.assertEqual(model.base_max_height, 1.2)
        self.assertEqual(model.base_max_span, 1.3)
        self.assertTrue(model.base_aft_of_lifting_surface)
        self.assertEqual(model.center_of_gravity_station, 1.4)
        self.assertEqual(model.semi_apex_angle, 1.5)
        self.assertFalse(model.rounded_nose_flag)
        self.assertEqual(model.total_side_area, 1.6)
        self.assertEqual(model.nose_side_area, 1.7)
        self.assertEqual(model.distance_to_side_centroid, 1.8)
        self.assertEqual(model.distance_to_planform_centroid, 1.9)

        # Test invalid body_centroid_height
        data["body_centroid_height"] = -0.1
        with self.assertRaises(ValidationError):
            LowAspectRatioWingBody(**data)

    def test_transverse_jet_control(self):
        # Test valid data
        data = {
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
        model = TransverseJetControl(**data)
        self.assertEqual(model.qty_time, 3)
        self.assertEqual(model.time, [0.1, 0.2, 0.3])
        self.assertEqual(model.control_force, [1.0, 1.1, 1.2])
        self.assertEqual(model.altitudes, [5.0, 5.1, 5.2])
        self.assertEqual(model.boundary_layer_state, [True, False, True])
        self.assertEqual(model.nozzle_exit_mach_number, 0.8)
        self.assertEqual(model.jet_vacuum_specific_impulse, 300.0)
        self.assertEqual(model.nozzle_span, 0.5)
        self.assertEqual(model.nozzle_inclination, 15.0)
        self.assertEqual(model.propellant_specific_heat, 1.4)
        self.assertEqual(model.nozzle_discharge_coefficient, 0.98)
        self.assertEqual(model.nozzle_distance_from_leading_edge, 2.0)

        # Test invalid time length
        data["time"] = [0.1, 0.2]
        with self.assertRaises(ValidationError):
            TransverseJetControl(**data)

    def test_hypersonic_flap_control(self):
        # Test valid data
        data = {
            "altitude": 10.0,
            "hingeline_chord_ratio": 0.5,
            "wall_to_freestream_temperature_ratio": 1.0,
            "control_chord_ratio": 0.02,
            "qty_deflections": 2,
            "deflections": [0.1, 0.2],
            "boundary_layer_state": [True, False]
        }
        model = HypersonicFlapControl(**data)
        self.assertEqual(model.altitude, 10.0)
        self.assertEqual(model.hingeline_chord_ratio, 0.5)
        self.assertEqual(model.wall_to_freestream_temperature_ratio, 1.0)
        self.assertEqual(model.control_chord_ratio, 0.02)
        self.assertEqual(model.qty_deflections, 2)
        self.assertEqual(model.deflections, [0.1, 0.2])
        self.assertEqual(model.boundary_layer_state, [True, False])

        # Test invalid deflections length
        data["deflections"] = [0.1]
        with self.assertRaises(ValidationError):
            HypersonicFlapControl(**data)

    def test_propeller_power_properties(self):
        # Test valid data
        data = {
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
        model = PropellerPowerProperties(**data)
        self.assertEqual(model.thrust_incidence_angle, 5.0)
        self.assertEqual(model.qty_engines, 2)
        self.assertEqual(model.qty_blades, 4)
        self.assertTrue(model.counter_rotating)
        self.assertEqual(model.prop_radius, 1.5)
        self.assertTrue(model.rotation_direction)
        self.assertEqual(model.thrust_coefficient, 0.8)
        self.assertEqual(model.hub_buttline, 0.5)
        self.assertEqual(model.hub_station, 2.0)
        self.assertEqual(model.hub_waterline, 1.0)
        self.assertEqual(model.blade_chord_ratio, [0.1, 0.2, 0.3])
        self.assertEqual(model.blade_angle, [15.0, 20.0, 25.0])
        self.assertEqual(model.normal_force_factor, 1.2)

        # Test invalid thrust_incidence_angle
        data["thrust_incidence_angle"] = -5.0
        with self.assertRaises(ValidationError):
            PropellerPowerProperties(**data)

    def test_jet_power_properties(self):
        # Test valid data
        data = {
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
        model = JetPowerProperties(**data)
        self.assertEqual(model.qty_engines, 2)
        self.assertEqual(model.centerline_buttline, 0.5)
        self.assertEqual(model.thrust_incidence_angle, 5.0)
        self.assertEqual(model.thrust_coefficient, 0.8)
        self.assertEqual(model.inlet_area, 1.2)
        self.assertEqual(model.inlet_station, 2.0)
        self.assertEqual(model.exhaust_diameter, 0.6)
        self.assertEqual(model.exhaust_station, 3.0)
        self.assertEqual(model.exhaust_waterline, 1.0)
        self.assertEqual(model.exhaust_exit_angle, 15.0)
        self.assertEqual(model.exhaust_exit_velocity, 300.0)
        self.assertEqual(model.exhaust_static_temperature, 1500.0)
        self.assertEqual(model.exhaust_total_pressure, 101325.0)
        self.assertEqual(model.ambient_temperature, 288.15)
        self.assertEqual(model.ambient_static_pressure, 101325.0)

        # Test invalid thrust_incidence_angle
        data["thrust_incidence_angle"] = -5.0
        with self.assertRaises(ValidationError):
            JetPowerProperties(**data)

    def test_aerodynamics_data(self):
        # Test valid data
        data = {
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
        model = AerodynamicsData(**data)
        self.assertEqual(model.CLalpha_body, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMalpha_body, [0.01, 0.02, 0.03])
        self.assertEqual(model.CD_body, [0.001, 0.002, 0.003])
        self.assertEqual(model.CL_body, [0.1, 0.2, 0.3])
        self.assertEqual(model.CM_body, [0.01, 0.02, 0.03])
        self.assertEqual(model.ALPOC, 0.5)
        self.assertEqual(model.ALPLC, 1.0)
        self.assertEqual(model.ACLMC, 1.5)
        self.assertEqual(model.CLMC, 0.8)
        self.assertEqual(model.CLAC, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAC, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDC, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLC, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMC, [0.01, 0.02, 0.03])
        self.assertEqual(model.ALPOW, 0.5)
        self.assertEqual(model.ALPLW, 1.0)
        self.assertEqual(model.ACLMW, 1.5)
        self.assertEqual(model.CLMW, 0.8)
        self.assertEqual(model.CLAW, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAW, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDW, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLW, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMW, [0.01, 0.02, 0.03])
        self.assertEqual(model.ALPOH, 0.5)
        self.assertEqual(model.ALPLH, 1.0)
        self.assertEqual(model.ACLMH, 1.5)
        self.assertEqual(model.CLMH, 0.8)
        self.assertEqual(model.CLAH, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAH, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDH, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLH, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMH, [0.01, 0.02, 0.03])
        self.assertEqual(model.ALPOV, 0.5)
        self.assertEqual(model.ALPLV, 1.0)
        self.assertEqual(model.ACLMV, 1.5)
        self.assertEqual(model.CLMV, 0.8)
        self.assertEqual(model.CLAV, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAV, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDV, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLV, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMV, [0.01, 0.02, 0.03])
        self.assertEqual(model.ALPOF, 0.5)
        self.assertEqual(model.ALPLF, 1.0)
        self.assertEqual(model.ACLMF, 1.5)
        self.assertEqual(model.CLMF, 0.8)
        self.assertEqual(model.CLAF, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAF, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDF, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLF, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMF, [0.01, 0.02, 0.03])
        self.assertEqual(model.CLAWB, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMAWB, [0.01, 0.02, 0.03])
        self.assertEqual(model.CDWB, [0.001, 0.002, 0.003])
        self.assertEqual(model.CLWB, [0.1, 0.2, 0.3])
        self.assertEqual(model.CMWB, [0.01, 0.02, 0.03])
        self.assertEqual(model.DEODA, [0.1, 0.2, 0.3])
        self.assertEqual(model.EPSLON, [0.1, 0.2, 0.3])
        self.assertEqual(model.QHOQINF, [0.1, 0.2, 0.3])

        # Test invalid CLalpha_body
        data["CLalpha_body"] = [-0.1, 0.2, 0.3]
        with self.assertRaises(ValidationError):
            AerodynamicsData(**data)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
