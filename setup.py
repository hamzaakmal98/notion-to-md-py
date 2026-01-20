from setuptools import setup, find_packages
import os

# Ensures the long description is pulled from your README
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="notion-to-md-py", 
    version="0.1.4",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "httpx",
        "pytablewriter",
        "notion-client",
    ],
    extras_require={
        "async": [
            "asyncio",
        ]
    },
    description="A package to convert Notion content into Markdown format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hamzaakmal98/notion-to-md-py",
    author="hamzaakmal98",
    author_email="hamzaakmal98@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="notion markdown converter python",
    project_urls={
        "Bug Tracker": "https://github.com/hamzaakmal98/notion-to-md-py/issues",
        "Source Code": "https://github.com/hamzaakmal98/notion-to-md-py",
    },
)
