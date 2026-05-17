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