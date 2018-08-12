# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Function to format RUT

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