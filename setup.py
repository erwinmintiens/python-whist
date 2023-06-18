import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


class InstallCommand(install):
    def run(self):
        install.run(self)

        if sys.platform.startswith("win"):
            save_files_dir = os.path.join(get_python_lib(), ".whist_score", "saves")
        else:
            save_files_dir = os.path.join(
                os.path.expanduser("~"), ".whist_score", "saves"
            )

        os.makedirs(save_files_dir, exist_ok=True)
        print(f"Created directory: {save_files_dir}")


setup(
    name="whist-score",
    version="0.3.6",
    author="Erwin Mintiens",
    author_email="erwin.mintiens@protonmail.com",
    license_files=("LICENSE",),
    description="whist-score is a scorekeeper for the colour whist card game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erwinmintiens/whist-score",
    py_modules=["whist_score", "main"],
    packages=find_packages(),
    package_data={"whist_score": ["config/*.json"]},
    install_requires=["click>=7.1.2", "tabulate>=0.9.0"],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        whist-score=main:main
    """,
    cmdclass={
        "install": InstallCommand,
    },
)
