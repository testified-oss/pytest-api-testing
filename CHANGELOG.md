# Changelog

All notable changes to the Pytest API Testing Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2026-10-10

### Added
- `1d43b1e` feat(client): Add initial base API client
- `997af32` feat: Initial setup of pytest configuration
- `496defe` test(config): Add validator utils
- `7d93997` test(api): Add initial API tests
- `d214684` test(fixture): Add environment fixtures
- `d214684` test(config): Add dev/prod config
- `4a99084` test(env): Add initial config test
- `0da45b6` test: Add custom pytest.ini section

### Changed
- `d55ee0e` chore: Move files
- `8bda1a5` chore: Move gh docs
- `ca850469` chore: Add makefile scripts
- `d15deaf` chore(ci): Remove Python 3.9 from workflow matrix

### Fixed
- `5f958c8` fix(pytest): Remove stray [custom_section] in pytest.ini causing warning
- `751e7ef` fix: Cap requests at <2.33.0 for Python 3.9 compatibility
- `ae2b13a` fix: Cap pytest at <9.0 for Python 3.9 compatibility with pillow>=10.0.0
- `dbc9983` fix: Cap pillow to >=10.0.0 (12.3.0 requires Python >=3.10, fails 3.9 matrix)
- `784b373` fix: Upgrade pytest-html-reporter to >=0.2.10 to resolve CI failure
- `a5e74da` fix: Cap pytest at <9.0 to resolve CI failure with pytest-html-reporter
- `4706e91` fix: Cap urllib3 to >=1.26.15,<2.0.0 (2.8.0 requires Python >=3.10)

### Build and CI
- `ffb3447` ci: Add GitHub Actions workflow for automated testing
- `69293c9` ci: Re-run CI to verify pytest version fix

### Documentation
- `501a33f` docs: Update test info
- `eeb22ca` docs: Add gh docs

### Dependencies
- `c5e89e7` chore(deps): Bump pyjwt from 2.8.0 to 2.12.0
- `42bbc51` chore(deps): Bump requests from 2.32.4 to 2.33.0
- `633a2a5` chore(deps): Bump pytest from 7.4.0 to 9.0.3
- `67d938e` chore(deps): Bump pillow from 12.1.1 to 12.2.0
- `3f24b67` chore(deps): Bump requests from 2.31.0 to 2.32.4
- `08171e8` chore(deps): Bump urllib3 from 2.3.0 to 2.5.0
- `6dee2c1` chore(deps): Bump urllib3 from 2.5.0 to 2.6.3
- `bdd0297` chore(deps): Bump pillow from 11.1.0 to 12.1.1
- `8de3aae` chore(deps): Bump requests from 2.32.4 to 2.33.0
- `ce5ddf0` chore(deps): Bump pyjwt from 2.8.0 to 2.12.0
- `a653401` chore(deps): Bump idna from 3.10 to 3.15
- `6ca8329` chore(deps): Bump urllib3 from 2.6.3 to 2.7.0
- `bd012b0` chore(deps): Bump pillow from 12.2.0 to 12.3.0
- `8387070` chore(deps): Bump pyjwt from 2.13.0 to 2.15.0
- `8fcb15d` chore(deps): Bump urllib3 from 2.7.0 to 2.8.0

### Removed
- `7f8d750` chore: Init directories