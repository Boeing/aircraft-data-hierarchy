from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from math import sqrt
from math import isfinite as math_isfinite
from typing import Dict, Any, List, Optional, Tuple
from pydantic import BaseModel, Field, model_validator, field_validator, constr, AnyUrl, EmailStr
from ...common_base_model import CommonBaseModel, Metadata

class String(CommonBaseModel):
    """Represents a string data type with enhanced attributes for engineering applications.

    Attributes:
        value (str): The actual string value. It must have at least 1 character.
        default (Optional[str]): A default value for the variable, if any. Defaults to None.
        metadata (Metadata): Additional metadata providing further context or details about the variable.
                             Defaults to a new instance of Metadata.

    Raises:
        ValidationError: If the input value does not meet the validation criteria.
    """

    value: str = Field(..., description="The actual string value.", min_length=1)
    default: Optional[str] = Field(
        None, description="A default value for the variable, if any."
    )
    metadata: Optional[Metadata] = Field(
        None,
        description="Additional metadata providing further context or details about the variable.",
    )

    @field_validator("value", mode="before")
    def validate_value_not_empty(cls, value: str) -> str:
        """Validate that the string value is not empty or just whitespace.

        Args:
            value: The string value to validate.

        Returns:
            The validated string value.

        Raises:
            ValueError: If the value is empty or just whitespace.
        """
        if not value.strip():
            raise ValueError("String value cannot be empty or just whitespace.")
        return value


class Boolean(CommonBaseModel):
    """Represents a boolean data type with enhanced attributes for engineering applications.

    Attributes:
        value (bool): The actual boolean value.
        units (str): Units of the variable, typically 'unitless' for boolean types.
        description (Optional[str]): A brief description of the variable.
        default (Optional[bool]): Default boolean value of the variable, if any.
        metadata (Metadata): Additional metadata for the variable.

    Raises:
        ValidationError: If the input value does not meet the validation criteria.
    """

    value: bool = Field(..., description="The actual boolean value.")
    units: str = Field(
        default="unitless",
        description="Units of the variable, typically 'unitless' for boolean types.",
    )
    description: Optional[str] = Field(
        None, description="A brief description of the variable."
    )
    default: Optional[bool] = Field(
        None, description="Default boolean value of the variable, if any."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the variable."
    )

    @field_validator("default", mode="before")
    def validate_default(cls, value: Optional[bool], values: dict) -> Optional[bool]:
        """Validate and convert the default value to a boolean if it's provided as a string.

        Args:
            value: The default value being validated.
            values: The dictionary containing the field values.

        Returns:
            The validated default value.

        Raises:
            ValueError: If the default value is a string that cannot be converted to a boolean.
        """
        if isinstance(value, str):
            lower_value = value.lower()
            if lower_value in {"true", "1", "t", "y", "yes"}:
                return True
            elif lower_value in {"false", "0", "f", "n", "no"}:
                return False
            else:
                raise ValueError(f"Invalid string value for a boolean conversion: {value}")
        return value


class Float(CommonBaseModel):
    """Represents a floating-point number with enhanced attributes for engineering applications.

    Attributes:
        value (float): The actual floating-point value.
        units (str): Units of the variable, allowing for dimensional analysis.
        description (Optional[str]): A brief description of the variable.
        default (Optional[float]): Default floating-point value of the variable, if any.
        metadata (Metadata): Additional metadata for the variable.

    Raises:
        ValidationError: If the input value does not meet the validation criteria.
    """

    value: float = Field(..., description="The actual floating-point value.")
    units: str = Field(default="unitless", description="Units of the variable.")
    description: Optional[str] = Field(
        None, description="A brief description of the variable."
    )
    default: Optional[float] = Field(
        None, description="Default floating-point value of the variable, if any."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the variable."
    )

    @field_validator("default", mode="before")
    def validate_default(cls, value: Optional[float], values: dict) -> Optional[float]:
        """Validate and convert the default value to a float if it's provided as a string.

        Args:
            value: The default value being validated.
            values: The dictionary containing the field values.

        Returns:
            The validated default value.

        Raises:
            ValueError: If the default value is a string that cannot be converted to a float.
        """
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Invalid string value for a float conversion: {value}")
        return value


