# config-parser

A lightweight library for parsing layered configuration files (TOML/YAML/env).

## Installation

You can install the library using pip:

```bash
pip install config-parser
```

## Usage

Here's a simple example of how to use the library:

```python
from config_parser import ConfigParser

# Create a ConfigParser instance
config = ConfigParser()

# Load configuration from a TOML file
config.load('config.toml')

# Access a specific value from the configuration
value = config.get('section', 'key')
print('Value from TOML:', value)
```

This example demonstrates loading a TOML configuration file and accessing a specific value.

## Additional Examples

### Example 1: Loading a YAML Configuration File
```python
# Load configuration from a YAML file
config.load('config.yaml')
```

### Example 2: Accessing Nested Values in Configuration
```python
# Access a nested value from the configuration
nested_value = config.get('section.subsection', 'key')
print('Nested Value:', nested_value)
```

### Example 3: Handling Missing Keys Gracefully
```python
# Attempt to access a key that may not exist
try:
    value = config.get('section', 'missing_key')
    print('Value:', value)
except KeyError:
    print('Key not found! Please check your configuration.')
```

### Example 4: Loading Configuration with Environment Variable Interpolation
```python
# Load configuration that includes environment variables
config.load('config_with_env.toml')
print('Config with Env:', config.get('section', 'key'))
```

## Important Note on TOML Parsing

When loading TOML files, be aware that parse failures may occur silently. If a file contains errors, the `ConfigParser` will skip the problematic sections without raising an exception. Always validate the configuration after loading to ensure it is correct and handle any missing keys appropriately.