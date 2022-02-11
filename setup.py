import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pandas_geojson",
    version="1.0.0",
    description="Convert Pandas Dataframe to GeoJSON",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jaycroft/pandas-geojson",
    author="Jay",
    author_email="datacraftsmansguild@gmail.com",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["pandas_geojson"],
    include_package_data=True,
    install_requires=["pandas"],
)
