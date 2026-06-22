"""General pytest fixtures."""

from pathlib import Path

import pytest
import yaml


@pytest.fixture(scope="session")
def template_path() -> Path:
    """Location of the template."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def simple_answers(template_path) -> dict:
    """Generic template answers."""
    with open(template_path / "tests/utils/simple_answers.yaml") as file:
        simple_answers = yaml.safe_load(file)
    return simple_answers
