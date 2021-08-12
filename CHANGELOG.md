# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.1] - 2021-08-12
### Added
- fixes rut formatting functions for inputs containing dash

## [2.0.0] - 2018-12-26
### Added
- format_rut function to get a well formatted RUT
- get_capitalized_verification_digit to get capitalized verification digit
- format_rut_with_dots to get RUT with thousands separator
- format_capitalized_rut_with_dots to get RUT with thousands separator and capitalized
- format_rut_without_dots to get RUT with dash only
- format_capitalized_rut_without_dots to get RUT with dash only and capitalized
### Changed
- functions raise ValueError when input is invalid
- get_verification_digit doesn't accept capitalize flag anymore
- refactoring of code
### Removed
- format_rut removed and replaced

## [1.2.0] - 2018-08-12
### Added
- format_rut function to get a well formatted RUT
### Changed
- functions return None when input is invalid

## [1.1.0] - 2018-08-12
### Changed
- get_verification_digit function can return capital K depending on the input flag

## [1.0.0] - 2018-08-11
### Added
- rut_chile module
- is_valid_rut function to check if a given RUT is valid
- get_verification_digit function to generate the verification digit of a given RUT
- CHANGELOG to keep track of changes
- .travis.yml configuration file
- requirements.txt