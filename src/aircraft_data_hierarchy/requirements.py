from enum import Enum
from math import sqrt
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, field_validator
from .common_base_model import CommonBaseModel, Metadata


class Requirement(CommonBaseModel):
    """
    Defines a single requirement for engineering or scientific projects, encapsulating
    attributes for specification, tracking, and validation.

    Attributes:
        name (str): A unique identifier for the requirement.
        description (str): A detailed description of what the requirement entails.
        category (Optional[str]): The classification of the requirement (e.g., performance, safety).
        priority (str): The priority level of the requirement (e.g., high, medium, low).
        verification_method (str): The method to be used for verifying the requirement (e.g., test, analysis, inspection).
        status (str): The current status of the requirement (e.g., open, closed, in progress).
        source (Optional[str]): The origin or source of the requirement (e.g., customer, internal, regulation).
        target_component (Optional[str]): The component or system to which the requirement applies.
        acceptance_criteria (str): The criteria that must be met for the requirement to be considered satisfied.
        risk (Optional[str]): A description of the potential risks associated with the requirement.
        verification_evidence (Optional[str]): Documentation or evidence proving the requirement has been verified.
        metadata (Optional[Metadata]): Additional metadata providing context or details about the requirement.

    Raises:
        ValueError: If essential string attributes are empty, ensuring all requirements are descriptive and actionable.
    """

    name: str = Field(..., description="A unique name identifying the requirement.")
    description: str = Field(..., description="A detailed description of the requirement.")
    category: Optional[str] = Field(None, description="The category of the requirement.")
    priority: str = Field(..., description="The priority level of the requirement.")
    verification_method: str = Field(..., description="The method used to verify the requirement.")
    status: str = Field(..., description="The current status of the requirement.")
    source: Optional[str] = Field(None, description="The source or origin of the requirement.")
    target_component: Optional[str] = Field(None, description="The component or system to which the requirement applies.")
    acceptance_criteria: str = Field(..., description="The criteria for the requirement to be considered satisfied.")
    risk: Optional[str] = Field(None, description="Potential risks associated with the requirement.")
    verification_evidence: Optional[str] = Field(None, description="Evidence demonstrating the verification of the requirement.")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata about the requirement.")

    @field_validator('name', 'description', 'priority', 'verification_method', 'status', 'acceptance_criteria')
    def validate_non_empty(cls, value: str) -> str:
        """
        Validates that critical string fields are not empty or just whitespace,
        ensuring requirements are clear and actionable.

        Args:
            value (str): The value of the field being validated.

        Returns:
            The validated string value.

        Raises:
            ValueError: If the input value is empty or consists only of whitespace.
        """
        if not value.strip():
            raise ValueError(f"The field cannot be empty or just whitespace.")
        return value


class Requirements(CommonBaseModel):
    """Aggregates and categorizes multiple lists of requirements within a project, facilitating structured specification, organization, 
    and tracking.

    This class is vital for managing complex sets of requirements in engineering and scientific projects, allowing for clear delineation 
    and efficient access to different types of requirements such as safety, performance, design, and more.

    Attributes:
        name (str): A unique name identifying the set of requirements.
        description (str): A brief description of the requirements set, providing context or purpose.
        requirements (Dict[str, List[Requirement]]): A dictionary mapping requirement categories to lists of Requirement objects,
                                                     providing flexibility for managing different requirement types.
        metadata (Metadata): Additional metadata providing further context or details about the requirements.
    """

    name: str = Field(..., description="A unique name identifying the set of requirements.")
    description: str = Field(..., description="A brief description of the requirements set, providing context or purpose.")
    requirements: Dict[str, List[Requirement]] = Field(
        default_factory=dict,
        description="Dictionary mapping requirement categories to requirement lists.",
    )
    metadata: Optional[Metadata] = Field(
        None,
        description="Additional metadata for the requirements.",
    )

    @field_validator("name", "description")
    def validate_non_empty(cls, value: str, field: Field) -> str:
        """Validate that the name and description fields are not empty.
    
        Args:
            value: The value of the field being validated.
            field: The metadata of the field being validated.
    
        Raises:
            ValueError: If the field value is empty or just whitespace.
    
        Returns:
            The validated value.
        """
        if not value.strip():
            raise ValueError(
                f"The '{field.name}' field cannot be empty or just whitespace."
            )
        return value
    
    def add_requirement(self, requirement: Requirement, category: str) -> None:
        """Dynamically add a new requirement to the specified category, enhancing the project's requirements documentation and tracking.
    
        Args:
            requirement: The requirement to be added.
            category: The category under which to add the requirement.
    
        Raises:
            ValueError: If the specified category does not exist, it will be created.
        """
        if category not in self.requirements:
            self.requirements[category] = []
        self.requirements[category].append(requirement)
    
    def remove_requirement(self, requirement_name: str, category: str) -> None:
        """Remove a requirement from the specified category based on its name.
    
        Args:
            requirement_name: The name of the requirement to remove.
            category: The category from which to remove the requirement.
    
        Raises:
            ValueError: If the specified category does not exist or if the requirement is not found within the category.
        """
        if category not in self.requirements or not any(
            req.name == requirement_name for req in self.requirements[category]
        ):
            raise ValueError(
                f"Requirement '{requirement_name}' not found in category '{category}'."
            )
        self.requirements[category] = [
            req for req in self.requirements[category] if req.name != requirement_name
        ]
    
    def get_requirements_by_category(self, category: str) -> List[Requirement]:
        """Retrieve a list of requirements belonging to the specified category.
    
        Args:
            category: The category from which to retrieve the requirements.
    
        Returns:
            The list of requirements in the specified category.
    
        Raises:
            ValueError: If the specified category does not exist in the requirements.
        """
        if category not in self.requirements:
            raise ValueError(f"Category '{category}' does not exist.")
        return self.requirements[category]
