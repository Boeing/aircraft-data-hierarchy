import unittest
from pydantic import ValidationError
from typing import List, Dict, Any, Optional
from aircraft_data_hierarchy.common_base_model import CommonBaseModel, Metadata
from aircraft_data_hierarchy.requirements import Requirement
from aircraft_data_hierarchy.performance import Discipline
from aircraft_data_hierarchy.behavior import Behavior
from aircraft_data_hierarchy.work_breakdown_structure.airframe import Component


class TestComponent(unittest.TestCase):
    """Unit tests for the Component class."""

    def test_component_creation(self):
        """
        Test creating a Component with all fields provided.
        """
        metadata = Metadata(key="example_key", value="example_value")
        component = Component(
            name="Engine",
            description="Main engine component",
            requirements=[Requirement(
                name="Req1",
                description="Requirement 1",
                priority="High",
                verification_method="Test",
                status="Open",
                acceptance_criteria="Criteria 1"
            )],
            subcomponents=[],
            metadata=metadata,
            performance=[Discipline(
                name="Performance1",
                description="Performance description"
            )],
            behavior=[Behavior(
                name="Behavior1",
                description="Behavior description"
            )]
        )
        self.assertEqual(component.name, "Engine")
        self.assertEqual(component.description, "Main engine component")
        self.assertEqual(component.metadata, metadata)
        self.assertEqual(len(component.requirements), 1)
        self.assertEqual(component.subcomponents, [])
        self.assertEqual(len(component.performance), 1)
        self.assertEqual(len(component.behavior), 1)

    def test_default_values(self):
        """
        Test that default values are set correctly.
        """
        component = Component()
        self.assertIsNone(component.name)
        self.assertIsNone(component.description)
        self.assertIsNone(component.requirements)
        self.assertIsNone(component.subcomponents)
        self.assertIsNone(component.geometry)
        self.assertIsNone(component.parameters)
        self.assertIsNone(component.metadata)
        self.assertIsNone(component.performance)
        self.assertIsNone(component.behavior)

    def test_non_empty_validation(self):
        """
        Test that name and description fields must not be empty or whitespace only.
        """
        with self.assertRaises(ValidationError):
            Component(name=" ", description="Valid description")
        with self.assertRaises(ValidationError):
            Component(name="Valid name", description=" ")

    def test_optional_fields(self):
        """
        Test that optional fields can be omitted.
        """
        component = Component(name="Engine", description="Main engine component")
        self.assertEqual(component.name, "Engine")
        self.assertEqual(component.description, "Main engine component")
        self.assertIsNone(component.requirements)
        self.assertIsNone(component.subcomponents)
        self.assertIsNone(component.geometry)
        self.assertIsNone(component.parameters)
        self.assertIsNone(component.metadata)
        self.assertIsNone(component.performance)
        self.assertIsNone(component.behavior)

    def test_recursive_subcomponents(self):
        """
        Test that subcomponents can be nested within a component.
        """
        subcomponent = Component(name="SubEngine", description="Sub engine component")
        component = Component(
            name="Engine",
            description="Main engine component",
            subcomponents=[subcomponent]
        )
        self.assertEqual(len(component.subcomponents), 1)
        self.assertEqual(component.subcomponents[0].name, "SubEngine")
        self.assertEqual(component.subcomponents[0].description, "Sub engine component")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
