from gendiff.formater.common import resolve_to_string

# Константы для статусов
STATUS_EQUAL = 'equal'
STATUS_NESTED = 'nested'
STATUS_ADDED = 'added'
STATUS_DELETED = 'deleted'
STATUS_CHANGED = 'changed'


def format_plain(diff, path=''):
    result = []
    for item in diff:
        key = item['key']
        current_path = f'{path}.{key}' if path != '' else key
        lines = make_line(item, current_path)
        if lines is not None:
            result.append(lines)
    return '\n'.join(result)


def make_line(item, path):
    status = item['status']
    if status == STATUS_EQUAL:
        return None
    elif status == STATUS_NESTED:
        return format_plain(item['nested'], path)
    elif status == STATUS_ADDED:
        action = f'added with value: {get_value(item["new_value"])}'
    elif status == STATUS_DELETED:
        action = 'removed'
    elif status == STATUS_CHANGED:
        action = (f'updated. From {get_value(item["old_value"])}'
                  f' to {get_value(item["new_value"])}')
    else:
        raise ValueError('error in format diff')
    result = f"Property '{path}' was {action}"
    return result


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return resolve_to_string(value)
