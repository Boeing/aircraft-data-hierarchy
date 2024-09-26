import unittest

class TestImports(unittest.TestCase):
    def test_import_aircraft_data_hierarchy(self):
        try:
            from aircraft_data_hierarchy import Behavior, CommonBaseModel, DataExchange, Requirements
        except ImportError:
            self.fail("Failed to from aircraft_data_hierarchy")

    def test_import_work_breakdown_structure(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure import Equipment, AircraftSystem
        except ImportError:
            self.fail("Failed to import from aircraft_data_hierarchy.work_breakdown_structure")

    def test_import_work_breakdown_structure_airframe(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.airframe import Component, Loft, AerodynamicsData
        except ImportError:
            self.fail("Failed to from aircraft_data_hierarchy.work_breakdown_structure.airframe")

    def test_import_work_breakdown_structure_propulsion(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.propulsion import Propulsion, PropulsionGeometry, PropulsionCycle
        except ImportError:
            self.fail("Failed to from aircraft_data_hierarchy.work_breakdown_structure.propulsion")

    def test_import_work_breakdown_structure_systems(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.systems import System, SystemAttributes, create_system_diagram
        except ImportError:
            self.fail("Failed to from aircraft_data_hierarchy.work_breakdown_structure.systems")

if __name__ == '__main__':
    unittest.main()