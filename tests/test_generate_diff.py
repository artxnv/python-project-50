from gendiff.scripts.generate_diff import generate_diff


def load_fixture(filename):
    """Загружает содержимое фикстуры из файла."""
    with open(f'tests/fixtures/{filename}', 'r') as file:
        return file.read()


def test_generate_diff():
    expected_output = load_fixture('expected_output.txt')

    diff = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    )

    print(f"Generated Diff:\n{diff}")
    print(f"Expected Output:\n{expected_output}")

    assert diff == expected_output
