from gendiff.formater.stylish import format_stylish
from gendiff.formater.plain import format_plain
from gendiff.formater.json import format_json


def get_formatted_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError('Unsupported format name')
