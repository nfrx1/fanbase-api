import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fanbase-api",
    version="1.0.7",
    author="Kapom",
    author_email="aasionkj@gmail.com",
    description="The first fanbase package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nfrx1/FanBase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["requests"]
)