class Integer(CommonBaseModel):
    """Represents an integer data type with enhanced attributes for engineering applications.

    Attributes:
        value (int): The actual integer value.
        units (str): Units of the variable, allowing for dimensional analysis.
        description (Optional[str]): A brief description of the variable.
        default (Optional[int]): Default integer value of the variable, if any.
        metadata: Optional[Metadata]): Additional metadata for the variable.

    Raises:
        ValidationError: If the input value does not meet the validation criteria.
    """

    value: int = Field(..., description="The actual integer value.")
    units: str = Field(default="unitless", description="Units of the variable.")
    description: Optional[str] = Field(
        None, description="A brief description of the variable."
    )
    default: Optional[int] = Field(
        None, description="Default integer value of the variable, if any."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the variable."
    )

    @field_validator("default", mode="before")
    def validate_default(cls, value: Optional[int], values: dict) -> Optional[int]:
        """Validate and convert the default value to an integer if it's provided as a string.

        Args:
            value: The default value being validated.
            values: The dictionary containing the field values.

        Returns:
            The validated default value.

        Raises:
            ValueError: If the default value is a string that cannot be converted to an integer.
        """
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                raise ValueError(
                    f"Invalid string value for an integer conversion: {value}"
                )
        return value


class Point(BaseModel):
    """
    Represents a point in 3D space, defined by its x, y, and z coordinates.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        z (float): The z-coordinate of the point.

    Raises:
        ValueError: If any coordinate is not a finite number, ensuring points are well-defined in 3D space.
    """

    @property
    def coordinates(self) -> Tuple[float, float, float]:
        """Return the coordinates as a tuple (x, y, z)."""
        return self.x, self.y, self.z
        
    x: float = Field(..., description="The x-coordinate of the point.")
    y: float = Field(..., description="The y-coordinate of the point.")
    z: float = Field(..., description="The z-coordinate of the point.")

    @field_validator("x", "y", "z")
    @classmethod
    def validate_coordinate(cls, value: float) -> float:
        """Validate that the coordinate is a finite number, ensuring the point is well-defined.

        Args:
            value: The coordinate value to validate.

        Returns:
            The validated coordinate value.

        Raises:
            ValueError: If the coordinate is not a finite number.
        """
        if not math_isfinite(value):
            raise ValueError("Coordinate values must be finite.")
        return value

    def distance_to(self, other: "Point") -> float:
        """Calculate the Euclidean distance between this point and another point.

        Args:
            other: The other point to calculate the distance to.

        Returns:
            The Euclidean distance between the two points.
        """
        return sqrt(
            sum((a - b) ** 2 for a, b in zip(self.coordinates, other.coordinates))
        )

    def __hash__(self):
        """Return the hash value of the Point object."""
        return hash(self.coordinates)

