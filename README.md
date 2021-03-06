## TESA

[![DOI](https://zenodo.org/badge/179812040.svg)](https://zenodo.org/badge/latestdoi/179812040)

This is a short descritpion of how to use the T-ESA (Twitter-Easy Sentiment Analysis)
package for conducting some sentiment analysis using a lexicon based approach.

Per **Default** the Hu and Liu lexicon is used (Hu & Liu, 2004; Liu et al., 2005) for the opinions.
In addition, for handling **emojis** the lexicon package (in **R**) based on work of Novak et al. (2015) is utilized. The data
can be accessed from this link:
https://rdrr.io/cran/lexicon/man/emojis_sentiment.html (see */TESA/lexicon/emojis/ for more details how to data was preprocessed with a R-Script
for usage in TESA).

However, users can also provide other lexicons as text-files (one for positive words
and one for negative ones) as well as another emoji lexicons (make sure to keep the column names and file structure).

Please see the provided example for more details.

The package works on single tweets that are expected to be provided as string variable.
It is capable of:

- **`cleaning the tweet`** (stop word and special character removal using a given list)

- using the **`Porter-Stemmer`** or a lemmanization routine (both taken from the **nltk** package) to ensure better matching betweens the words in the tweets and the lexicon

- simple **`negation handling`**

- interpretation of **`emojis`** and their sentiments using the work of Novak et al. (2015) and the **emoji** Python libary

**How to install it:**

run this statement on your command line:

```{bash}
pip install -i https://test.pypi.org/simple/ TESA
```

or if you want to build from source:

- download the project

- navigate to the folder containing the setup.py

- run pip3 install . (or pip3 install -e . to give access to all users of your local machine)

- in case you do not have administration rights use the --user specification for pip


**How to use it:**

Some example Python code and data can be found in the /Example directory of the Python package
that shows the usage of the API.

As almost mentioned you will have to install the nltk and emoji Python package as well.

**References**

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA

 Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
       and Comparing Opinions on the Web." Proceedings of the 14th 
       International World Wide Web conference (WWW-2005), May 10-14, 
       2005, Chiba, Japan.

Novak, P. K., Smailovic, J., Sluban, B., and Mozetic, I. "Sentiment of emojis."
       PLoS ONE 10(12). 2015, doi:10.1371/journal.pone.0144296 

Twitter-Easy Sentiment Analysis
-------------------------------
[![DOI](https://zenodo.org/badge/179812040.svg)](https://zenodo.org/badge/latestdoi/179812040)
