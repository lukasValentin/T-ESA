# -*- coding: utf-8 -*-
import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setuptools.setup(
    name="TESA",
    version="0.0.2",
    author="Lukas Graf",
    author_email="graflukas@web.de",
    description="Simple sentiment analysis of single tweets using opinion and emoji lexicons",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lukasValentin/T-ESA",
    packages=setuptools.find_packages(
            "nltk", "emoji"),
    include_package_data=True,
    package_data={'TESA': ['/TESA/lexicon/opinions/*.txt', '/TESA/lexicon/emojis/*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
