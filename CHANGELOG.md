# Changelog

<!-- version list -->

## v2.11.2 (2026-06-22)

### Bug Fixes

- Keep strong reference to SingleShot delayed-action task
  ([#211](https://github.com/hvaclibs/nexia/pull/211),
  [`3510562`](https://github.com/hvaclibs/nexia/commit/3510562034f3287392e6ac45fb52883c12c2ca37))

### Build System

- Drop Python 3.9 support ([#213](https://github.com/hvaclibs/nexia/pull/213),
  [`b0c1526`](https://github.com/hvaclibs/nexia/commit/b0c1526b033b1c472b672b00d5343203b058da28))

- Migrate to poetry and drop tox ([#210](https://github.com/hvaclibs/nexia/pull/210),
  [`3e9e608`](https://github.com/hvaclibs/nexia/commit/3e9e6085ffab0213a1fa3576d2d17f8301a7dc9e))

### Chores

- **deps**: Bump mypy from 1.17.1 to 1.18.2 ([#184](https://github.com/hvaclibs/nexia/pull/184),
  [`78280f2`](https://github.com/hvaclibs/nexia/commit/78280f2f38ad37263379f9fd6ffc2e15e5950583))

- **deps**: Bump orjson from 3.11.3 to 3.11.4 ([#187](https://github.com/hvaclibs/nexia/pull/187),
  [`8718280`](https://github.com/hvaclibs/nexia/commit/8718280a2a0ce0c82a97fad50574f8c6973a6e35))

- **deps**: Bump pytest from 8.4.1 to 8.4.2 ([#177](https://github.com/hvaclibs/nexia/pull/177),
  [`4c06ba7`](https://github.com/hvaclibs/nexia/commit/4c06ba77f77d3dada03a5859041f0b79c030c277))

- **deps**: Bump pytest-asyncio from 1.1.0 to 1.2.0
  ([#181](https://github.com/hvaclibs/nexia/pull/181),
  [`0e57505`](https://github.com/hvaclibs/nexia/commit/0e57505fb95db68c3ea66178aea39787a298cef6))

- **deps**: Bump tox from 4.28.4 to 4.30.2 ([#176](https://github.com/hvaclibs/nexia/pull/176),
  [`0ee54b6`](https://github.com/hvaclibs/nexia/commit/0ee54b6ee8888e8bcbe3780b667b4785afff4787))

- **deps**: Bump tox from 4.30.2 to 4.30.3 ([#186](https://github.com/hvaclibs/nexia/pull/186),
  [`d7e40a2`](https://github.com/hvaclibs/nexia/commit/d7e40a2550385e33d58c8fd480435fd52dc0d575))

- **deps-ci**: Bump the github-actions group across 1 directory with 4 updates
  ([#189](https://github.com/hvaclibs/nexia/pull/189),
  [`98a1cf9`](https://github.com/hvaclibs/nexia/commit/98a1cf97f54d3849e54c7e33325237fd3b116d09))

- **deps-ci**: Bump the github-actions group with 2 updates
  ([#175](https://github.com/hvaclibs/nexia/pull/175),
  [`6f1d3ec`](https://github.com/hvaclibs/nexia/commit/6f1d3ec005b69e403061e1861199bef8611865a9))

- **deps-dev**: Bump coverage from 7.10.6 to 7.10.7
  ([#183](https://github.com/hvaclibs/nexia/pull/183),
  [`9d8430c`](https://github.com/hvaclibs/nexia/commit/9d8430c43084e9f034747c7eedb628e152625f6a))

- **deps-dev**: Bump pip from 25.2 to 26.0 ([#190](https://github.com/hvaclibs/nexia/pull/190),
  [`3fab240`](https://github.com/hvaclibs/nexia/commit/3fab24029b34b5ef5004bcc8451bf64451d245bd))

- **deps-dev**: Bump twine from 6.1.0 to 6.2.0 ([#178](https://github.com/hvaclibs/nexia/pull/178),
  [`282ec73`](https://github.com/hvaclibs/nexia/commit/282ec7320cd0a415b6bc2daf02f196f15ff784ee))

- **deps-dev**: Bump wheel from 0.45.1 to 0.46.2
  ([#191](https://github.com/hvaclibs/nexia/pull/191),
  [`742e48e`](https://github.com/hvaclibs/nexia/commit/742e48ecde48c8181a7e48191464c58e89a6c6d1))

- **pre-commit.ci**: Pre-commit autoupdate ([#196](https://github.com/hvaclibs/nexia/pull/196),
  [`58f3191`](https://github.com/hvaclibs/nexia/commit/58f31917f7bb88cf09dad9e350d877b1146161d2))

- **pre-commit.ci**: Pre-commit autoupdate ([#182](https://github.com/hvaclibs/nexia/pull/182),
  [`3a53d82`](https://github.com/hvaclibs/nexia/commit/3a53d82cd229b372dc290b8f1b718d80c90c25ff))

- **pre-commit.ci**: Pre-commit autoupdate ([#179](https://github.com/hvaclibs/nexia/pull/179),
  [`363dab8`](https://github.com/hvaclibs/nexia/commit/363dab8c92f54589799da2420c26bbb8a935adf2))

- **pre-commit.ci**: Pre-commit autoupdate ([#170](https://github.com/hvaclibs/nexia/pull/170),
  [`4c932f7`](https://github.com/hvaclibs/nexia/commit/4c932f7c3ace3d795beed205b77a6b2ad209b106))

### Continuous Integration

- Automate releases with python-semantic-release
  ([#215](https://github.com/hvaclibs/nexia/pull/215),
  [`3cb041d`](https://github.com/hvaclibs/nexia/commit/3cb041d743413dbc8bf70cea40c526d9896d0598))

- Use the release environment for trusted publishing
  ([#216](https://github.com/hvaclibs/nexia/pull/216),
  [`1733927`](https://github.com/hvaclibs/nexia/commit/17339278a4f277d3a404aeb3aa3875e1a309ace6))

### Testing

- Switch http mocking from aioresponses to aiointercept
  ([#214](https://github.com/hvaclibs/nexia/pull/214),
  [`103962d`](https://github.com/hvaclibs/nexia/commit/103962dd6b82d892f5d52f8502fa0dddea0a41b3))


## [0.9.3] - 2020-04-29

Add additional debug logging

## [0.9.2] - 2020-04-16

Add an option to specify the full path to the state file

## [0.9.1] - 2020-04-11

Always use the heat and cool temperature
when we get a heat, a cool, and a target temperature

Fixes the jumping band in homekit

Fix emergency heat

## [0.9.0] - 2020-04-11

Add support for XL824

Supported XL950, XL1050, XL824
Not supported XL624

## [0.8.2] - 2020-04-10

* Fix detection of emergency heat
* Check device type to exclude non-thermostats

## [0.8.1] - 2020-04-10

* Resolve unexpected error handling HTTP 304 status
