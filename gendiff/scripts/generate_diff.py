import json

def generate_diff(file1_path, file2_path):
    # Чтение и парсинг JSON-файлов
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))

    # Получаем все ключи из обоих файлов
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    # Формируем результат сравнения
    result = []
    for key in keys:
        if key not in data2:
            result.append(f"- {key}: {data1[key]}")
        elif key not in data1:
            result.append(f"+ {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"- {key}: {data1[key]}")
            result.append(f"+ {key}: {data2[key]}")
        else:
            result.append(f"  {key}: {data1[key]}")

    return "\n".join(result)