class Polyline(CommonBaseModel):
    """Represents a polyline, a series of connected 3D points forming a continuous line or path.

    Useful in geometric modeling and spatial analysis, the Polyline class enables the representation
    of linear paths, edges, or trajectories in three-dimensional space, facilitating calculations and
    visualizations related to lines.

    Attributes:
        points (List[Point]): A series of 3D points defining the polyline.
        metadata (Metadata): Additional metadata for the polyline.
    """

    points: List[Point] = Field(
        ..., description="A series of 3D points defining the polyline."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the polyline."
    )

    @field_validator("points", mode="before")
    def validate_points(cls, value: List[Point]) -> List[Point]:
        """Validate the 'points' list to ensure it contains at least two points.

        Args:
            value: The list of points being validated.

        Returns:
            The validated list of points.

        Raises:
            ValueError: If the list contains fewer than two points.
        """
        if len(value) < 2:
            raise ValueError("A polyline must contain at least two points.")
        return value

    def add_point(self, point: Point) -> None:
        """Add a new point object to the end of the polyline, extending its path.

        Args:
            point: The point object to be appended to the polyline.
        """
        self.points.append(point)

    def length(self) -> float:
        """Calculate the total length of the polyline by summing the distances between consecutive points.

        Returns:
            The total length of the polyline.
        """
        total_length = 0.0
        for i in range(1, len(self.points)):
            total_length += self.points[i].distance_to(self.points[i - 1])
        return total_length

    def simplify(self, tolerance: float) -> Polyline:
        """Simplify the polyline by removing redundant points based on a specified tolerance.

        The simplification algorithm iteratively removes points that deviate from the line segment formed
        by their neighboring points by a distance less than the specified tolerance. This process continues
        until no more points can be removed without exceeding the tolerance.

        Args:
            tolerance: The maximum deviation allowed for a point to be considered redundant.

        Returns:
            A new simplified polyline with redundant points removed.
        """
        if len(self.points) < 3:
            return self

        simplified_points = [self.points[0]]  # Always keep the first point
        for i in range(1, len(self.points) - 1):
            prev_point = simplified_points[-1]
            point = self.points[i]
            next_point = self.points[i + 1]

            area = abs(
                (next_point.coordinates[0] - prev_point.coordinates[0])
                * (point.coordinates[1] - prev_point.coordinates[1])
                - (next_point.coordinates[1] - prev_point.coordinates[1])
                * (point.coordinates[0] - prev_point.coordinates[0])
            )
            height = area / prev_point.distance_to(next_point)

            if height > tolerance:
                simplified_points.append(point)

        simplified_points.append(self.points[-1])  # Always keep the last point
        return Polyline(points=simplified_points)


class Spline(BaseModel):
    """
    Represents a spline, which is a smooth curve constructed from a series of control points.

    Splines are essential in various applications such as computer graphics, geometric modeling, and trajectory planning.

    Attributes:
        points (List[Point]): The list of control points that define the spline. The spline passes through these points.
        degree (int): The degree of the spline curve. Common values are 2 (quadratic) and 3 (cubic).

    Raises:
        ValueError: If the number of points is less than the degree + 1, which is necessary for defining a valid spline.
    """

    points: List[Point] = Field(
        ...,
        description="Control points that define the spline.",
        min_items=2  # Ensuring there's at least two points to define a curve
    )
    degree: int = Field(
        default=3,
        gt=0,
        description="The degree of the spline curve. Commonly 2 (quadratic) or 3 (cubic)."
    )

    @field_validator("points", mode="before")
    def validate_points(cls, value: List[Point], values: dict) -> List[Point]:
        """Validate that the list of points is sufficient to define a spline of the specified degree.

        Args:
            value: The list of control points.
            values: A dictionary of field names to their validated values.

        Returns:
            The validated list of control points.

        Raises:
            ValueError: If the number of points is less than the required for the spline's degree.
        """
        degree = values.degree if hasattr(values, "degree") else 3  # Default to cubic if degree is not yet validated
        if len(value) < degree + 1:
            raise ValueError(
                f"At least {degree + 1} points are required to define a spline of degree {degree}."
            )
        return value

    @field_validator("degree", mode="before")
    def validate_degree(cls, value: int) -> int:
        """Validate that the degree of the spline is a positive integer.

        Args:
            value: The degree of the spline.

        Returns:
            The validated degree of the spline.

        Raises:
            ValueError: If the degree is not a positive integer.
        """
        if value <= 0:
            raise ValueError("The degree of the spline must be a positive integer.")
        return value


