#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:33:43 2017

@author: magananoronha
"""
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import os
import spacy
import pandas as pd
import itertools as it

nlp = spacy.load('en')


data_directory = os.path.join('..', 'data',
                              'yelp_dataset_challenge_academic_dataset')

review_json_filepath = os.path.join(data_directory,
                                    'yelp_academic_dataset_review.json')

unigram_sentences_filepath = os.path.join(intermediate_directory,
                                          'unigram_sentences_all.txt')


def punct_space(token):
    """
    helper function to eliminate tokens
    that are pure punctuation or whitespace
    """
    
    return token.is_punct or token.is_space

def line_review(filename):
    """
    generator function to read in reviews from the file
    and un-escape the original line breaks in the text
    """
    
    with codecs.open(filename, encoding='utf_8') as f:
        for review in f:
            yield review.replace('\\n', '\n')
            
def lemmatized_sentence_corpus(filename):
    """
    generator function to use spaCy to parse reviews,
    lemmatize the text, and yield sentences
    """
    
    for parsed_review in nlp.pipe(line_review(filename),
                                  batch_size=10000, n_threads=4):
        
        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent
                             if not punct_space(token)])

    
with codecs.open(unigram_sentences_filepath, 'w', encoding='utf_8') as f:
    for sentence in lemmatized_sentence_corpus(review_txt_filepath):
        f.write(sentence + '\n')


trigram_sentences = LineSentence(trigram_sentences_filepath)
word2vec_filepath = os.path.join(intermediate_directory, 'word2vec_model_all')

food2vec = Word2Vec(trigram_sentences, size=100, window=5,
                    min_count=20, sg=1, workers=4)

food2vec.save(word2vec_filepath)

for i in range(1,12):

    food2vec.train(trigram_sentences)
    food2vec.save(word2vec_filepath)