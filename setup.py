import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartlens", # Replace with your own username
    version="1.0.0",
    author="SmartLens Technologies, Inc.",
    author_email="michael@smartlens.ai",
    description="A Python library for the SmartLens API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SmartLens/smartlens-python/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
