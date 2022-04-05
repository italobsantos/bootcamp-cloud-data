from unicodedata import name
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requeriments.txt") as f:
    requeriments = f.read().splitlines()

setup(
    name= "am_modulation",
    version = "0.0.1",
    author= "Italo",
    description="Simple AM modulator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/italobsantos/bootcamp-cloud-data/tree/master/treinamento-python/projeto-gerenciamento-pacotes/simple-am-modulator-package",
    packages=find_packages(),
    install_requires=requeriments,
    python_requires='>=3.5',
)