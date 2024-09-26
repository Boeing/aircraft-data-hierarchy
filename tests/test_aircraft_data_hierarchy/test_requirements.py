import unittest
from typing import List, Dict
from pydantic import ValidationError
from aircraft_data_hierarchy.common_base_model import Metadata, CommonBaseModel
from aircraft_data_hierarchy.requirements import Requirement, Requirements  # Replace 'your_module' with the actual module name


class TestRequirement(unittest.TestCase):

    def test_valid_requirement(self):
        """Test creating a valid Requirement instance."""
        metadata = Metadata(key="example_key", value="example_value")
        req = Requirement(
            name="REQ-001",
            description="This is a test requirement.",
            category="performance",
            priority="high",
            verification_method="test",
            status="open",
            source="customer",
            target_component="component-1",
            acceptance_criteria="Must pass all tests.",
            risk="Low risk",
            verification_evidence="Test report",
            metadata=metadata
        )
        self.assertEqual(req.name, "REQ-001")
        self.assertEqual(req.description, "This is a test requirement.")
        self.assertEqual(req.category, "performance")
        self.assertEqual(req.priority, "high")
        self.assertEqual(req.verification_method, "test")
        self.assertEqual(req.status, "open")
        self.assertEqual(req.source, "customer")
        self.assertEqual(req.target_component, "component-1")
        self.assertEqual(req.acceptance_criteria, "Must pass all tests.")
        self.assertEqual(req.risk, "Low risk")
        self.assertEqual(req.verification_evidence, "Test report")
        self.assertIsInstance(req.metadata, Metadata)

    def test_invalid_requirement_empty_fields(self):
        """Test creating a Requirement instance with empty critical fields."""
        with self.assertRaises(ValidationError):
            Requirement(
                name="",
                description="",
                priority="",
                verification_method="",
                status="",
                acceptance_criteria=""
            )

    def test_optional_fields(self):
        """Test creating a Requirement instance with optional fields omitted."""
        req = Requirement(
            name="REQ-002",
            description="This is another test requirement.",
            priority="medium",
            verification_method="analysis",
            status="in progress",
            acceptance_criteria="Must meet analysis criteria."
        )
        self.assertIsNone(req.category)
        self.assertIsNone(req.source)
        self.assertIsNone(req.target_component)
        self.assertIsNone(req.risk)
        self.assertIsNone(req.verification_evidence)
        self.assertIsNone(req.metadata)


class TestRequirements(unittest.TestCase):

    def setUp(self):
        """Set up a Requirements instance for testing."""
        metadata = Metadata(key="example_key", value="example_value")
        self.requirements = Requirements(
            name="Project Requirements",
            description="A set of project requirements.",
            metadata=metadata
        )

    def test_add_requirement(self):
        """Test adding a requirement to a category."""
        req = Requirement(
            name="REQ-003",
            description="A new requirement.",
            priority="low",
            verification_method="inspection",
            status="open",
            acceptance_criteria="Must pass inspection."
        )
        self.requirements.add_requirement(req, "safety")
        self.assertIn("safety", self.requirements.requirements)
        self.assertEqual(len(self.requirements.requirements["safety"]), 1)
        self.assertEqual(self.requirements.requirements["safety"][0].name, "REQ-003")

    def test_remove_requirement(self):
        """Test removing a requirement from a category."""
        req = Requirement(
            name="REQ-004",
            description="Another new requirement.",
            priority="medium",
            verification_method="test",
            status="open",
            acceptance_criteria="Must pass all tests."
        )
        self.requirements.add_requirement(req, "performance")
        self.requirements.remove_requirement("REQ-004", "performance")
        self.assertNotIn("REQ-004", [r.name for r in self.requirements.requirements["performance"]])

    def test_remove_nonexistent_requirement(self):
        """Test removing a non-existent requirement."""
        with self.assertRaises(ValueError):
            self.requirements.remove_requirement("REQ-999", "performance")

    def test_get_requirements_by_category(self):
        """Test retrieving requirements by category."""
        req1 = Requirement(
            name="REQ-005",
            description="Requirement 1.",
            priority="high",
            verification_method="test",
            status="open",
            acceptance_criteria="Must pass all tests."
        )
        req2 = Requirement(
            name="REQ-006",
            description="Requirement 2.",
            priority="medium",
            verification_method="analysis",
            status="in progress",
            acceptance_criteria="Must meet analysis criteria."
        )
        self.requirements.add_requirement(req1, "design")
        self.requirements.add_requirement(req2, "design")
        design_reqs = self.requirements.get_requirements_by_category("design")
        self.assertEqual(len(design_reqs), 2)
        self.assertEqual(design_reqs[0].name, "REQ-005")
        self.assertEqual(design_reqs[1].name, "REQ-006")

    def test_get_requirements_by_nonexistent_category(self):
        """Test retrieving requirements from a non-existent category."""
        with self.assertRaises(ValueError):
            self.requirements.get_requirements_by_category("nonexistent")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

