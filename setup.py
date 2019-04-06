# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TESA (Twitter Easy Sentiment Analysis",
    version="0.0.1",
    author="Lukas Graf",
    author_email="graflukas@web.de",
    description="Simple sentiment analysis of single tweets using opinion lexicons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukasValentin/T-ESA",
    packages=setuptools.find_packages(
            "nltk"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
