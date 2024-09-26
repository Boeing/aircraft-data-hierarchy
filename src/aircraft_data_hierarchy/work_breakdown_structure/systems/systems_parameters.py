"""
Vehicle Systems module for aircraft system modeling.

This module provides Pydantic models for representing various aspects of aircraft systems,
including functional blocks, data signals, physical characteristics, and system attributes.
"""

from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Literal, Tuple
from enum import Enum


class SignalType(str, Enum):
    """Enumeration of signal types."""

    ANALOG = "Analog"
    DIGITAL = "Digital"
    DISCRETE = "Discrete"
    SERIAL = "Serial"


class SignalDirection(str, Enum):
    """Enumeration of signal directions."""

    INPUT = "Input"
    OUTPUT = "Output"
    BIDIRECTIONAL = "Bidirectional"


class FunctionalBlock(BaseModel):
    """
    Represents a functional block in the system diagram.

    Attributes:
        block_id (str): Unique identifier for the block.
        name (str): Name of the functional block.
        description (str): Brief description of the block's function.
        inputs (List[str]): List of input signal names.
        outputs (List[str]): List of output signal names.
    """

    block_id: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    inputs: List[str] = Field(default_factory=list)
    outputs: List[str] = Field(default_factory=list)


class DataSignal(BaseModel):
    """
    Represents a data signal in the system.

    Attributes:
        name (str): Name of the signal.
        type (SignalType): Type of the signal.
        direction (SignalDirection): Direction of the signal.
        source (str): Source of the signal (system or component ID).
        destination (str): Destination of the signal (system or component ID).
        description (str): Brief description of the signal.
    """

    name: str = Field(..., min_length=1, max_length=100)
    type: SignalType
    direction: SignalDirection
    source: str = Field(..., min_length=1, max_length=50)
    destination: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1, max_length=500)


class PhysicalCharacteristics(BaseModel):
    """
    Physical characteristics of the system.

    Attributes:
        weight (float): Weight in kilograms.
        dimensions (Dict[str, float]): Dimensions in meters (length, width, height).
        volume (float): Volume in cubic meters.
        center_of_gravity (Dict[str, float]): Center of gravity coordinates (x, y, z) in meters.
    """

    weight: float = Field(..., gt=0)
    dimensions: Dict[str, float] = Field(..., min_items=3, max_items=3)
    volume: float = Field(..., gt=0)
    center_of_gravity: Dict[str, float] = Field(..., min_items=3, max_items=3)

    @field_validator("dimensions")
    @classmethod
    def validate_dimensions(cls, v: Dict[str, float]) -> Dict[str, float]:
        """Validate that dimensions include length, width, and height."""
        if set(v.keys()) != {"length", "width", "height"}:
            raise ValueError("Dimensions must include 'length', 'width', and 'height'")
        return v

    @field_validator("center_of_gravity")
    @classmethod
    def validate_cog(cls, v: Dict[str, float]) -> Dict[str, float]:
        """Validate that center of gravity includes x, y, and z coordinates."""
        if set(v.keys()) != {"x", "y", "z"}:
            raise ValueError("Center of gravity must include 'x', 'y', and 'z' coordinates")
        return v


class FluidFlowCharacteristics(BaseModel):
    """
    Represents the flow characteristics of a working fluid in the system.

    Attributes:
        fluid_type (str): Type of fluid (e.g., "Hydraulic Oil", "Fuel", "Coolant").
        flow_rate (float): Nominal flow rate in liters per minute.
        max_pressure (float): Maximum operating pressure in pascals.
        min_pressure (float): Minimum operating pressure in pascals.
        temperature_range (Tuple[float, float]): Operating temperature range in Celsius (min, max).
        viscosity (float): Kinematic viscosity in centistokes at operating temperature.
        density (float): Fluid density in kg/m³ at operating temperature.
    """

    fluid_type: str = Field(..., min_length=1, max_length=50)
    flow_rate: float = Field(..., gt=0)
    max_pressure: float = Field(..., gt=0)
    min_pressure: float = Field(..., ge=0)
    temperature_range: Tuple[float, float] = Field(..., min_items=2, max_items=2)
    viscosity: float = Field(..., gt=0)
    density: float = Field(..., gt=0)

    @field_validator("temperature_range")
    @classmethod
    def validate_temperature_range(cls, v: Tuple[float, float]) -> Tuple[float, float]:
        """Validate that the minimum temperature is less than the maximum temperature."""
        if v[0] >= v[1]:
            raise ValueError("Minimum temperature must be less than maximum temperature")
        return v


class CoolingRequirements(BaseModel):
    """
    Cooling requirements for the system.

    Attributes:
        method (str): Cooling method (e.g., "Air", "Liquid", "Conduction").
        heat_dissipation (float): Heat dissipation in watts.
        max_operating_temperature (float): Maximum operating temperature in Celsius.
    """

    method: str = Field(..., min_length=1, max_length=50)
    heat_dissipation: float = Field(..., ge=0)
    max_operating_temperature: float


class PowerRequirements(BaseModel):
    """
    Power requirements for the system.

    Attributes:
        voltage (float): Required voltage in volts.
        current (float): Required current in amperes.
        frequency (Optional[float]): Required frequency in Hz, if applicable.
        power_type (str): Type of power (e.g., "AC", "DC").
        peak_power (float): Peak power consumption in watts.
        average_power (float): Average power consumption in watts.
    """

    voltage: float = Field(..., gt=0)
    current: float = Field(..., gt=0)
    frequency: Optional[float] = Field(None, gt=0)
    power_type: str = Field(..., min_length=1, max_length=20)
    peak_power: float = Field(..., gt=0)
    average_power: float = Field(..., gt=0)


class SystemAttributes(BaseModel):
    """
    Attributes specific to an aircraft system.

    Attributes:
        functional_blocks (List[FunctionalBlock]): List of functional blocks in the system.
        data_signals (List[DataSignal]): List of data signals in the system.
        physical_characteristics (PhysicalCharacteristics): Physical characteristics of the system.
        cooling_requirements (CoolingRequirements): Cooling requirements for the system.
        power_requirements (PowerRequirements): Power requirements for the system.
        fluid_flow (Optional[FluidFlowCharacteristics]): Fluid flow characteristics, if applicable.
    """

    functional_blocks: List[FunctionalBlock]
    data_signals: List[DataSignal]
    physical_characteristics: PhysicalCharacteristics
    cooling_requirements: CoolingRequirements
    power_requirements: PowerRequirements
    fluid_flow: Optional[FluidFlowCharacteristics] = None


class System(BaseModel):
    """
    Represents an aircraft system.

    Attributes:
        wbs_id (str): Work Breakdown Structure ID.
        mil_std_881f_reference (str): Reference to MIL-STD-881F.
        name (str): Name of the system.
        type (Literal["System"]): Type of the item (always "System" for this class).
        attributes (SystemAttributes): Specific attributes of the system.
        components (List[str]): List of component WBS IDs that make up this system.
    """

    wbs_id: str = Field(..., min_length=1, max_length=20)
    mil_std_881f_reference: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=1, max_length=100)
    type: Literal["System"] = "System"
    attributes: SystemAttributes
    components: List[str] = Field(..., min_items=1)

    @field_validator("type")
    @classmethod
    def type_must_be_system(cls, v: str) -> str:
        """Validate that the type is always 'System'."""
        if v != "System":
            raise ValueError("Type must be 'System'")
        return v
