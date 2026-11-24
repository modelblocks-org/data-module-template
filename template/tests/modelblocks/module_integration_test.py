"""Test importing the module through Snakemake.

!!!!! DO NOT ERASE OR MODIFY !!!!!
PLEASE ENSURE THIS SET OF MINIMAL TESTS WORKS BEFORE PUBLISHING YOUR MODULE.
Contents may be updated in future template updates.
"""

import subprocess


def test_snakemake_all_failure(module_path):
    """The snakemake 'all' rule should return an error by default."""
    process = subprocess.run(
        "snakemake --cores 1", shell=True, cwd=module_path, capture_output=True
    )
    assert "INVALID" in str(process.stderr)


def test_snakemake_integration_testing(module_path):
    """Run a light-weight test simulating someone using this module."""
    assert subprocess.run(
        "snakemake --use-conda --cores 1  --forceall",
        shell=True,
        check=True,
        cwd=module_path / "tests/modelblocks/integration",
    )
