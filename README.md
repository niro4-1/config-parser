# config-parser
A repository for parsing configuration files.

## Important Note on TOML Parsing

When loading TOML files, be aware that parse failures may occur silently. If a file contains errors, the `ConfigParser` will skip the problematic sections without raising an exception. Always validate the configuration after loading to ensure it is correct and handle any missing keys appropriately.

### Additional Details on TOML Parsing

- **Error Handling**: Implement error handling to catch and log any issues during parsing.
- **Validation**: Consider adding a validation step after loading to check for required keys and expected data types.
- **Debugging**: Use logging to output the loaded configuration and any skipped sections for easier debugging.

This ensures that users are aware of potential pitfalls and can handle them effectively.

## New Feature

This section describes the new feature added in this branch.