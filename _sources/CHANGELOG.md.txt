# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2020-05-01

### Added

- Add logging support to the application. [#10]

### Fixes

- Fix the stack lookup problem where all the stacks were loaded instead of only the
  stacks of a specific project. [#11]

## [0.2.0] - 2020-04-26

### Added

- Add support to handle multiple stacks in one project. [#8]

### Fixes

- Ignore empty `yml` files. [#8]

## [0.1.0] - 2020-04-22

First usable version of the project.

[//]: # (Release links)
[0.1.0]: https://github.com/rgreinho/tfpy/releases/tag/0.1.0
[0.2.0]: https://github.com/rgreinho/tfpy/releases/tag/0.2.0
[0.3.0]: https://github.com/rgreinho/tfpy/releases/tag/0.3.0

[//]: # (Issue/PR links)
[#8]: https://github.com/rgreinho/tfpy/pull/8
[#10]: https://github.com/rgreinho/tfpy/pull/10
[#11]: https://github.com/rgreinho/tfpy/pull/11
