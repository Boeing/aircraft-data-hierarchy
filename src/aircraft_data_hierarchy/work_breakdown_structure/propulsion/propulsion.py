from __future__ import annotations
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel, ConfigDict, Field, field_validator
from ...common_base_model import CommonBaseModel, Metadata
from ...requirements import Requirement
from .propulsion_cycle import PropulsionCycle

class Propulsion(CommonBaseModel):
    """
    Represents the propulsion system within an air vehicle system, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the propulsion system, acting as a unique identifier.
        description (Optional[str]): A brief description of the propulsion system purpose and functionality.
        geometry (Optional[Dict[str, Any]]): Geometric information of the component, if applicable.
        parameters (Optional[Dict[str, Any]]): Cycle or physical parameters associated with the propulsion system.
        metadata (Optional[Metadata]): Additional metadata providing context or details about the propulsion system.
        subcomponents (Optional[List[Propulsion]]): A list of sub-components, if any, within the propulsion system.
        requirements (Optional[List[Requirement]]): Specific requirements associated with the propulsion system.
        performance (Optional[List[Discipline]]): List of disciplines analyzing the propulsion system.
        behavior (Optional[List[Behavior]]): Specific behaviors for the propulsion system.

    Raises:
        ValueError: If any string field is empty, ensuring all components have meaningful identifiers and descriptions.
    """

    name: Optional[str] = Field(None, description="The name of the propulsion system.")
    description: Optional[str] = Field(None, description="A brief description of the propulsion system.")
    geometry: Optional[Dict[str, Any]] = Field(default=None, description="Geometry of the propulsion system.")
    # TODO: Get MultiPointCycle imported behaviorLib Demo
    # cycle: Union[PropulsionCycle, MultiPointCycle] = Field(default=None, description="Cycle of the propulsion system.")
    cycle: PropulsionCycle = Field(default=None, description="Cycle of the propulsion system.")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="Parameters of the propulsion system.")
    metadata: Optional[Metadata] = Field(default=None, description="Additional metadata for the propulsion system.")
    subcomponents: Optional[List[Propulsion]] = Field(
        default=None, description="Sub-components within the propulsion system."
    )
    requirements: Optional[List[Requirement]] = Field(
        default=None, description="Specific requirements for the propulsion system."
    )
    # TODO: Get MultiPointCycle imported behaviorLib and performanceLib Demo
    # performance: Optional[PropulsionCyclePerformance] = Field(default=None, description="Propulsion performance data.")
    # behavior: Optional[PropulsionCycleBehavior] = Field(default=None, description="SpPropulsion behavior data.")

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_non_empty_string(cls, value: Optional[str]) -> Optional[str]:
        """
        Validates that the name and description fields are not empty or whitespace only.

        Args:
            value (Optional[str]): The value to validate.

        Returns:
            Optional[str]: The validated string value.

        Raises:
            ValueError: If the input value is empty or consists only of whitespace.
        """
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty or whitespace only.")
        return value
    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)


# Ensure all models are fully defined
Propulsion.model_rebuild()
