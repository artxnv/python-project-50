from gendiff.data_loader import load_data
from gendiff.nested_diff_builder import build_nested_diff_tree
from gendiff.flat_diff_builder import build_flat_diff_tree

def generate_diff(file1_path, file2_path, formatter):
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)
    diff_tree = build_diff(data1, data2)
    return formatter(diff_tree)  # Передаем дерево в форматтер

def build_diff(data1, data2):
    """Создает основное дерево различий в виде структуры данных, не зависящей от форматов."""
    diff_tree = []
    keys = sorted(set(data1.keys()).union(data2.keys()))

    for key in keys:
        if key not in data1:
            diff_tree.append({"key": key, "value": data2[key], "status": "added"})
        elif key not in data2:
            diff_tree.append({"key": key, "value": data1[key], "status": "removed"})
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff_tree.append({
                    "key": key,
                    "value": build_diff(data1[key], data2[key]),  # Вложенное дерево
                    "status": "nested"
                })
            elif data1[key] != data2[key]:
                diff_tree.append({
                    "key": key,
                    "old_value": data1[key],
                    "new_value": data2[key],
                    "status": "changed"
                })
            else:
                diff_tree.append({
                    "key": key,
                    "value": data1[key],
                    "status": "unchanged"
                })
    return diff_tree
