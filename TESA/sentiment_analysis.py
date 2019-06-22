# -*- coding: utf-8 -*-
"""
Sentiment_Analysis
==================

@author: Lukas Graf, February-June 2019

This module contains a class "lexicon_analysis" for conducting basic sentiment
analysis of tweets in English language using the Hu and Liu
opinion lexicon. Based on the identified polarity of the message, a sentiment
score is calculated that is translated into "negative" if the score is smaller
equal -2 and "positive" if the score is greater equal +2. Scores between that
limits are marked as "neutral".

The results are: 

- sentiment ('negative', 'neutral', 'positive')

- sentiment score as integer (thus, you can also modify the bounds for the sentiment categories)

"""
from TESA.preprocessing import clean, handle_negations, lemmanize, stem
import pkg_resources
import pandas as pd
import codecs
from itertools import chain
import emoji
import functools
import operator

class lexicon_analysis:
    """
    Class for analysing the sentiment of tweets using an Opinion lexicon
    """

    # class constructor -> empty list for the lexicon
    # and the path to the two text files containing the lexicon
    # per default the Hu and Liu lexicon is loaded
    def __init__(self, file_pos=None, file_neg=None,
                 emojis_pos=None, emojis_neg=None):
        """
        the class constructor
        """
        if (file_pos is None and file_neg is None):
            # path to the opinion lexicon
            DATA_PATH = pkg_resources.resource_filename('TESA',
                                                        '/lexicon/opinions/')
            file_pos = DATA_PATH + 'positive.txt'
            file_neg = DATA_PATH + 'negative.txt'
            # path to the emoji lexicon
            DATA_PATH = pkg_resources.resource_filename('TESA',
                                                        '/lexicon/emojis/')
            file_e_pos = DATA_PATH + 'positive_emojis.csv'
            file_e_neg = DATA_PATH + 'negative_emojis.csv'
            

        self.pos, self.neg = [], []
        self.file_pos = file_pos
        self.file_neg = file_neg
        self.file_e_pos = file_e_pos
        self.file_e_neg = file_e_neg


    def load_lexicon(self):
        """
        loads the Liu and Wang sentiment lexicon as well as the emoji-lexicon
        (or any other user-defined lexicon)
        and return two lists containing the opionion lexicon derived
        words as well as the emojis

    	 Parameters
        -------
        None

    	 Returns
        -------
        pos, neg : String
    		 loaded opinion lexicon
        """
        # read in the data
        # opionion lexicon first
        with open(self.file_pos) as positives:
            self.pos = positives.readlines()
            self.pos = [item.replace("\n","") for item in self.pos]
        with open(self.file_neg) as negatives:
            self.neg = negatives.readlines()
            self.neg = [item.replace("\n","") for item in self.neg]
        # read in the emojis (utf-8 representation)
        # use read_emoji_lexicon method and append to the opionion lexicon
        self.pos = list(chain(self.pos,
                              self.read_emoji_lexicon(self.file_e_pos)))
        self.neg = list(chain(self.neg,
                              self.read_emoji_lexicon(self.file_e_neg)))      
    # end load_lexicon


    @staticmethod
    def read_emoji_lexicon(fname):
        """
        reads in the emoji lexicon stored as csv files and extracts the
        utf-8 representation of the emojis
        
        Parameters
        ----------
        fname : String
            filename (path + filename) of emoji-lexicon as csv
        
        Returns
        -------
        emojis : List-like
            emojis as UTF-8 representation
        """
        df = pd.read_csv(fname, sep=";")
        # convert from utf-8 hex to utf-8
        df['emoji'] = df['utf_8'].apply(lambda x: codecs.decode(x, "hex").decode('utf-8'))
        return df['emoji'].to_list()


    # setup a method for counting the matches between a given tweet
    # and the words stored in the lexicon
    # count positive and negative words
    def find_token_matches(self, tweet_tokens):
        """
        calculates the occurence of positive and negative words
        in a given tweet and returns a list of assigned scores
        +1 means that a token is positive, -1 that a token is 
        negative, 0 that the token was not found in the lexicon

	    Parameters
	    ----------
	    tweet_tokens : List
		     list of preprocessed Tweet tokens (cleaning, etc.)

	    Returns
	    -------
	    scores : List
		    list of scores (sentiment values) derived from matches
		    between the tokenized tweets and the opinion lexicon
        """
        scores = []
        token_pos = 1
        token_neg = -1
        token_neutral = 0
        
        # sometimes one token holds more than one emoji -> these need
        # to split too by using the emoji Python library
        tmp = []
        for ii in range(len(tweet_tokens)):
            token = tweet_tokens[ii]
            if emoji.emoji_count(token) <= 1:
                tmp.append(token)
                continue
            emoji_tokens = self.split_mutliple_emojis(token)
            tmp = list(chain(tmp, emoji_tokens))
        

        # loop over the tokens in a tweet and assign the sentiment
        # depending on the match to the lexicon -> it is necessary to
        # call the load_lexicon method first
        for token in tweet_tokens:
            if (token in self.pos):
                scores.append(token_pos)
            elif (token in self.neg):
                scores.append(token_neg)
            else:
                scores.append(token_neutral)
            # endif
        # endfor
        return scores
    # end find_token_matches
    
    
    @staticmethod
    def split_mutliple_emojis(emoji_token):
        """
        splits a token containing multiple tokens into
        single emojis
        """
        splitted = emoji.get_emoji_regexp().split(emoji_token)
        splitted = [sub.split() for sub in splitted]
        return functools.reduce(operator.concat, splitted)


    @staticmethod
    def get_overall_scores(token_scores):
        """
        returns the number of positive and negative scores in a tweet

	    Parameters
	    ----------
	    token_scores : List
		     list of sentiment scores for a tokenized tweet

	    Returns
	    -------
	    num_pos, num_neg : Integer
		      number of positive and negative sentiment scores per tokenized tweet
        """
        num_pos = token_scores.count(1)
        num_neg = token_scores.count(-1)
        return num_pos, num_neg
    # end get_overall_scores


    def get_sentiment_per_tweet(self, tweet, lemmas=True, stemming=False):
    	"""
    	there is a textblob build in method for classifying Tweets according to their
    	Sentiment -> the method returns a polarity score between -1 and 1 that is converted
    	into a sentiment label ("negative", "positive", "neutral") that is returned
    	in addition, also a subjectivity score is available (between 0 and 1) ranking from
    	objective (zero) to subjective (1)
    	"""

    	# Firstly, the Twitter data should be cleaned -> see function above
    	tweet_cleaned = clean(tweet)
    	# create tokens out of the tweet
    	tweet_tokens = tweet_cleaned.split()

    	# next, the tweets are lemmanized or stemmed
    	if (stemming):
            tweet_tokens = [stem(token) for token in tweet_tokens]
        # endif
    	if (lemmas):
            tweet_tokens = [lemmanize(token) for token in tweet_tokens]
        # endif

    	# calculate the sentiment score based on the opinion lexicon by Hu and Liu
    	# therefore, the find_token_matches method of this class is used
    	scores = self.find_token_matches(tweet_tokens)
    	# negation handling
    	scores_token = handle_negations(tweet_tokens, scores)
    	# count the scores
    	pos, neg = self.get_overall_scores(scores_token)
    	# calculate the difference between the number of positive and negative words
    	sentiment_score = pos - neg

    	# bounds for assigning a sentiment as positive or negative or neutral
    	# based on the paper by Kovacs-Gyori et al. 2018
    	bound_positive = 2
    	bound_negative = -2

    	# just query the score and assign the sentiment
    	if sentiment_score <= bound_negative:
    		sentiment = "negative"

    	elif sentiment_score >= bound_positive:
    		sentiment = "positive"

    	else:
    		sentiment = "neutral"

    	# endif
    	# return the sentiment and the sentiment_score
    	return sentiment, sentiment_score
    # end get_sentiment_per_tweet

# end class
