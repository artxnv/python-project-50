from gendiff.scripts.generate_diff import generate_diff
from gendiff.formatters.stylish import format_stylish  # Импортируем нужный форматтер
from tests.fixtures import load_fixture

def test_generate_diff_json():
    expected_output = load_fixture('expected_output_json.txt')
    diff = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        format_stylish  # Передаем форматтер
    )
    assert diff == expected_output

def test_generate_diff_yaml():
    expected_output = load_fixture('expected_output_yaml.txt')
    diff = generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        format_stylish  # Передаем форматтер
    )
    assert diff == expected_output

def test_generate_diff_nested_json():
    expected_output = load_fixture('expected_output_nested_json.txt')
    diff = generate_diff(
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        format_stylish  # Передаем форматтер
    )
    assert diff == expected_output

def test_generate_diff_nested_yaml():
    expected_output = load_fixture('expected_output_nested_yaml.txt')
    diff = generate_diff(
        'tests/fixtures/nested_file1.yml',
        'tests/fixtures/nested_file2.yml',
        format_stylish  # Передаем форматтер
    )
    assert diff == expected_output