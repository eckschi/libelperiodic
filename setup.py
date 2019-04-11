import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ElPeriodic",
    version="1.0",
    author="Maksym Sobolyev",
    author_email="sobomax@gmail.com",
    description="Phase-locked userland scheduling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sobomax/libelperiodic'",
    packages=["elperiodic"], #setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


