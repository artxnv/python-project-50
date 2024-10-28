# stylish.py
def format_stylish(diff_tree, depth=0):
    """Форматирует дерево различий в стиль 'stylish'."""
    indent = '  ' * depth
    lines = ["{"]
    
    for node in diff_tree:
        key = node['key']
        status = node['status']
        
        if status == 'added':
            lines.append(f"{indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif status == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif status == 'changed':
            lines.append(f"{indent}  - {key}: {format_value(node['old_value'], depth + 1)}")
            lines.append(f"{indent}  + {key}: {format_value(node['new_value'], depth + 1)}")
        elif status == 'unchanged':
            lines.append(f"{indent}    {key}: {format_value(node['value'], depth + 1)}")
        elif status == 'nested':
            lines.append(f"{indent}    {key}: {format_stylish(node['value'], depth + 1)}")
    
    lines.append(f"{'  ' * (depth)}" + "}")
    return '\n'.join(lines)

def format_value(value, depth):
    """Вспомогательная функция для форматирования значений."""
    if isinstance(value, dict):
        indent = '  ' * depth
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    return str(value).lower() if isinstance(value, bool) else str(value)
