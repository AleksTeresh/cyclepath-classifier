import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cyclepath-classifier",
    version="0.2.1",
    description="A command-line tool for automatically calculating round complexity of LCL problems in cycles and paths based on their description in the node-edge-checkable formalism",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AleksTeresh/cyclepath-classifier",
    author="Aleksandr Tereshchenko",
    author_email="aleksandr.tereshch@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cyclepath_classifier"],
    include_package_data=True,
)
