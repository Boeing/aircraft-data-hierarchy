from __future__ import annotations
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, field_validator
from ..common_base_model import CommonBaseModel, Metadata
from ..requirements import Requirement
from ..performance import Discipline
from ..behavior import Behavior

class Equipment(CommonBaseModel):
    """
    Represents miscellaneous equipment onboard an aircraft required for it's operational use.

    Attributes:
        name (Optional[str]): The name of the equipment, acting as a unique identifier.
        description (Optional[str]): A brief description of the equipments's purpose and functionality.
        geometry (Optional[Dict[str, Any]]): Geometric information of the equipment, if applicable.
        parameters (Optional[Dict[str, Any]]): Operational or physical parameters associated with the equipment.
        metadata (Optional[Metadata]): Additional metadata providing context or details about the equipment.
        subequipment (Optional[List[Equipment]]): A list of sub-components, if any, within this equipment.
        requirements (Optional[List[Requirement]]): Specific requirements associated with this equipment.
        performance (Optional[List[Discipline]]): List of disciplines analyzing the equipment.
        behavior (Optional[List[Behavior]]): Specific behaviors for the equipment.

    Raises:
        ValueError: If any string field is empty, ensuring all equipment has meaningful identifiers and descriptions.
    """

    name: Optional[str] = Field(None, description="The name of the equipment.")
    description: Optional[str] = Field(None, description="A brief description of the equipment.")
    geometry: Optional[Dict[str, Any]] = Field(default=None, description="Geometry of the equipment.")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="Parameters of the equipment.")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata for the equipment.")
    subequipment: Optional[List[Equipment]] = Field(default=None, description="Sub-equipment within this equipment.")
    requirements: Optional[List[Requirement]] = Field(default=None, description="Specific requirements for the equipment.")
    performance: Optional[List[Discipline]] = Field(default=None, description="List of disciplines analyzing the equipment.")
    behavior: Optional[List[Behavior]] = Field(default=None, description="Specific behaviors for the equipment.")

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

    class Config:
        """Pydantic model configuration."""
        arbitrary_types_allowed = True
        from_attributes = True

# Ensure all models are fully defined
Equipment.model_rebuild()
