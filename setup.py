from setuptools import setup, find_packages

setup(
    name="pystringutils",
    version="0.1.0",
    author="Raees Fatima",
    description="Handy string utilities for Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
