def resolve_to_string(value):
    if value is None:
        result = 'null'
    elif isinstance(value, bool):
        result = 'true' if value else 'false'
    else:
        result = str(value)
    return result
