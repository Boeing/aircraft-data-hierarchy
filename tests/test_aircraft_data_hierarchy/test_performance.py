import unittest
from datetime import datetime
from pydantic import ValidationError
from aircraft_data_hierarchy.common_base_model import CommonBaseModel, Metadata
from aircraft_data_hierarchy.performance import DataExchange, ModelDescription, Discipline
import uuid

# Assuming the classes DataExchange, ModelDescription, and Discipline are already defined as provided

class TestModels(unittest.TestCase):

    def test_data_exchange_creation(self):
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"]
        )
        self.assertEqual(data_exchange.model_identifier, "model_123")
        self.assertEqual(data_exchange.inputs, ["input1", "input2"])
        self.assertEqual(data_exchange.outputs, ["output1"])

    def test_data_exchange_optional_fields(self):
        data_exchange = DataExchange()
        self.assertIsNone(data_exchange.model_identifier)
        self.assertEqual(data_exchange.inputs, [])
        self.assertEqual(data_exchange.outputs, [])

    def test_model_description_creation(self):
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"]
        )
        model_description = ModelDescription(
            specification_version="2.0",
            model_name="Test Model",
            guid=str(uuid.uuid4()),
            generation_tool="Tool XYZ",
            generation_date_and_time=datetime.now(),
            data_exchange=data_exchange,
            license="MIT",
            copyright="NASA",
            author="John Doe",
            version="1.0",
            description="A test model"
        )
        self.assertEqual(model_description.specification_version, "2.0")
        self.assertEqual(model_description.model_name, "Test Model")
        self.assertEqual(model_description.data_exchange, data_exchange)

    def test_model_description_optional_fields(self):
        model_description = ModelDescription()
        self.assertIsNone(model_description.specification_version)
        self.assertIsNone(model_description.model_name)
        self.assertIsNone(model_description.guid)
        self.assertIsNone(model_description.generation_tool)
        self.assertIsNone(model_description.generation_date_and_time)
        self.assertIsNone(model_description.data_exchange)
        self.assertIsNone(model_description.license)
        self.assertIsNone(model_description.copyright)
        self.assertIsNone(model_description.author)
        self.assertIsNone(model_description.version)
        self.assertIsNone(model_description.description)

    def test_model_description_invalid_specification_version(self):
        with self.assertRaises(ValidationError):
            ModelDescription(specification_version="1.0")

    def test_model_description_invalid_guid(self):
        with self.assertRaises(ValidationError):
            ModelDescription(guid="invalid-guid")

    def test_discipline_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(
            name="Aerodynamics",
            description="Study of the motion of air",
            tools=[],
            metadata=metadata
        )
        self.assertEqual(discipline.name, "Aerodynamics")
        self.assertEqual(discipline.description, "Study of the motion of air")
        self.assertEqual(discipline.tools, [])
        self.assertEqual(discipline.metadata, metadata)

    def test_discipline_optional_fields(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(metadata=metadata)
        self.assertIsNone(discipline.name)
        self.assertIsNone(discipline.description)
        self.assertEqual(discipline.tools, [])
        self.assertIsNotNone(discipline.metadata)

    def test_discipline_invalid_name(self):
        with self.assertRaises(ValidationError):
            Discipline(name="Invalid Name!", metadata=Metadata(key="example_key", value="example_value"))

    def test_discipline_add_tool(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(
            name="Aerodynamics",
            description="Study of the motion of air",
            tools=[],
            metadata=metadata
        )
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"]
        )
        model_description = ModelDescription(
            specification_version="2.0",
            model_name="Test Model",
            guid=str(uuid.uuid4()),
            generation_tool="Tool XYZ",
            generation_date_and_time=datetime.now(),
            data_exchange=data_exchange,
            license="MIT",
            copyright="NASA",
            author="John Doe",
            version="1.0",
            description="A test model"
        )
        discipline.add_tool(model_description)
        self.assertEqual(len(discipline.tools), 1)
        self.assertEqual(discipline.tools[0], model_description)

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)
