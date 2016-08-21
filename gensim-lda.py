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
import gensim

def get_files(path):
    # Extract ticket details from SVD database extract
    file = open(path)
    documents = list(csv.reader(file))

    def column(matrix, i):
        return [row[i] for row in matrix]

    refnum = column(documents, ref_idx)
    documents = column(documents, doc_idx)
    return ([refnum, documents])

def clustering(documents):
    # Set up word handling
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()

    # See logging events
    logger = logging.getLogger('gensim.corpora.mmcorpus')

    # Perform the clustering
    for i in documents:
        texts = []
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        # Remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]

        # Stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

        # Add tokens to list
        texts.append(stemmed_tokens)

    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    ldamodel = gensim.models.ldamodel.LdaModel(
        corpus,
        num_topics=2,
        id2word=dictionary,
        passes=20)
    return ldamodel

if __name__ == "__main__":
    # Set up environment-based variables
    ref_idx = 3  # Input file column index for the reference number
    doc_idx = 7  # Input file column index for the ticket description

    tickets = get_files('input/example.csv')[1]
    model = clustering(tickets)
    # print(model.print_topics(num_topics=2, num_words=4))
    m = open('model.txt', 'a')
    m.write(str(model.print_topics()))
    m.close()


