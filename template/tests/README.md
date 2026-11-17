# Test setup

These are arranged in three different directories.

- `modelblocks`: standard tests that every Modelblocks module should have.
  Should be run on the `default` environment.
    - `convention_test.py`: validates the project against the [Modelblocks Convention](https://modelblocks.readthedocs.io/en/stable/).
    - `module_integration_test.py`: validates that the `Snakemake` workflow can be exported as a module.
- `unit`: for the development of unit tests of python scripts in `workflow/scripts`.
  Should be run on the `unit-test` environment.
- `workflow`: for the development of workflow level tests.
  Should be run on the `default` environment.

## Continuous integration

By default, only `modelblocks` and `unit` are run during Github CI testing during [pull requests](./../.github/workflows/pr-ci.yml).
