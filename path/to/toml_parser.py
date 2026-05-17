# Fix for Silent Failure in TOML Parsing

This commit improves error handling in the TOML parsing logic to ensure that errors are properly surfaced instead of failing silently.

## Changes:
- Updated the parsing logic to catch and report errors more effectively.
- Added unit tests to cover edge cases in TOML parsing.

This addresses issue #7.