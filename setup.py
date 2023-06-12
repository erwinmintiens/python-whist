from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="whist-score",
    version="0.1.0",
    author="Erwin Mintiens",
    author_email="erwin.mintiens@protonmail.com",
    license_files=("LICENSE",),
    description="whist-score is a scorekeeper for the whist card game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erwinmintiens/whist-score",
    py_modules=["whist", "main"],
    packages=find_packages(),
    install_requires=["click>=7.1.2", "colorama>=0.4.6"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        whist-score=main:main
    """,
    data_files=[
        (
            os.path.expanduser("~/.whist-score"),
            [
                "config/abondance_point_system.json",
                "config/game_types.json",
                "config/miserie_point_system.json",
                "config/solo_point_system.json",
                "config/troel_point_system.json",
                "config/vragen_en_meegaan_point_system.json",
            ],
        )
    ],
)
