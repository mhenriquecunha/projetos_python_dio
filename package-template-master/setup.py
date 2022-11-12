from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_mhc",
    version="0.0.1",
    author="Mauro_Henrique",
    author_email="oggimhc@gmail.com",
    description="Modelo aula Dio_Me",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhenriquecunha/projetos_python_dio.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)