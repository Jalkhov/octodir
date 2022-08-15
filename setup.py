import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist")
    os.system("twine upload dist/* --skip-existing")
    sys.exit()
elif sys.argv[-1] == "test":
    os.system("python setup.py sdist")
    os.system("twine upload -r testpypi dist/* --skip-existing")
    sys.exit()

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name='octodir',
    version="1.0.0",
    description="Tool for downloading directories from Github repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jalkhov/octodir",
    author="Pedro Torcatt",
    author_email="pedrotorcattsoto@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="github directory download",
    packages=["octodir"],
    include_package_data=True,
    python_requires=">=3.0",
    install_requires=open(
        os.path.join(here, "requirements.txt"), encoding="utf-8"
    )
    .read()
    .split("\n"),
    project_urls={
        "Bug Reports": "https://github.com/Jalkhov/octodir/issues",
        "Source": "https://github.com/Jalkhov/octodir/",
    },
    entry_points={"console_scripts": [
        "octodir=octodir.octodir_cli:octodir_cli"]},
)