class Mesh(CommonBaseModel):
    """Represents a 3D mesh, a collection of polygons (typically triangles or quadrilaterals) used to model the surface of a 3D object.

    Meshes are fundamental in computer graphics, engineering simulations, and geometric modeling, allowing for the detailed
    representation of complex 3D shapes. This class facilitates the construction, manipulation, and analysis of mesh geometries,
    supporting applications in visualization, physical simulation, and more.

    Attributes:
        polylines (List[Polyline]): A collection of polylines defining the mesh.
        metadata (Metadata): Additional metadata for the mesh.
    """

    polylines: List[Polyline] = Field(
        ..., description="A collection of polylines defining the mesh."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the mesh."
    )

    @field_validator("polylines", mode="before")
    def validate_polylines(cls, value: List[Polyline]) -> List[Polyline]:
        """Validate the 'polylines' list to ensure it contains at least one polyline.

        Args:
            value: The list of polylines being validated.

        Returns:
            The validated list of polylines.

        Raises:
            ValueError: If the list is empty.
        """
        if not value:
            raise ValueError("A mesh must contain at least one polyline.")
        return value

    def add_polyline(self, polyline: Polyline) -> None:
        """Add a new polyline object to the mesh, expanding its geometry.

        Args:
            polyline: The new polyline to be added to the mesh.
        """
        self.polylines.append(polyline)

    def remove_polyline(self, index: int) -> None:
        """Remove a polyline from the mesh at the specified index.

        Args:
            index: The index of the polyline to be removed.

        Raises:
            IndexError: If the specified index is out of range.
        """
        if index < 0 or index >= len(self.polylines):
            raise IndexError("Invalid index for polyline removal.")
        self.polylines.pop(index)

    # TODO: Fix Issue with unexpected is_manifold() results
    #       in tests/test_aircraft_data_hierarchy/test_work_breakdown_structure/test_airframe/test_airframe_geometry.py::TestMesh::test_mesh_is_manifold
    # def is_manifold(self) -> bool:
    #     """Check if the mesh is manifold.

    #     A mesh is considered manifold if it satisfies the following conditions:
    #     - Each edge is shared by exactly two polygons.
    #     - The mesh has no boundary edges.
    #     - The mesh has no self-intersections.

    #     Returns:
    #         True if the mesh is manifold, False otherwise.
    #     """
    #     from collections import defaultdict

    #     edge_count = defaultdict(int)

    #     def add_edge(p1: Point, p2: Point):
    #         """Add an edge to the edge count dictionary.

    #         Args:
    #             p1: The first point of the edge.
    #             p2: The second point of the edge.
    #         """
    #         edge = tuple(sorted((p1, p2), key=lambda p: (p.x, p.y, p.z)))
    #         edge_count[edge] += 1

    #     for polyline in self.polylines:
    #         points = polyline.points
    #         for i in range(len(points)):
    #             add_edge(points[i], points[(i + 1) % len(points)])

    #     for count in edge_count.values():
    #         if count != 2:
    #             return False

    #     return True

    def calculate_volume(self) -> float:
        """Calculate the volume enclosed by the mesh.

        This method uses the tetrahedron decomposition algorithm to compute the volume
        enclosed by the mesh geometry.

        Returns:
            The calculated volume of the mesh.
        """
        def signed_tetrahedron_volume(a: Point, b: Point, c: Point, d: Point) -> float:
            """Calculate the signed volume of a tetrahedron given its four vertices.

            Args:
                a: The first vertex of the tetrahedron.
                b: The second vertex of the tetrahedron.
                c: The third vertex of the tetrahedron.
                d: The fourth vertex of the tetrahedron.

            Returns:
                The signed volume of the tetrahedron.
            """
            return (
                (a.x - d.x) * (b.y - d.y) * (c.z - d.z)
                + (a.y - d.y) * (b.z - d.z) * (c.x - d.x)
                + (a.z - d.z) * (b.x - d.x) * (c.y - d.y)
                - (a.z - d.z) * (b.y - d.y) * (c.x - d.x)
                - (a.y - d.y) * (b.x - d.x) * (c.z - d.z)
                - (a.x - d.x) * (b.z - d.z) * (c.y - d.y)
            ) / 6.0

        # Assuming the mesh is closed and the polylines form a valid surface
        # We will use the first point as the reference point for tetrahedron decomposition
        reference_point = self.polylines[0].points[0]
        total_volume = 0.0

        for polyline in self.polylines:
            points = polyline.points
            for i in range(1, len(points) - 1):
                total_volume += signed_tetrahedron_volume(
                    reference_point, points[0], points[i], points[i + 1]
                )

        return abs(total_volume)


