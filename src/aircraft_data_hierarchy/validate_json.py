import argparse
import json
import logging
from pathlib import Path

from pydantic import ValidationError

from aircraft_data_hierarchy.work_breakdown_structure.work_breakdown_structure import (
    AircraftSystem,
)

logger = logging.getLogger("adh")
logging.basicConfig(level=logging.INFO)


def validate_json(json_data: dict) -> bool:
    """
    Validate the structure of the provided JSON data using Pydantic models.

    Parameters
    ----------
    json_data : dict
        The JSON data to validate.

    Returns
    -------
    bool
        True if the JSON data is valid, False otherwise.
    """
    try:
        AircraftSystem(**json_data)
        return True
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return False


def main() -> None:
    """
    Main function to read and validate the JSON file.
    """
    parser = argparse.ArgumentParser(description="Validate a JSON file.")
    parser.add_argument(
        "json_file_path", type=str, help="The path to the JSON file to validate."
    )
    args = parser.parse_args()

    json_file_path = args.json_file_path
    json_path = Path(json_file_path)
    if not json_path.is_file():
        logger.error(f"File not found: {json_file_path=}")
        return

    with open(json_file_path, "r") as f:
        json_data = json.load(f)

    if validate_json(json_data):
        logger.info("JSON file is valid.")
    else:
        logger.error("JSON file is invalid.")


if __name__ == "__main__":
    main()
