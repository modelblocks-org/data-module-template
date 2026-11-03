"""Shared pytest fixtures."""

import tomllib
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def module_path():
    """Parent directory of the project."""
    # If your module needs files in resources/user/, place automated downloads here.
    return Path(__file__).parents[2]


@pytest.fixture(scope="module")
def pixi_platforms(module_path) -> list[str]:
    """Pixi platforms defined for this project."""
    with (module_path / "pixi.toml").open("rb") as pixi_config:
        return tomllib.load(pixi_config)["workspace"]["platforms"]
