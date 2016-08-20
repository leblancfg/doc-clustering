#!usr/bin/env python
#-*- coding: utf-8 -*-
# Author: leblancfg
# 2016

"""
Document Clustering from Service Desk tickets
"""

from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import csv
import os
import logging
from gensim import corpora, models
import gensim

# Set up word handling
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

# Set up word handling
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

# See logging events
logger = logging.getLogger('gensim.corpora.mmcorpus')

# Extract ticket details from SVD database extract
file = open('input/tickets.csv')
documents = list(csv.reader(file))

def column(matrix, i):
    return [row[i] for row in matrix]

refnum = column(documents, 3)
documents = column(documents,7)
texts = []

# Perform the clustering
for i in documents:

    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # Remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # Stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # Add tokens to list
    texts.append(stemmed_tokens)

    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]

    ldamodel = gensim.models.ldamodel.LdaModel(
        corpus,
        num_topics=2,
        id2word=dictionary,
        passes=20)

