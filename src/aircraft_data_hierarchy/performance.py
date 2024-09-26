from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, Field, field_validator, ConfigDict
from .common_base_model import CommonBaseModel, Metadata
import uuid

class DataExchange(CommonBaseModel):
    """
    Represents the data exchange information in a model.

    Attributes:
        model_identifier (Optional[str]): The identifier of the model.
        inputs (Optional[List[Any]]): The list of input variables.
        outputs (Optional[List[Any]]): The list of output variables.
    """
    model_identifier: Optional[str] = Field(None, description="The identifier of the model.")
    inputs: Optional[List[Any]] = Field(default_factory=list, description="The list of input variables.")
    outputs: Optional[List[Any]] = Field(default_factory=list, description="The list of output variables.")

    model_config = ConfigDict(protected_namespaces=(), arbitrary_types_allowed=True)

class ModelDescription(CommonBaseModel):
    """
    Represents the model description.

    Attributes:
        specification_version (Optional[str]): The specification version.
        model_name (Optional[str]): The name of the model.
        guid (Optional[str]): The globally unique identifier of the model.
        generation_tool (Optional[str]): The tool used to generate the model.
        generation_date_and_time (Optional[datetime]): The date and time when the model was generated.
        data_exchange (Optional[DataExchange]): The data exchange information.
        license (Optional[str]): The license of the model.
        copyright (Optional[str]): The copyright information.
        author (Optional[str]): The author of the model.
        version (Optional[str]): The version of the model.
        description (Optional[str]): A description of the model.
    """
    specification_version: Optional[str] = Field(None, description="The specification version.")
    model_name: Optional[str] = Field(None, description="The name of the model.")
    guid: Optional[str] = Field(None, description="The globally unique identifier of the model.")
    generation_tool: Optional[str] = Field(None, description="The tool used to generate the model.")
    generation_date_and_time: Optional[datetime] = Field(None, description="The date and time when the model was generated.")
    data_exchange: Optional[DataExchange] = Field(None, description="The data exchange information.")
    license: Optional[str] = Field(None, description="The license of the model.")
    copyright: Optional[str] = Field(None, description="The copyright information.")
    author: Optional[str] = Field(None, description="The author of the model.")
    version: Optional[str] = Field(None, description="The version of the model.")
    description: Optional[str] = Field(None, description="A description of the model.")

    model_config = ConfigDict(protected_namespaces=(), arbitrary_types_allowed=True)

    @field_validator('specification_version')
    def validate_specification_version(cls, v):
        if v and v != '2.0':
            raise ValueError('Invalid specification version. Must be 2.0')
        return v

    @field_validator('guid')
    def validate_guid(cls, v):
        if v:
            try:
                uuid_obj = uuid.UUID(v, version=4)
                return str(uuid_obj)
            except ValueError:
                raise ValueError('Invalid GUID format. Must be a valid UUID version 4')
        return v

class Discipline(CommonBaseModel):
    """
    Represents a specific discipline within engineering or scientific fields, organizing associated tools, models, and methodologies.

    This class facilitates structured access to and management of discipline-specific resources, enhancing the organization and efficiency of engineering and scientific projects.

    Attributes:
        name (Optional[str]): The name of the discipline, providing a clear identifier for categorization and reference.
        description (Optional[str]): A brief description of the discipline and its scope.
        tools (Optional[List[ModelDescription]]): A list of tools and models associated with the discipline, detailing the available resources for conducting analyses or simulations.
        metadata (Optional[Metadata]): Additional metadata providing further context or details about the discipline and its associated resources.
    """
    name: Optional[str] = Field(None, description="The name of the discipline.")
    description: Optional[str] = Field(None, description="A brief description of the discipline and its scope.")
    tools: Optional[List[ModelDescription]] = Field(default_factory=list, description="A list of tools and models associated with the discipline.")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata for the discipline.")

    @field_validator("name", mode="before")
    def validate_name(cls, value: str) -> str:
        """
        Validate the 'name' field to ensure it is not empty and contains only alphanumeric characters, underscores, and spaces.

        Args:
            value: The name of the discipline being validated.

        Returns:
            The validated name.

        Raises:
            ValueError: If the name is empty, contains invalid characters, or is not a string.
        """
        if value:
            if not isinstance(value, str):
                raise ValueError("Discipline name must be a string.")
            if not value.strip():
                raise ValueError("Discipline name cannot be empty.")
            if not all(c.isalnum() or c.isspace() or c == "_" for c in value):
                raise ValueError("Discipline name can only contain alphanumeric characters, underscores, and spaces.")
        return value

    def add_tool(self, tool: ModelDescription) -> None:
        """
        Add a new tool or model to the discipline, expanding the set of resources available for analysis and design.

        Args:
            tool: The tool or model to be added.
        """
        self.tools.append(tool)
