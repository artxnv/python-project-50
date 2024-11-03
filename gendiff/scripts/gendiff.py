import argparse
from gendiff.scripts.generate_diff import generate_diff
from gendiff.formatters.stylish import format_stylish

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first configuration file')
    parser.add_argument('second_file', help='Path to the second configuration file')
    parser.add_argument('-f', '--format', help='Set format of output', default='stylish')

    args = parser.parse_args()

    formatter = format_stylish if args.format == 'stylish' else None
    diff = generate_diff(args.first_file, args.second_file, formatter)
    print(diff)

if __name__ == '__main__':
    main()
