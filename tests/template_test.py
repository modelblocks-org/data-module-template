"""Test a simplified template use-case."""

import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
from copier import run_copy


class TestBuiltTemplate:
    """Build and check the resulting template."""

    @pytest.fixture(scope="class", params=["Apache-2.0"])
    def template_project(
        self, request, tmp_path_factory, template_path, simple_answers
    ):
        """Run the template in a temporary location, for further testing."""
        path = tmp_path_factory.mktemp(request.param)
        modified_answers = deepcopy(simple_answers)
        modified_answers.update(license=request.param)
        run_copy(
            src_path=str(template_path),
            dst_path=str(path),
            data=modified_answers,
            vcs_ref="HEAD",  # Use the latest version for the test
        )
        return path

    @pytest.fixture(scope="class")
    def pixi_built(self, template_project):
        """Create a pixi environment for the temporary template project."""
        pixi_config = template_project / "pixi.toml"
        subprocess.run(
            f"pixi install --manifest-path {pixi_config}",
            shell=True,
            cwd=template_project,
            check=True,
        )
        subprocess.run(
            "pixi run export-snakemake-env module",
            shell=True,
            cwd=template_project,
            check=True,
        )
        return template_project

    def test_task_test_integration(self, pixi_built):
        """The template's tests should pass by default."""
        assert subprocess.run(
            "pixi run test-integration", shell=True, check=True, cwd=pixi_built
        )

    def test_task_export_snakemake_env(self, pixi_built):
        """The template's export task should work as expected."""
        assert subprocess.run(
            "pixi run export-snakemake-env module",
            shell=True,
            check=True,
            cwd=pixi_built,
        )

    def test_linting(self, pixi_built):
        """The generated project should result in perfect snakemake linting."""
        assert subprocess.run(
            "pixi run snakemake --lint", shell=True, check=True, cwd=pixi_built
        )

    def test_github_issue_templates(self, template_path: Path, template_project: Path):
        """The issue templating and configuration should match at both levels."""
        issue_template_dir = Path(".github/ISSUE_TEMPLATE")
        repo_path = template_path / issue_template_dir
        temp_path = template_project / issue_template_dir

        repo_files = sorted(path.relative_to(repo_path) for path in repo_path.iterdir())
        temp_files = sorted(path.relative_to(temp_path) for path in temp_path.iterdir())
        assert temp_files == repo_files

        for relative_path in repo_files:
            repo_file = repo_path / relative_path
            generated_file = temp_path / relative_path

            assert repo_file.is_file()
            assert generated_file.is_file()
            assert generated_file.read_text() == repo_file.read_text()
