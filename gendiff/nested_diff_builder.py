# gendiff/nested_diff_builder.py

def build_nested_diff_tree(file1_data, file2_data):
    diff = []
    
    def compare_dicts(d1, d2, path=''):
        keys = set(d1.keys()).union(set(d2.keys()))
        
        for key in sorted(keys):
            current_path = f"{path}.{key}" if path else key
            
            if key not in d1:
                diff.append({'key': current_path, 'value': d2[key], 'status': 'added'})
            elif key not in d2:
                diff.append({'key': current_path, 'value': d1[key], 'status': 'removed'})
            elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
                compare_dicts(d1[key], d2[key], current_path)
            elif d1[key] != d2[key]:
                diff.append({'key': current_path, 'value': d2[key], 'status': 'changed'})
            else:
                diff.append({'key': current_path, 'value': d1[key], 'status': 'unchanged'})
    
    compare_dicts(file1_data, file2_data)
    return diff
