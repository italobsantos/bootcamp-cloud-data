from unicodedata import name
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requeriments.txt") as f:
    requirements = f.read().splitlines()

setup(
    name= "image_processing",
    version = "0.0.1",
    author= "Karina",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/italobsantos/bootcamp-cloud-data/tree/master/treinamento-python/projeto-gerenciamento-pacotes/image-processing-package",
    packages=find_packages(),
    install_requires=requeriments,
    python_requires='>=3.5',
)