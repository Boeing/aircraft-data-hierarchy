import unittest
from pydantic import ValidationError
from aircraft_data_hierarchy.behavior import (
    Activity,
    ActivityState,
    Behavior,
    Bounds,
    ContactInfoType,
    ContactLocation,
    DataTable,
    ExtrapolateEnum,
    InterpolateEnum,
    Metadata,
    NormalPDF,
    Uncertainty,
    UncertaintyEffect,
    UniformPDF,
)


class TestBehavior(unittest.TestCase):
    def test_behavior_creation(self):
        activity = Activity(
            name="CruiseCalculation",
            description="Computes cruising fuel flow",
            state=ActivityState.IN_PROGRESS,
        )
        behavior = Behavior(
            name="MissionPerformance",
            description="Overall mission performance profile",
            sequence=[activity],
            metadata=Metadata(key="domain", value="aerodynamics"),
        )
        self.assertEqual(behavior.name, "MissionPerformance")
        self.assertEqual(len(behavior.sequence), 1)
        self.assertEqual(behavior.sequence[0].name, "CruiseCalculation")
        self.assertEqual(behavior.sequence[0].state, ActivityState.IN_PROGRESS)
        self.assertEqual(behavior.metadata.key, "domain")
        self.assertEqual(behavior.metadata.value, "aerodynamics")

    def test_activity_validation_empty_name(self):
        with self.assertRaises(ValidationError):
            Activity(name="   ", description="Valid description")

    def test_behavior_validation_empty_sequence(self):
        with self.assertRaises(ValidationError):
            Behavior(
                name="TestBehavior",
                description="Behavior with empty sequence",
                sequence=[],
            )

    def test_uncertainty_models(self):
        bounds = Bounds(value="10.0")
        normal_pdf = NormalPDF(num_sigmas=3.0, bounds=[bounds])
        uncertainty = Uncertainty(
            effect=UncertaintyEffect.ADDITIVE,
            normal_pdf=normal_pdf,
        )
        self.assertEqual(uncertainty.effect, UncertaintyEffect.ADDITIVE)
        self.assertEqual(uncertainty.normal_pdf.num_sigmas, 3.0)
        self.assertEqual(len(uncertainty.normal_pdf.bounds), 1)
        self.assertEqual(uncertainty.normal_pdf.bounds[0].value, "10.0")

        uniform_pdf = UniformPDF(bounds=[bounds])
        self.assertEqual(len(uniform_pdf.bounds), 1)
        self.assertEqual(uniform_pdf.bounds[0].value, "10.0")

    def test_enums(self):
        self.assertEqual(ExtrapolateEnum.BOTH.value, "both")
        self.assertEqual(InterpolateEnum.LINEAR.value, "linear")
        self.assertEqual(ContactInfoType.EMAIL.value, "email")
        self.assertEqual(ContactLocation.PROFESSIONAL.value, "professional")


if __name__ == "__main__":
    unittest.main()
