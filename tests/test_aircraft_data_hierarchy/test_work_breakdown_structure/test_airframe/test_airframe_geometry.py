import unittest
from pydantic import ValidationError
from typing import List
from aircraft_data_hierarchy.work_breakdown_structure.airframe.airframe_geometry import (
    CrossSection, Body, Point, Polyline, Mesh, Airfoil, Spline, LiftingSurface, Loft, String, Boolean, Float, Integer, Metadata
)

class TestPydanticModels(unittest.TestCase):

    def test_cross_section(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0)
        ]
        upper_curve = Spline(points=points)
        lower_curve = Spline(points=points)
        data = {
            "station": 0.5,
            "upper_curve": upper_curve,
            "lower_curve": lower_curve
        }
        model = CrossSection(**data)
        self.assertEqual(model.station, 0.5)
        self.assertEqual(model.upper_curve, upper_curve)
        self.assertEqual(model.lower_curve, lower_curve)

        # Test missing both curves
        data = {
            "station": 0.5
        }
        with self.assertRaises(ValidationError):
            CrossSection(**data)

    def test_body_geometry(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0)
        ]
        reference_axis = Spline(points=points)
        cross_section = CrossSection(station=0.5, upper_curve=Spline(points=points))
        data = {
            "reference_axis": reference_axis,
            "cross_sections": [cross_section]
        }
        model = Body(**data)
        self.assertEqual(model.reference_axis, reference_axis)
        self.assertEqual(model.cross_sections, [cross_section])

        # Test missing cross_sections
        data["cross_sections"] = []
        with self.assertRaises(ValidationError):
            Body(**data)

    def test_lifting_surface_geometry(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0)
        ]
        leading_edge_spline = Spline(points=points)
        trailing_edge_spline = Spline(points=points)
        airfoil_section = Airfoil(spline=Spline(points=points))
        data = {
            "leading_edge_spline": leading_edge_spline,
            "trailing_edge_spline": trailing_edge_spline,
            "airfoil_sections": [airfoil_section]
        }
        model = LiftingSurface(**data)
        self.assertEqual(model.leading_edge_spline, leading_edge_spline)
        self.assertEqual(model.trailing_edge_spline, trailing_edge_spline)
        self.assertEqual(model.airfoil_sections, [airfoil_section])

        # Test missing airfoil_sections
        data["airfoil_sections"] = []
        with self.assertRaises(ValidationError):
            LiftingSurface(**data)

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        point = Point(x=1.0, y=2.0, z=3.0)
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)
        self.assertEqual(point.z, 3.0)

    def test_point_distance(self):
        point1 = Point(x=0.0, y=0.0, z=0.0)
        point2 = Point(x=1.0, y=1.0, z=1.0)
        self.assertAlmostEqual(point1.distance_to(point2), 1.732, places=3)

class TestPolyline(unittest.TestCase):
    def test_polyline_creation(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        self.assertEqual(len(polyline.points), 2)

    def test_polyline_length(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        self.assertAlmostEqual(polyline.length(), 1.732, places=3)

    def test_polyline_simplify(self):
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=1.0, y=1.0, z=1.0)
        ]
        polyline = Polyline(points=points)
        simplified_polyline = polyline.simplify(tolerance=0.1)
        self.assertEqual(len(simplified_polyline.points), 2)

class TestMesh(unittest.TestCase):
    def test_mesh_creation(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        mesh = Mesh(polylines=[polyline])
        self.assertEqual(len(mesh.polylines), 1)

    # TODO: Fix Issue with unexpected is_manifold() results
    # def test_mesh_is_manifold(self):
    #     points = [
    #         Point(x=0.0, y=0.0, z=0.0),
    #         Point(x=1.0, y=0.0, z=0.0),
    #         Point(x=1.0, y=1.0, z=0.0),
    #         Point(x=0.0, y=1.0, z=0.0)
    #     ]
    #     polyline = Polyline(points=points)
    #     mesh = Mesh(polylines=[polyline])
    #     self.assertTrue(mesh.is_manifold())

    def test_mesh_calculate_volume(self):
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=1.0, y=0.0, z=0.0),
            Point(x=1.0, y=1.0, z=0.0),
            Point(x=0.0, y=1.0, z=0.0)
        ]
        polyline = Polyline(points=points)
        mesh = Mesh(polylines=[polyline])
        self.assertAlmostEqual(mesh.calculate_volume(), 0.0, places=3)

class TestSpline(unittest.TestCase):
    def test_spline_creation(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0),
                  Point(x=2.0, y=2.0, z=2.0),  Point(x=3.0, y=3.0, z=3.0)]
        spline = Spline(points=points, degree=3)
        self.assertEqual(len(spline.points), 4)
        self.assertEqual(spline.degree, 3)

    def test_spline_validation(self):
        points = [Point(x=0.0, y=0.0, z=0.0)]
        with self.assertRaises(ValidationError):
            Spline(points=points, degree=3)

class TestLoft(unittest.TestCase):
    def test_loft_creation(self):
        points1 = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0),
                   Point(x=2.0, y=2.0, z=2.0), Point(x=3.0, y=3.0, z=3.0)]
        points2 = [Point(x=0.0, y=0.0, z=1.0), Point(x=1.0, y=1.0, z=2.0),
                   Point(x=2.0, y=2.0, z=3.0), Point(x=3.0, y=3.0, z=4.0)]
        spline1 = Spline(points=points1, degree=4)
        spline2 = Spline(points=points2, degree=4)
        loft = Loft(splines=[spline1, spline2], num_samples=10)
        self.assertEqual(len(loft.splines), 2)
        self.assertEqual(loft.num_samples, 10)

    def test_loft_calculate_surface(self):
        points1 = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0),
                   Point(x=2.0, y=2.0, z=2.0), Point(x=3.0, y=3.0, z=3.0)]
        points2 = [Point(x=0.0, y=0.0, z=1.0), Point(x=1.0, y=1.0, z=2.0),
                   Point(x=2.0, y=2.0, z=3.0), Point(x=3.0, y=3.0, z=4.0)]
        spline1 = Spline(points=points1, degree=4)
        spline2 = Spline(points=points2, degree=4)
        loft = Loft(splines=[spline1, spline2], num_samples=10)
        surface = loft.calculate_surface()
        self.assertEqual(len(surface), 40)  # 2 splines * 10 samples

class TestString(unittest.TestCase):
    def test_string_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        string = String(value="test", default="default", metadata=metadata)
        self.assertEqual(string.value, "test")
        self.assertEqual(string.default, "default")

    def test_string_validation(self):
        with self.assertRaises(ValidationError):
            String(value="")

class TestBoolean(unittest.TestCase):
    def test_boolean_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        boolean = Boolean(value=True, default=False, metadata=metadata)
        self.assertTrue(boolean.value)
        self.assertFalse(boolean.default)

    def test_boolean_validation(self):
        with self.assertRaises(ValidationError):
            Boolean(value="not a boolean")

class TestFloat(unittest.TestCase):
    def test_float_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        float_var = Float(value=1.23, default=0.0, metadata=metadata)
        self.assertAlmostEqual(float_var.value, 1.23)
        self.assertAlmostEqual(float_var.default, 0.0)

    def test_float_validation(self):
        with self.assertRaises(ValidationError):
            Float(value="not a float")

class TestInteger(unittest.TestCase):
    def test_integer_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        integer = Integer(value=123, default=0, metadata=metadata)
        self.assertEqual(integer.value, 123)
        self.assertEqual(integer.default, 0)

    def test_integer_validation(self):
        with self.assertRaises(ValidationError):
            Integer(value="not an integer")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
