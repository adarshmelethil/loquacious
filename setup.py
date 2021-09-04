#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="loquacious",
    version="0.1",
    description="Have a response to anything",
    url="https://github.com/adarshmelethil/loquacious",
    download_url="",
    license="MIT",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    author="Adarsh Melethil",
    author_email="adarshmelethil@gmail.com",
    install_requires=["docopt==0.6.2", "requests==2.26.0"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["loquacious=loquacious.cli:main"]},
)
