from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict

class NodeNotFoundError(Exception):
    """Exception raised when a node is not found in the ADH."""
    pass

class PathAlreadyExistsError(Exception):
    """Exception raised when a path already exists in the ADH."""
    pass

class CommonBaseModel(BaseModel):
    """
    A base model providing common validation logic for all derived models.

    Attributes:
        adh_data (Optional[Dict[str, Any]]): Dictionary for storing additional data.
        adh_root (Optional[Dict[str, Any]]): Dictionary representing the root of the ADH (Application Data Hierarchy).
        aliases (Optional[Dict[str, str]]): Dictionary for storing alias to path mappings.
    """

    adh_data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    adh_root: Optional[Dict[str, Any]] = Field(default_factory=dict)
    aliases: Optional[Dict[str, str]] = Field(default_factory=dict)

    model_config = ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        protected_namespaces=(),  # Allow the use of 'model_' prefix
    )

    @field_validator("*")
    @classmethod
    def strip_strings(cls, value: Any, info: Any) -> Any:
        """
        Strip leading and trailing whitespace from string fields before further validation.

        Args:
            value (Any): The value to be validated.
            info (Any): The field information.

        Returns:
            Any: The validated and possibly modified value.

        Raises:
            ValueError: If the field value is an empty string after trimming.
        """
        if isinstance(value, str):
            stripped_value = value.strip()
            if not stripped_value:
                raise ValueError(f"Field '{info.field_name}' cannot be empty after trimming.")
            return stripped_value
        return value

    def create_node(self, path: str, data: Dict[str, Any]) -> None:
        """
        Create a new node in the ADH at the specified path with the provided data.

        Args:
            path (str): The path where the new node should be created in the ADH.
            data (Dict[str, Any]): A dictionary containing the data to be stored in the new node.

        Raises:
            PathAlreadyExistsError: If the specified path already exists in the ADH.
            TypeError: If the provided data is not a valid dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")

        if self.get_node(path) is not None:
            raise PathAlreadyExistsError(f"A node already exists at the specified path: {path}")

        path_components = path.split(".")
        current_node = self.adh_root

        for component in path_components[:-1]:
            if component not in current_node:
                current_node[component] = {}
            current_node = current_node[component]

        current_node[path_components[-1]] = data

    def get_node(self, path: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a node from the ADH at the specified path.

        Args:
            path (str): The path of the node to retrieve from the ADH.

        Returns:
            Optional[Dict[str, Any]]: The node data as a dictionary if found, or None if the node doesn't exist.
        """
        path_components = path.split(".")
        current_node = self.adh_root

        for component in path_components:
            if component not in current_node:
                return None
            current_node = current_node[component]

        return current_node

    def search_nodes(self, filter_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search for nodes in the ADH that match the provided filter criteria.

        Args:
            filter_criteria (Dict[str, Any]): A dictionary specifying the filter criteria for the search.

        Returns:
            List[Dict[str, Any]]: A list of nodes (as dictionaries) that match the filter criteria.
        """
        def match_node(node: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
            return all(node.get(key) == value for key, value in criteria.items())

        def search_recursive(current_node: Dict[str, Any], criteria: Dict[str, Any], path: str, results: List[Dict[str, Any]]) -> None:
            if match_node(current_node, criteria):
                result = current_node.copy()
                result["_path"] = path
                results.append(result)
            for key, value in current_node.items():
                if isinstance(value, dict):
                    search_recursive(value, criteria, f"{path}.{key}", results)

        results: List[Dict[str, Any]] = []
        search_recursive(self.adh_root, filter_criteria, "", results)
        return results

    def update_node(self, path: str, data: Dict[str, Any]) -> None:
        """
        Update a node in the ADH at the specified path with the provided data.

        Args:
            path (str): The path of the node to update in the ADH.
            data (Dict[str, Any]): A dictionary containing the updated data for the node.

        Raises:
            NodeNotFoundError: If the specified path doesn't exist in the ADH.
            TypeError: If the provided data is not a valid dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError("The provided data must be a dictionary.")

        path_components = path.split(".")
        current_node = self.adh_root

        for component in path_components[:-1]:
            if component not in current_node:
                raise NodeNotFoundError(f"The specified path doesn't exist in the ADH: {path}")
            current_node = current_node[component]

        if path_components[-1] not in current_node:
            raise NodeNotFoundError(f"The specified path doesn't exist in the ADH: {path}")

        current_node[path_components[-1]] = data

    def move_node(self, source_path: str, target_path: str) -> None:
        """
        Move a node from one path to another in the ADH.

        Args:
            source_path (str): The path of the node to be moved.
            target_path (str): The path where the node should be moved to.

        Raises:
            NodeNotFoundError: If the source path doesn't exist.
            PathAlreadyExistsError: If the target path already exists in the ADH.
        """
        source_node = self.get_node(source_path)
        if source_node is None:
            raise NodeNotFoundError(f"The source path doesn't exist in the ADH: {source_path}")
        if self.get_node(target_path) is not None:
            raise PathAlreadyExistsError(f"The target path already exists in the ADH: {target_path}")

        self.create_node(target_path, source_node)
        self.delete_node(source_path)

    def delete_node(self, path: str) -> None:
        """
        Delete a node from the ADH at the specified path.

        Args:
            path (str): The path of the node to delete from the ADH.

        Raises:
            NodeNotFoundError: If the specified path doesn't exist in the ADH.
        """
        path_components = path.split(".")
        current_node = self.adh_root

        for component in path_components[:-1]:
            if component not in current_node:
                raise NodeNotFoundError(f"The specified path doesn't exist in the ADH: {path}")
            current_node = current_node[component]

        if path_components[-1] not in current_node:
            raise NodeNotFoundError(f"The specified path doesn't exist in the ADH: {path}")

        del current_node[path_components[-1]]

    def merge_nodes(self, source_path: str, target_path: str) -> None:
        """
        Merge the data of a source node into a target node in the ADH.

        Args:
            source_path (str): The path of the source node to merge from.
            target_path (str): The path of the target node to merge into.

        Raises:
            NodeNotFoundError: If either the source or target path doesn't exist in the ADH.
        """
        source_node = self.get_node(source_path)
        target_node = self.get_node(target_path)

        if source_node is None:
            raise NodeNotFoundError(f"The source path doesn't exist in the ADH: {source_path}")
        if target_node is None:
            raise NodeNotFoundError(f"The target path doesn't exist in the ADH: {target_path}")

        def merge_dicts(target, source):
            for key, value in source.items():
                if isinstance(value, dict):
                    target[key] = merge_dicts(target.get(key, {}), value)
                else:
                    target[key] = value
            return target

        merge_dicts(target_node, source_node)

    def copy_node(self, source_path: str, target_path: str) -> None:
        """
        Copy a node from a source path to a target path in the ADH.

        Args:
            source_path (str): The path of the node to be copied.
            target_path (str): The path where the node should be copied to.

        Raises:
            NodeNotFoundError: If the source path doesn't exist.
            PathAlreadyExistsError: If the target path already exists in the ADH.
        """
        source_node = self.get_node(source_path)
        if source_node is None:
            raise NodeNotFoundError(f"The source path doesn't exist in the ADH: {source_path}")
        if self.get_node(target_path) is not None:
            raise PathAlreadyExistsError(f"The target path already exists in the ADH: {target_path}")

        def deep_copy(node):
            if isinstance(node, dict):
                return {key: deep_copy(value) for key, value in node.items()}
            return node

        copied_node = deep_copy(source_node)
        self.create_node(target_path, copied_node)

    def link_nodes(self, source_path: str, target_path: str) -> None:
        """
        Create a link between a source node and a target node in the ADH.

        Args:
            source_path (str): The path of the source node to link from.
            target_path (str): The path of the target node to link to.

        Raises:
            NodeNotFoundError: If either the source or target path doesn't exist in the ADH.
        """
        source_node = self.get_node(source_path)
        target_node = self.get_node(target_path)

        if source_node is None:
            raise NodeNotFoundError(f"The source path doesn't exist in the ADH: {source_path}")
        if target_node is None:
            raise NodeNotFoundError(f"The target path doesn't exist in the ADH: {target_path}")

        self.aliases[source_path] = target_path

    def unlink_nodes(self, source_path: str) -> None:
        """
        Remove the link between a source node and its target node in the ADH.

        Args:
            source_path (str): The path of the source node to unlink.

        Raises:
            NodeNotFoundError: If the specified path is not linked to any other node.
        """
        if source_path not in self.aliases:
            raise NodeNotFoundError(f"The specified path is not linked to any other node: {source_path}")

        del self.aliases[source_path]


class Metadata(CommonBaseModel):
    """
    A metadata model for storing and managing key-value pairs.

    Attributes:
        key (str): The key of the metadata entry.
        value (Any): The value associated with the key.
    """

    key: str
    value: Any

    class Config:
        """Pydantic configuration for the Metadata model."""
        validate_assignment = True
        arbitrary_types_allowed = True
        extra = "forbid"
        str_min_length = 1
        str_max_length = 255
        str_strip_whitespace = True

    @field_validator('key')
    def key_must_be_non_empty(cls, key: str) -> str:
        """
        Ensure the key is non-empty and within specified length limits.

        Args:
            key (str): The key to validate.

        Returns:
            str: The validated key.

        Raises:
            ValueError: If the key is empty or exceeds the specified length limits.
        """
        if not key.strip():
            raise ValueError("Key must be non-empty.")
        if not (1 <= len(key.strip()) <= 255):
            raise ValueError("Key length must be between 1 and 255 characters.")
        return key.strip()
