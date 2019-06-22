# load the lexicon package that contains emojis and their sentiment
# the package description can be found here:
# https://rdrr.io/cran/lexicon/man/emojis_sentiment.html
# Copyright:
# 2015 - Department of Knowledge Technologies
# also see this paper: http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0144296&type=printable
# if not installed so far, install the "lexicon" package by running
# install.packages("lexicon")
require("lexicon")

# get the sentiment lexicon
df <- lexicon::emojis_sentiment
# unfortunately, the emojis are not encoded in valid Unicode
# therefore, some cleaning is necessary to convert to
# UTF-8 (hex) encoding
df$utf_8  <- gsub(">", "", gsub("<", "", df$byte))
#df$emoji <- df$utf_8.encode("utf-8")

# get the positive and negative emojis
pos <- df[df$polarity == "positive",]
neg <- df[df$polarity == "negative",]

# write to csv
write.csv2(pos, "positive_emojis.csv", quote=F)
write.csv2(neg, "negative_emojis.csv", quote=F)
