def format_diff(diff_tree):
    return format_stylish(diff_tree)


def format_stylish(diff_tree):
    def format_node(node, depth=0):
        indent = ' ' * 4 * depth
        lines = []

        for item in node:
            key = item['key']
            status = item['status']

            if status == 'added':
                lines.append(f"{indent}+ {key}: {format_value(item['value'], depth)}")
            elif status == 'removed':
                lines.append(f"{indent}- {key}: {format_value(item['value'], depth)}")
            elif status == 'unchanged':
                lines.append(f"{indent}  {key}: {format_value(item['value'], depth)}")
            elif status == 'changed':
                lines.append(f"{indent}- {key}: {format_value(item['old_value'], depth)}")
                lines.append(f"{indent}+ {key}: {format_value(item['new_value'], depth)}")
            elif status == 'nested':
                lines.append(f"{indent}  {key}: {{")
                lines.append(format_node(item['value'], depth + 1))
                lines.append(f"{indent}  }}")

        return '\n'.join(lines)

    def format_value(value, depth):
        if isinstance(value, dict):
            lines = []
            indent = ' ' * 4 * (depth + 1)
            for k, v in value.items():
                lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
            return "{{\n{}\n{}}}".format('\n'.join(lines), ' ' * 4 * depth)  # Используем метод format()
        return format_primitive_value(value)

    def format_primitive_value(value):
        if isinstance(value, bool):
            return str(value).lower()
        if value is None:
            return 'null'
        return str(value)

    return format_node(diff_tree)
