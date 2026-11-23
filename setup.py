
from pathlib import Path
from typing import List

from setuptools import find_packages, setup


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Read external package dependencies without treating comments or -e . as packages."""
    requirements_path = Path(__file__).resolve().parent / file_path
    requirements: List[str] = []

    with requirements_path.open(encoding="utf-8") as file_obj:
        for line in file_obj:
            requirement = line.strip()
            if requirement and not requirement.startswith("#") and requirement != HYPHEN_E_DOT:
                requirements.append(requirement)

    return requirements


setup(
    name="mlops_project_no_03",
    version="0.0.1",
    author="Babar Ali Khan",
    author_email="babaralikhanaiexpert098@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
