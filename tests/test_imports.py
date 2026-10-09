"""Smoke test: every module in src/ imports with the locked dependencies.

Catches missing dependencies, import errors and incompatible dependency updates
before they reach the pipeline workflows.
"""
import importlib
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"

# app.py is a Streamlit script that renders the page when it is imported
EXCLUDED = {"__init__", "app"}

MODULES = sorted(path.stem for path in SRC_DIR.glob("*.py") if path.stem not in EXCLUDED)


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module: str) -> None:
    """Imports a module from src/ to verify that it and its dependencies load.

    Args:
        module: Name of the module, importable because src/ is on the pytest path.
    """
    importlib.import_module(module)
