from gendiff import generate_diff

diff = generate_diff('gendiff/file1.json', 'gendiff/file2.json')
print(diff)
