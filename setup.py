import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rut_chile",
    version="2.0.0",
    author="Guillermo Valenzuela",
    author_email="gevalenz@gmail.com",
    description="Package for validating Chilean RUT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gevalenz/rut-chile",
    packages=setuptools.find_packages(),
    keywords="RUT Chile",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
