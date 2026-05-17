def deep_merge(dict1, dict2):
    """Recursively merges two dictionaries."""
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            deep_merge(dict1[key], value)
        else:
            dict1[key] = value
    return dict1

# Example usage:
config1 = {'a': 1, 'b': {'c': 2}}
config2 = {'b': {'d': 3, 'c': 4}}
merged_config = deep_merge(config1, config2)
print(merged_config)  # Output: {'a': 1, 'b': {'c': 4, 'd': 3}}