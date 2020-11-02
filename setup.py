# made with help of https://realpython.com/pypi-publish-python-package/#a-small-python-package

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flexpy",
    version="0.0.2",
    description="Python API for SIL FieldWorks Language Explorer (FLEx)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Kuhron/flexpy",
    author="Wesley Kuhron Jones",
    author_email="wesleykuhronjones@gmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["flexpy"],
    include_package_data=True,
    # install_requires=["feedparser", "html2text"],
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)

