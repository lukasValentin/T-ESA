# T-ESA

This is a short descritpion of how to use the T-ESA (Twitter-Easy Sentiment Analysis)
package for conducting some sentiment analysis using a lexicon based approach.

Per **Default** the Hu and Liu lexicon is used (Hu & Liu, 2004; Liu et al., 2005).
However, users can also provide other lexicons as text-files (one for positive words
and one for negative ones).

The package works on single tweets that are expected to be provided as string variable.
It is capable of:

- cleaning the tweet (stop word and special character removal using a given list)
- using the Porter-Stemmer or a lemmanization routine (both taken from the nltk
package) to ensure better matching betweens the words in the tweets and the lexicon
- simple negation handling

As almost mentioned you will have to install the nltk Python package as well.

** References **
Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA

 Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
       and Comparing Opinions on the Web." Proceedings of the 14th 
       International World Wide Web conference (WWW-2005), May 10-14, 
       2005, Chiba, Japan.
=======
Twitter-Easy Sentiment Analysis
>>>>>>> b95fc32a6847cd65140649f93ac196a2eb8cab13
