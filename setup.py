from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

__pkg_name__ = "purple-lemon-base"
__version__ = "0.0.1"

#test_requires = ["pytest","coverage"]

setup(
    name=__pkg_name__,
    version=__version__,
    long_description=long_description,
    packages=find_packages(where="src/main", include=['purple_lemon_base.*']),
    package_dir={"": "src/main"},
    url='https://github.com/maumaugithub/purple-lemon-base',
    install_requires=[
        "dataclasses",
        "python-semantic-release"
    ],
    extras_require={  
        "test": ["pytest"],
    },
)