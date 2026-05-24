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

## Silent TOML Parse Failures

When loading TOML files, it's important to be aware that parse failures may occur silently. If a file contains errors, the `ConfigParser` will not raise an exception but will instead skip the problematic sections. To ensure that your configuration is loaded correctly, always validate the configuration after loading and handle any missing keys appropriately.
