#!/usr/bin/python3
from TESA import sentiment_analysis
import pandas as pd

def get_texts (df, analyzer):
    
    res = df["text"].apply(lambda x: analyzer.get_sentiment_per_tweet(x))
    sentiments = [x[0] for x in res]
    scores = [x[1] for x in res]
    df["sentiments"] = sentiments
    df["scores"] = scores
    outfile = "sentiments.csv"
    df.to_csv(outfile, sep=";")

if __name__ == '__main__':
    

    analyzer = sentiment_analysis.lexicon_analysis ()
    analyzer.load_lexicon ()
    df = pd.read_csv(r"nyc_tweets.csv")
    get_texts(df, analyzer)

    
