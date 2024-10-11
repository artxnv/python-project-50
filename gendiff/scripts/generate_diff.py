import json

from gendiff.parsers import parse_file


def generate_diff(file1_path, file2_path):
    # Чтение и парсинг файлов
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    # Получаем все ключи из обоих файлов
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    # Формируем результат сравнения
    result = ["{"]
    for key in keys:
        if key not in data2:
            result.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            result.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {format_value(data1[key])}")
            result.append(f"  + {key}: {format_value(data2[key])}")
        else:
            result.append(f"    {key}: {format_value(data1[key])}")

    result.append("}")
    return "\n".join(result)


def format_value(value):
    """Форматирует значение для вывода в нужном формате."""
    if isinstance(value, bool):
        return str(value).lower()  # Приводим к нижнему регистру для JSON и YAML
    elif isinstance(value, str):
        return value  # Оставляем строки без изменений
    return json.dumps(value)  # Для остальных типов используем json.dumps
