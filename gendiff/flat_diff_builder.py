def build_flat_diff_tree(file1_data, file2_data):
    diff = []
    keys = set(file1_data.keys()).union(set(file2_data.keys()))
    
    for key in sorted(keys):
        if key not in file1_data:
            diff.append({'key': key, 'value': file2_data[key], 'status': 'added'})
        elif key not in file2_data:
            diff.append({'key': key, 'value': file1_data[key], 'status': 'removed'})
        elif file1_data[key] != file2_data[key]:
            diff.append({'key': key, 'value': file2_data[key], 'status': 'changed'})
        else:
            diff.append({'key': key, 'value': file1_data[key], 'status': 'unchanged'})
    
    return diff
