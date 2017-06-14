#---Import libraries---#
import seaborn
from textblob import TextBlob
import pandas as pd
import numpy as np
import nltk
import sys
import os
import string
import unicodedata
import csv
from nltk.text import Text
from nltk.probability import FreqDist
import unicodedata
from collections import Counter

#---Functions---#
def sentiment(comment):
  analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
      
#---Read data---#
posts =  pd.read_csv("POTUS_facebook_statuses.csv", error_bad_lines = False)
comments = pd.read_csv("comment.csv")

#---Learn---#
posts.head()
posts.describe()

sent = []
comments.head()

#---Get sentiment for all responses---#
for i in xrange(len(comments["comment_message"])):
    item = comments["comment_message"][i].decode("unicode-escape") 
    result = sentiment(item)
    print result
    #result = float(result)
    sent.append(result)
    
#---How many negatives and positives?---#
Counter(sent)

