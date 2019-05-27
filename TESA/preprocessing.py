# -*- coding: utf-8 -*-
"""
    @name:    preprocessing.py

    @author:  Lukas Graf
    
    @purpose: preprocesses tweets for sentiment analysis
              this includes:
                  * stop word removal
                  * special character removal
                  * lemmatization and stemming
                  * negation handling
              the program works on single tweets and returns
              a list of tweet tokens
"""
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# simple data cleaning
# -> stop-word, special character removal
def clean(tweet, language="english"): 
    """
    clean tweet text by removing links, special characters 
    using simple regex statements 
    """
    # convert to lower
    tweet = tweet.lower()
    # get the stop-words available from the nltk.corpus lib
    # as the corpus would haver also delete a lot of negations from the tweets
    # it is considered to use just a subset
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
                  'ourselves', 'you', "you're", "you've", "you'll",
                  "you'd", 'your', 'yours', 'yourself', 'yourselves',
                  'he', 'him', 'his', 'himself', 'she', "she's", 'her',
                  'hers', 'herself', 'it', "it's", 'its', 'itself',
                  'they', 'them', 'their', 'theirs', 'themselves', 'what',
                  'which', 'who', 'whom', 'this', 'that', "that'll",
                  'these', 'those', 'am', 'is', 'are', 'was', 'were',
                  'be', 'been', 'being', 'have', 'has', 'had', 'having',
                  'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
                  'if', 'or', 'because', 'as', 'until', 'while', 'of',
                  'at', 'by', 'for', 'with', 'about', 'against', 'between',
                  'into', 'through', 'during', 'before', 'after', 'above',
                  'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
                  'off', 'over', 'under', 'again', 'further', 'then', 'once',
                  'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
                  'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
                  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
                  'will', 'just',  'should', "should've", 'now', 'd', 'll',
                  'm', 'o', 're', 've', 'y', 'ain', 'ma', '.', ',', ';', '!', '?']
    
    # convert to string again as re expects a string-like object (and not a list)
    # remove all the stopwords as well as the numbers and words shorter than two letters
    # also check the spelling
    tmp = ""
    tmp_c = [tmp + item for item in tweet.split() if item not in stop_words and item.isalpha() and len(item) >= 2]
    tmp_c = ",".join(item for item in tmp_c)
    
    # remove other  special characters including @, URLs, Usernames and other special characters
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) M^|(\w+:\/\/\S+)", " ", tmp_c).split())
# end clean

# word stemming
# =============================================================================
def stem(token):
     """
     stems a tweet using the PorterStemmer algorithm
     """
     porter = PorterStemmer()
     token_stemed = [porter.stem(word) for word in token.split()]
     # return the stemmend token
     return token_stemed
# end stem

#=============================================================================
# lemmanization
def lemmanize(token):
     """
     finds the lemmans of words in a tweet
     """
     lemmanizer = WordNetLemmatizer()
     token_lemmanized = lemmanizer.lemmatize(token)
     # return the lemmanized token
     return token_lemmanized
# end lemmanize

#=============================================================================
# negation handling
def handle_negations(tweet_tokens, lexicon_scores):
    """
    Handling of negations occuring in tweets -> shifts meaning of words
    -> if a negation was found the polarity of the three following words will change
    """
    # new score list
    new_scores = lexicon_scores
    # Words defining negations
    # taken from https://github.com/gkotsis/negation-detection/blob/master/negation_detection.py
    # and Kolchyna et al. (2015)
    negations_adverbs = ["no", "without", "nil","not", "n't", "never", "none", "neith", "nor", "non",
                         "seldom", "rarely", "scarcely", "barely", "hardly", "lack", "lacking", "lacks",
                         "neither", "cannot", "can't", "daren't", "doesn't", "didn't", "hadn't",
                         "wasn't", "won't", "without", "hadnt", "haven't", "weren't"]
    
    negations_verbs = ["deny", "reject", "refuse", "subside", "retract", "non"]
    # find negations in the tweet_tokens list and change the scores of negative and positive tokens
    # immediatly following the negation
    index = 0
    for ii in range(len(tweet_tokens)):
        token = tweet_tokens[index]
        if (token in negations_adverbs or token in negations_verbs):
            # makle sure that the end of the tweet isn't reached yet
            if (index < len(tweet_tokens)-1):
                # if the sentiment of the next token is positive change it to negative
                if (lexicon_scores[index + 1] == 1):
                    new_scores[index + 1] = -1
                    index += 2
                # else change it to positive if it is negative
                elif (lexicon_scores[index + 1] == -1):
                    new_scores[index + 1] = 1
                    index += 2
                else:
                    index += 1
                # endif
            else:
                break
            # endif
        # if neutral let it neutral -> go to the next token
        else:
            index +=1
        # endif
            
        # exit the loop when all tokens have been checked
        if (index >= len(tweet_tokens)-1):
            break
        # endif
    # endfor
    # return the new scores
    return new_scores
# end handle_negations
