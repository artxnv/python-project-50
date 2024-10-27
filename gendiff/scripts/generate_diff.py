import json
from gendiff.data_loader import load_data
from gendiff.nested_diff_builder import build_nested_diff_tree  # Подразумевается, что вы реализовали эту функцию
from gendiff.flat_diff_builder import build_flat_diff_tree  # Подразумевается, что вы реализовали эту функцию
from gendiff.formatters.stylish import format_stylish  # Подразумеется, что вы реализовали эту функцию

def generate_diff(file1_path, file2_path):
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)
    return build_diff(data1, data2)

def build_diff(data1, data2, depth=0):
    diff = []
    keys = sorted(set(data1.keys()).union(data2.keys()))

    for key in keys:
        if key not in data1:
            diff.append(f"{'  ' * depth}+ {key}: {format_value(data2[key], depth)}")
        elif key not in data2:
            diff.append(f"{'  ' * depth}- {key}: {format_value(data1[key], depth)}")
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff.append(f"{'  ' * depth}  {key}: {{")
                diff.append(build_diff(data1[key], data2[key], depth + 1))
                diff.append(f"{'  ' * depth}  }}")
            elif data1[key] != data2[key]:
                diff.append(f"{'  ' * depth}- {key}: {format_value(data1[key], depth)}")
                diff.append(f"{'  ' * depth}+ {key}: {format_value(data2[key], depth)}")
            else:
                diff.append(f"{'  ' * depth}  {key}: {format_value(data1[key], depth)}")

    # Объединяем список в строку с переносами
    return '\n'.join(diff)


def format_value(value, depth=0):
    """Форматирует значение для вывода в нужном формате."""
    indent = '  ' * (depth + 1)
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{'  ' * depth}}}")
        return '\n'.join(lines)
    return json.dumps(value)
