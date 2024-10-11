import json
import os

import yaml


def parse_file(file_path):
    """Parse a file and return its contents as a dictionary.

    Args:
        file_path (str): The path to the file to be parsed.

    Returns:
        dict: The parsed content of the file.

    Raises:
        ValueError: If the file format is unsupported.
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
        json.JSONDecodeError: If there is an error parsing the JSON file.
    """
    extension = os.path.splitext(file_path)[1].lower()  # Get the file extension

    try:
        with open(file_path, 'r') as file:
            if extension in ['.yaml', '.yml']:
                return yaml.safe_load(file)  # For YAML files
            elif extension == '.json':
                return json.load(file)  # For JSON files
            else:
                raise ValueError(f"Unsupported file format: {extension}")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
