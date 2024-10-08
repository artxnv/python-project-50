import json


def generate_diff(file1_path, file2_path):
    # Чтение и парсинг JSON-файлов
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)
    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

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
        return str(value).lower()  # Приводим к нижнему регистру для JSON
    elif isinstance(value, str):
        return value  # Оставляем строки без изменений
    return json.dumps(value)  # Для остальных типов используем json.dumps
