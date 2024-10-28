import os

def load_fixture(filename):
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', filename), 'r') as file:
        return file.read()
