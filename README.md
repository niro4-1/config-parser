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

# Load configuration from a file
config.load('config.toml')

# Access values
value = config.get('section', 'key')
print(value)
```

This example demonstrates loading a TOML configuration file and accessing a specific value.

## Additional Examples

### Example 1: Loading YAML Configuration
```python
config.load('config.yaml')
```

### Example 2: Accessing Nested Values
```python
nested_value = config.get('section.subsection', 'key')
print(nested_value)
```

### Example 3: Handling Missing Keys
```python
try:
    value = config.get('section', 'missing_key')
except KeyError:
    print('Key not found!')
```

### Example 4: Environment Variable Interpolation
```python
config.load('config_with_env.toml')
```

This shows how to handle different configurations and error cases, enhancing clarity on usage.