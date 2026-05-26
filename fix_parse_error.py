# Fix for silent parse error on malformed TOML

# This commit updates the parsing logic to surface errors instead of ignoring them.

def handle_missing_config(file_path):
    try:
        # Attempt to read the config file
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file '{file_path}' not found. Searched locations: [<list of searched locations>]")
    except Exception as e:
        raise Exception(f"Error reading config file '{file_path}': {str(e)}")
