from gendiff.formatters.common import resolve_to_string

ONE_INDENT = '    '

def format_nested_stylish(diff, level=1):
    result = []
    for item in diff:
        result.extend(get_list_lines(item, level))
    result.insert(0, '{')
    result.append(get_indent(level - 1) + '}')
    return '\n'.join(result)

def get_list_lines(item, level):
    result = []
    status = item['status']
    key = item['key']
    new_value = item.get('new_value')
    old_value = item.get('old_value')

    indent = get_indent(level)
    if status == 'nested':
        # Добавляем обработку для вложенных элементов
        result.append(f'{indent}{key}: '
                      f'{format_nested_stylish(item["value"], level + 1)}')
    elif status in ['equal', 'unchanged']:
        # Обработка для равных значений
        result.append(f'{indent}  {key}: {get_value(old_value)}')  # Используем только old_value
    elif status == 'removed':
        result.append(f'{indent}- {key}: {get_value(old_value)}')
    elif status == 'added':
        result.append(f'{indent}+ {key}: {get_value(new_value)}')
    elif status == 'changed':
        result.append(f'{indent}- {key}: {get_value(old_value)}')
        result.append(f'{indent}+ {key}: {get_value(new_value)}')
    else:
        raise ValueError(f'Unexpected status: {status} in item: {item}')

    return result

def get_value(value):
    # Убрали level, так как он не нужен здесь
    if isinstance(value, dict):
        return dict_to_str(value)
    else:
        return resolve_to_string(value)

def dict_to_str(dict_):
    result = '{\n'
    for key in sorted(dict_.keys()):
        value = dict_[key]
        line = get_value(value) if isinstance(value, (dict, list)) else resolve_to_string(value)
        result += f'{get_indent(1)}{key}: {line}\n'  # Исправлено на 1
    result += get_indent(0) + '}'  # Исправлено на 0
    return result

def get_indent(level):
    return ONE_INDENT * level