class Loft(CommonBaseModel):
    """Represents a lofted surface, a smooth spatial surface generated by transitioning between multiple spline curves.

    In engineering and design, lofts are used to create complex shapes by smoothly connecting a series of cross-sectional
    profiles. This class enables the representation of lofted surfaces, facilitating their use in computational modeling,
    simulation, and visualization of aerodynamic shapes, product designs, and more.

    Attributes:
        splines (List[Spline]): A series of splines defining the shapes to interpolate for the loft.
        num_samples (int): The number of sample points to generate along each spline.
        metadata (Metadata): Additional metadata for the loft.
    """

    splines: List[Spline] = Field(
        ...,
        description="A series of splines defining the shapes to interpolate for the loft.",
    )
    num_samples: int = Field(
        100, description="The number of sample points to generate along each spline."
    )
    metadata: Optional[Metadata] = Field(
        None, description="Additional metadata for the loft."
    )

    @field_validator("splines", mode="before")
    def validate_splines(cls, value: List[Spline]) -> List[Spline]:
        """Validate the 'splines' list to ensure it contains at least two splines with the same degree.

        Args:
            value: The list of splines being validated.

        Returns:
            The validated list of splines.

        Raises:
            ValueError: If the list contains fewer than two splines or if the splines have different degrees.
        """
        if len(value) < 2:
            raise ValueError("A loft requires at least two splines.")

        degree = value[0].degree
        if any(spline.degree != degree for spline in value):
            raise ValueError("All splines in the loft must have the same degree.")

        return value

    @field_validator("num_samples", mode="before")
    def validate_num_samples(cls, value: int) -> int:
        """Validate the 'num_samples' field to ensure it is a positive integer.

        Args:
            value: The number of samples being validated.

        Returns:
            The validated number of samples.

        Raises:
            ValueError: If the number of samples is not a positive integer.
        """
        if value <= 0:
            raise ValueError("The number of samples must be a positive integer.")
        return value

    def add_spline(self, spline: Spline) -> None:
        """Add a new spline to the series of cross-sectional profiles, potentially altering the shape of the lofted surface.

        Args:
            spline: The new spline to be added to the series defining the loft.
        """
        self.splines.append(spline)

    def calculate_surface(self) -> List[List[float]]:
        """Calculate the lofted surface by interpolating between the splines.

        This method generates a series of intermediate curves by interpolating between the given splines,
        creating a smooth surface that transitions from one cross-sectional profile to another.

        Returns:
            A list of lists representing the lofted surface points, where each inner list represents a point
            on the surface with [x, y, z] coordinates.
        """
        def interpolate_points(p1: Point, p2: Point, t: float) -> Point:
            """Interpolate between two points.

            Args:
                p1: The first point.
                p2: The second point.
                t: The interpolation parameter (0 <= t <= 1).

            Returns:
                The interpolated point.
            """
            return Point(
                x=p1.x + t * (p2.x - p1.x),
                y=p1.y + t * (p2.y - p1.y),
                z=p1.z + t * (p2.z - p1.z)
            )

        def interpolate_splines(spline1: Spline, spline2: Spline, t: float) -> List[Point]:
            """Interpolate between two splines.

            Args:
                spline1: The first spline.
                spline2: The second spline.
                t: The interpolation parameter (0 <= t <= 1).

            Returns:
                A list of interpolated points.
            """
            return [
                interpolate_points(p1, p2, t)
                for p1, p2 in zip(spline1.points, spline2.points)
            ]

        surface_points = []

        for i in range(len(self.splines) - 1):
            spline1 = self.splines[i]
            spline2 = self.splines[i + 1]

            for j in range(self.num_samples):
                t = j / (self.num_samples - 1)
                interpolated_points = interpolate_splines(spline1, spline2, t)
                surface_points.extend([[p.x, p.y, p.z] for p in interpolated_points])

        return surface_points

