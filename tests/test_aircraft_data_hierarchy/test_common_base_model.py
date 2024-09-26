import unittest
from typing import Any, Dict, Optional
from pydantic import ValidationError
from aircraft_data_hierarchy.common_base_model import CommonBaseModel, Metadata, NodeNotFoundError, PathAlreadyExistsError  # Replace 'your_module' with the actual module name

class TestCommonBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = CommonBaseModel()

    def test_create_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.assertEqual(self.model.get_node('root.node1'), {'key': 'value'})

    def test_create_node_existing_path(self):
        self.model.create_node('root.node1', {'key': 'value'})
        with self.assertRaises(PathAlreadyExistsError):
            self.model.create_node('root.node1', {'key': 'new_value'})

    def test_create_node_invalid_data(self):
        with self.assertRaises(TypeError):
            self.model.create_node('root.node1', 'invalid_data')

    def test_get_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.assertEqual(self.model.get_node('root.node1'), {'key': 'value'})
        self.assertIsNone(self.model.get_node('root.non_existent_node'))

    def test_update_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.update_node('root.node1', {'key': 'new_value'})
        self.assertEqual(self.model.get_node('root.node1'), {'key': 'new_value'})

    def test_update_node_non_existent_path(self):
        with self.assertRaises(NodeNotFoundError):
            self.model.update_node('root.non_existent_node', {'key': 'value'})

    def test_update_node_invalid_data(self):
        self.model.create_node('root.node1', {'key': 'value'})
        with self.assertRaises(TypeError):
            self.model.update_node('root.node1', 'invalid_data')

    def test_delete_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.delete_node('root.node1')
        self.assertIsNone(self.model.get_node('root.node1'))

    def test_delete_node_non_existent_path(self):
        with self.assertRaises(NodeNotFoundError):
            self.model.delete_node('root.non_existent_node')

    def test_move_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.move_node('root.node1', 'root.node2')
        self.assertIsNone(self.model.get_node('root.node1'))
        self.assertEqual(self.model.get_node('root.node2'), {'key': 'value'})

    def test_move_node_non_existent_source(self):
        with self.assertRaises(NodeNotFoundError):
            self.model.move_node('root.non_existent_node', 'root.node2')

    def test_move_node_existing_target(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.create_node('root.node2', {'key': 'value'})
        with self.assertRaises(PathAlreadyExistsError):
            self.model.move_node('root.node1', 'root.node2')

    def test_copy_node(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.copy_node('root.node1', 'root.node2')
        self.assertEqual(self.model.get_node('root.node1'), {'key': 'value'})
        self.assertEqual(self.model.get_node('root.node2'), {'key': 'value'})

    def test_copy_node_non_existent_source(self):
        with self.assertRaises(NodeNotFoundError):
            self.model.copy_node('root.non_existent_node', 'root.node2')

    def test_copy_node_existing_target(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.create_node('root.node2', {'key': 'value'})
        with self.assertRaises(PathAlreadyExistsError):
            self.model.copy_node('root.node1', 'root.node2')

    def test_merge_nodes(self):
        self.model.create_node('root.node1', {'key1': 'value1'})
        self.model.create_node('root.node2', {'key2': 'value2'})
        self.model.merge_nodes('root.node1', 'root.node2')
        self.assertEqual(self.model.get_node('root.node2'), {'key2': 'value2', 'key1': 'value1'})

    def test_merge_nodes_non_existent_source(self):
        self.model.create_node('root.node2', {'key2': 'value2'})
        with self.assertRaises(NodeNotFoundError):
            self.model.merge_nodes('root.non_existent_node', 'root.node2')

    def test_merge_nodes_non_existent_target(self):
        self.model.create_node('root.node1', {'key1': 'value1'})
        with self.assertRaises(NodeNotFoundError):
            self.model.merge_nodes('root.node1', 'root.non_existent_node')

    def test_link_nodes(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.create_node('root.node2', {'key': 'value'})
        self.model.link_nodes('root.node1', 'root.node2')
        self.assertEqual(self.model.aliases['root.node1'], 'root.node2')

    def test_link_nodes_non_existent_source(self):
        self.model.create_node('root.node2', {'key': 'value'})
        with self.assertRaises(NodeNotFoundError):
            self.model.link_nodes('root.non_existent_node', 'root.node2')

    def test_link_nodes_non_existent_target(self):
        self.model.create_node('root.node1', {'key': 'value'})
        with self.assertRaises(NodeNotFoundError):
            self.model.link_nodes('root.node1', 'root.non_existent_node')

    def test_unlink_nodes(self):
        self.model.create_node('root.node1', {'key': 'value'})
        self.model.create_node('root.node2', {'key': 'value'})
        self.model.link_nodes('root.node1', 'root.node2')
        self.model.unlink_nodes('root.node1')
        self.assertNotIn('root.node1', self.model.aliases)

    def test_unlink_nodes_non_existent_link(self):
        with self.assertRaises(NodeNotFoundError):
            self.model.unlink_nodes('root.non_existent_node')

    def test_search_nodes(self):
        self.model.create_node('root.node1', {'key': 'value1'})
        self.model.create_node('root.node2', {'key': 'value2'})
        results = self.model.search_nodes({'key': 'value1'})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['key'], 'value1')


class TestMetadata(unittest.TestCase):

    def test_metadata_creation(self):
        metadata = Metadata(key='test_key', value='test_value')
        self.assertEqual(metadata.key, 'test_key')
        self.assertEqual(metadata.value, 'test_value')

    def test_metadata_key_empty(self):
        with self.assertRaises(ValidationError):
            Metadata(key='', value='test_value')

    def test_metadata_key_too_long(self):
        with self.assertRaises(ValidationError):
            Metadata(key='a' * 256, value='test_value')

    def test_metadata_key_strip_whitespace(self):
        metadata = Metadata(key='  test_key  ', value='test_value')
        self.assertEqual(metadata.key, 'test_key')


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
