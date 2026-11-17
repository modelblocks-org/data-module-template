"""Shared pytest fixtures."""

from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def module_path():
    """Parent directory of the project."""
    # If workflow tests need downloads, place them here.
    return Path(__file__).parents[2]
