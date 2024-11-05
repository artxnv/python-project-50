import json
import yaml
from pathlib import Path
from gendiff.comparator import create_diff
from gendiff.formater.formatter_selector import get_formatted_diff


def get_data_from_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def data_to_dict(data, ext):
    if ext == '.json':
        return json.loads(data)
    elif ext in ['.yaml', '.yml']:
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError('Unsupported file format')


def file_to_dict(path):
    data = get_data_from_file(path)
    ext = Path(path).suffix
    return data_to_dict(data, ext)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = file_to_dict(file_path1)
    dict2 = file_to_dict(file_path2)
    diff = create_diff(dict1, dict2)
    return get_formatted_diff(diff, format_name)
