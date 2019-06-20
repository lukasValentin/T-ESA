#!/usr/bin/python3
from TESA import sentiment_analysis

# load the class and create an object
# per default the Hu and Liu opinion lexicon is used
# if you would like to provide another lexicon or a modified version
# please call the constructor the following way
# 
# analyzer = sentiment_analysis.lexicon_analysis(file_pos='your_positive_file.txt', file_neg='your_negative_file.txt')
#
# please note, that the structure of your text files must be exactly the same as in case of the
# default lexicon:
# no headerlines and just one word per line
analyzer = sentiment_analysis.lexicon_analysis()

# load the lexicon -> per default the Hu and Liu opinion lexicon is used
# if no lexicon is loaded then no analysis can be conducted!
analyzer.load_lexicon()

# check if the lexicons were loaded correctly:
print(analyzer.pos)
print(analyzer.neg)

# now you can analyse the sentiments
# per default lemmanization is used
# if you would like to use the Porter Stemmer change it to:
#
# sentinemt, score = analyzer.get_sentiment_per_tweet(tweet, lemmas=False, stemming=True)
#
tweet = 'Can you recommend anyone for this #job? LEAD FINAN APPL ANAYLST - https://t.co/NuUxy8QoGq #FacilitiesMgmt #Tifton, GA #Hiring #CareerArc'
sentiment, score = analyzer.get_sentiment_per_tweet(tweet)
print('Sentiment: ' + sentiment)
print('Score: ' + str(score))


