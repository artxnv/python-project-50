from gendiff.scripts.generate_diff import generate_diff


def load_fixture(filename):
    """Загружает содержимое фикстуры из файла."""
    with open(f'tests/fixtures/{filename}', 'r') as file:
        return file.read()


def test_generate_diff_json():
    expected_output = load_fixture('expected_output_json.txt')
    diff = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    )
    assert diff == expected_output


def test_generate_diff_yaml():
    expected_output = load_fixture('expected_output_yaml.txt')
    diff = generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml'
    )
    assert diff == expected_output
