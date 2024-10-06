import argparse
from gendiff.scripts.generate_diff import generate_diff  # Правильный импорт

def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Определение позиционных аргументов
    parser.add_argument(
        'first_file',
        help='Path to the first configuration file'
    )
    parser.add_argument(
        'second_file',
        help='Path to the second configuration file'
    )

    # Определение опции --format
    parser.add_argument(
        '-f', '--format',
        help='Set format of output (plain or json)',
        default='plain'
    )

    # Обработка аргументов
    args = parser.parse_args()

    # Вызов функции для сравнения файлов и вывод результата
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()