class Airfoil(CommonBaseModel):
    """
    Represents an airfoil section, a fundamental component in aircraft design for wings and control surfaces.

    Attributes:
        spline (Optional[Spline]): A spline defining the contour of the airfoil section.

    Raises:
        ValueError: If the spline is not provided.
    """

    spline: Optional[Spline] = Field(
        None,
        description="A spline defining the contour of the airfoil section.",
    )

    @field_validator("spline",mode='before')
    def validate_spline(cls, value: Optional[Spline]) -> Spline:
        """
        Validates the spline defining the airfoil contour.

        Args:
            value: The spline object to validate.

        Returns:
            The validated spline object.

        Raises:
            ValueError: If the spline is not provided.
        """
        if value is None:
            raise ValueError("The spline defining the airfoil contour must be provided.")
        return value

# ToDo: ReferenceAxis is needed by airframe_geometry, propulsion_geometry, systems_parameters?, and equipment_?...
#       where should it go? AirVehicle level, with other Topology/Reference parameters? Its related to
#       parameters like moment arms between lifting surfaces...add 'aircraft_topology.py'?
class ReferenceAxis(CommonBaseModel):
    """
    Represents the reference axis of a body component, such as an aircraft fuselage or wing.

    Attributes:
        name (str): The name of the reference axis.
        points (List[Point]): A series of 3D points defining the reference axis.
        description (Optional[str]): A brief description of the reference axis.
        metadata (Metadata): Additional metadata for the reference axis.
        relative_to (Optional[str]): The name of another reference axis to which this axis is relative.
    """

    name: str = Field(..., description="The name of the reference axis.")
    points: List[Point] = Field(
        ..., description="A series of 3D points defining the reference axis."
    )
    description: Optional[str] = Field(
        None, description="A brief description of the reference axis."
    )
    metadata: Metadata = Field(
        default_factory=Metadata, description="Additional metadata for the reference axis."
    )
    relative_to: Optional[str] = Field(
        None, description="The name of another reference axis to which this axis is relative."
    )

    # Class-level dictionary to map names to ReferenceAxis instances
    _registry: Dict[str, ReferenceAxis] = {}

    @field_validator("points", mode="before")
    def validate_points(cls, value: List[Point]) -> List[Point]:
        """Validate the 'points' list to ensure it contains at least two points.

        Args:
            value: The list of points being validated.

        Returns:
            The validated list of points.

        Raises:
            ValueError: If the list contains fewer than two points.
        """
        if len(value) < 2:
            raise ValueError("A reference axis must contain at least two points.")
        return value

    @model_validator(mode="before")
    def validate_and_register(cls, values: dict) -> dict:
        """Ensure that the name is unique and register the instance.

        Args:
            values: The dictionary of field values.

        Returns:
            The validated dictionary of field values.

        Raises:
            ValueError: If the name is not unique.
        """
        name = values.get("name")
        if name in cls._registry:
            raise ValueError(f"A ReferenceAxis with the name '{name}' already exists.")
        return values

    @model_validator(mode="after")
    def resolve_relative_to(cls, values: dict) -> dict:
        """Resolve the 'relative_to' name to a ReferenceAxis instance.

        Args:
            values: The dictionary of field values.

        Returns:
            The validated dictionary of field values.

        Raises:
            ValueError: If the 'relative_to' name does not exist.
        """
        relative_to_name = values.get("relative_to")
        if relative_to_name:
            relative_to_axis = cls._registry.get(relative_to_name)
            if not relative_to_axis:
                raise ValueError(f"ReferenceAxis with name '{relative_to_name}' does not exist.")
            values["relative_to"] = relative_to_axis
        return values

    def __init__(self, **data: Any):
        super().__init__(**data)
        # Register the instance after initialization
        self._registry[self.name] = self

