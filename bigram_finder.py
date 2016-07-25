'''
Created on Jul 24, 2016

@author: hadoop
'''
import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize

text = "this is a foo bar bar black sheep  foo bar bar black sheep foo bar bar black  sheep shep bar bar black sentence"

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(word_tokenize(text))
finder.apply_freq_filter(2) #To filter less frequently occurring bi-grams

for i in finder.score_ngrams(bigram_measures.pmi):
    print i
#To just get top N bigrams based on score
nbest = finder.nbest(bigram_measures.pmi, 5)
