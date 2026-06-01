# config-parser

A lightweight library for parsing layered configuration files (TOML/YAML/env).

## Installation

Install the library using pip:

```bash
pip install config-parser
```

## Usage

Here's how to use the library:

```python
from config_parser import ConfigParser

# Create a ConfigParser instance
config = ConfigParser()

# Load configuration from a TOML file
config.load('config.toml')

# Access a specific value
value = config.get('section', 'key')
print('Value from TOML:', value)
```

This example shows loading a TOML file and accessing a value.

## Additional Examples

### Example 1: Loading a YAML Configuration File
```python
# Load configuration from a YAML file
config.load('config.yaml')
```

### Example 2: Accessing Nested Values
```python
# Access a nested value
nested_value = config.get('section.subsection', 'key')
print('Nested Value:', nested_value)
```

### Example 3: Handling Missing Keys
```python
# Attempt to access a potentially missing key
try:
    value = config.get('section', 'missing_key')
    print('Value:', value)
except KeyError:
    print('Key not found! Check your configuration for accuracy.')
```

### Example 4: Loading Configuration with Environment Variable Interpolation
```python
# Load configuration with environment variables
config.load('config_with_env.toml')
print('Config with Env:', config.get('section', 'key'))
```

## Important Note on TOML Parsing

When loading TOML files, errors may occur silently. The `ConfigParser` skips problematic sections without raising exceptions. Always validate your configuration after loading to ensure correctness and handle missing keys appropriately.