import argparse


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

    # Здесь можно добавить логику сравнения файлов
    print(f'Comparing files: {args.first_file} and {args.second_file}')
    print(f'Output format: {args.format}')


if __name__ == '__main__':
    main()
