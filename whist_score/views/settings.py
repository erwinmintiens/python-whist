def adjust_points():
    pass


def flatten_json(data, prefix=""):
    flattened_data = {}
    for key, value in data.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, new_key))
        else:
            flattened_data[new_key] = value
    return flattened_data
