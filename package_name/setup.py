from setuptools import setup, find_packages

with open("../README.md", "r") as f:
    page_description = f.read()

with open("../requirements.txt") as f:
    requeriments = f.read().splitlines()

setup(
    name = "desafios_dio-package",
    version = "0.0.1",
    author = "Lucio Flavio",
    author_email = "lucius.mat@gmail.com",
    description = "Desafios de Python-DIO",
    long_description = "page_description",
    long_description_content_type = "text/markdown",
    url = "",
    packages = find_packages(),
    install_requires = requeriments,
    python_requires = ">=3.8",
)