class LiftingSurface(CommonBaseModel):
    """
    Represents the geometric characteristics of a lifting surface, such as wings and tail surfaces of aircraft.

    Attributes:
        leading_edge_spline (Optional[Spline]): Spline defining the leading edge of the lifting surface.
        trailing_edge_spline (Optional[Spline]): Spline defining the trailing edge of the lifting surface.
        airfoil_sections (List[Airfoil]): List of Airfoil objects representing the airfoil shapes along the span.

    Raises:
        ValueError: If the list of airfoil sections is empty.
    """

    leading_edge_spline: Optional[Spline] = Field(
        None,
        description="Spline defining the leading edge of the lifting surface.",
    )
    trailing_edge_spline: Optional[Spline] = Field(
        None,
        description="Spline defining the trailing edge of the lifting surface.",
    )
    airfoil_sections: List[Airfoil] = Field(
        ...,
        description="List of Airfoil objects representing the airfoil shapes along the span.",
    )

    @field_validator("airfoil_sections", mode='before')
    def validate_airfoil_sections(
        cls, value: List[Airfoil]
    ) -> List[Airfoil]:
        """
        Ensures that at least one Airfoil object is provided.

        Args:
            value: The list of Airfoil objects to validate.

        Returns:
            The validated list of Airfoil objects.

        Raises:
            ValueError: If the list is empty.
        """
        if not value:
            raise ValueError(
                "At least one Airfoil must be provided for the lifting surface."
            )
        return value

class CrossSection(CommonBaseModel):
    """
    Represents a cross-section of a body component at a specific station along its length.

    Attributes:
        station (float): Normalized station of the cross-section along the body's length.
        upper_curve (Optional[Spline]): Spline defining the upper curve of the cross-section.
        lower_curve (Optional[Spline]): Spline defining the lower curve of the cross-section.

    Raises:
        ValueError: If neither an upper nor a lower curve spline is provided.
    """

    station: float = Field(..., ge=0, le=1, description="Normalized station of the cross-section along the body's length.")
    upper_curve: Optional[Spline] = Field(None, description="Spline defining the upper curve of the cross-section.")
    lower_curve: Optional[Spline] = Field(None, description="Spline defining the lower curve of the cross-section.")

    @model_validator(mode='before')
    def validate_curves(cls, values: dict) -> dict:
        """
        Validates that at least one of the upper or lower curve splines is provided.

        Args:
            values: Dictionary of field values.

        Returns:
            The validated dictionary of field values.

        Raises:
            ValueError: If neither an upper nor a lower curve spline is provided.
        """
        upper_curve = values.get("upper_curve")
        lower_curve = values.get("lower_curve")

        if upper_curve is None and lower_curve is None:
            raise ValueError("At least one of the upper or lower curve splines must be provided.")

        return values
        

class Body(CommonBaseModel):
    """
    Represents the geometric definition of a body-like surface component, such as an aircraft fuselage or engine nacelle.

    Attributes:
        reference_axis (Optional[Spline]): Spline defining the reference axis of the body.
        cross_sections (List[CrossSection]): List of CrossSection objects defining the body's shape at various stations.

    Raises:
        ValueError: If the list of cross sections is empty.
    """

    reference_axis: Optional[Spline] = Field(
        None,
        description="Spline defining the reference axis of the body.",
    )
    cross_sections: List[CrossSection] = Field(
        ...,
        description="List of CrossSection objects defining the body's shape at various stations.",
    )

    @field_validator("cross_sections", mode='before')
    def validate_cross_sections(cls, value: List[CrossSection]) -> List[CrossSection]:
        """
        Ensures that at least one CrossSection object is provided.

        Args:
            value: The list of CrossSection objects to validate.

        Returns:
            The validated list of CrossSection objects.

        Raises:
            ValueError: If the list is empty.
        """
        if not value:
            raise ValueError(
                "At least one CrossSection must be provided for the body geometry."
            )
        return value

class Geometry(CommonBaseModel):
    point: Optional[Point]
    polyline: Optional[Polyline]
    spline: Optional[Spline]
    cross_section: Optional[CrossSection]
    reference_axis: Optional[ReferenceAxis]
    airfoil: Optional[Airfoil]
    lifting_surface: Optional[LiftingSurface]
    body: Optional[Body]

