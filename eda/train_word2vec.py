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
import boto3
import pandas as pd
import itertools as it
from dateutil.parser import parse
import datetime


def punct_space(token):
    """
    helper function to eliminate tokens
    that are pure punctuation or whitespace
    """
    
    return token.is_punct or token.is_space

            
def line_review(df):
    """
    generator function to read in reviews from the file
    and un-escape the original line breaks in the text
    """
    for i, body in df['body'].iteritems():
        yield body            
            
            
def lemmatized_sentence_corpus(df):
    """
    generator function to use spaCy to parse reviews,
    lemmatize the text, and yield sentences
    """
    
    for spacy_doc in nlp.pipe(line_review(df), batch_size=10000, n_threads=60):

        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent
                             if not punct_space(token)])    
    
    
    for parsed_review in nlp.pipe(line_review(filename),
                                  batch_size=10000, n_threads=60):
        
        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent
                             if not punct_space(token)])

    
if __name__ == '__main__':
    nlp = spacy.load('en')
    data_directory = os.path.join('/home/ubuntu/workspace/climate-blog-scraper/data')

    s3 = boto3.client('s3')


    df = s3.get_object(Bucket='climateblogs', Key='cleaned_db.pkl')['Body'].read()
    
    
    
    df_filepath = os.path.join(data_directory, 'cleaned_db.pkl')
    df = pd.read_pickle(df_filepath)    
        
    unigram_sentences_filepath = os.path.join(data_directory,
                                              'unigram_sentences_all.txt')    
    
    
    with open(unigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for sentence in lemmatized_sentence_corpus(df):
            f.write(sentence + '\n')

    
    unigram_sentences = LineSentence(unigram_sentences_filepath)
    
    bigram_model_filepath = os.path.join(data_directory, 'bigram_model_all')
    bigram_model = Phrases(unigram_sentences)
    bigram_model.save(bigram_model_filepath)
    bigram_sentences_filepath = os.path.join(data_directory,
                                             'bigram_sentences_all.txt')
    
    
    with open(bigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for unigram_sentence in unigram_sentences:
            bigram_sentence = u' '.join(bigram_model[unigram_sentence])
            f.write(bigram_sentence + '\n')
    
    
    bigram_sentences = LineSentence(bigram_sentences_filepath)
    
    trigram_model = Phrases(bigram_sentences)
    trigram_model_filepath = os.path.join(data_directory,
                                          'trigram_model_all')
    trigram_model = Phrases(bigram_sentences)
    trigram_model.save(trigram_model_filepath)
    trigram_model = Phrases.load(trigram_model_filepath)
    trigram_sentences_filepath = os.path.join(data_directory,
                                              'trigram_sentences_all.txt')
    
    with open(trigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for bigram_sentence in bigram_sentences:
            trigram_sentence = u' '.join(trigram_model[bigram_sentence])
            f.write(trigram_sentence + '\n')
            
    trigram_sentences = LineSentence(trigram_sentences_filepath)
    

    
    
    trigram_sentences = LineSentence(trigram_sentences_filepath)
    word2vec_filepath = os.path.join(intermediate_directory, 'word2vec_model_all')
    
    food2vec = Word2Vec(trigram_sentences, size=100, window=5,
                        min_count=20, sg=1, workers=4)
    
    food2vec.save(word2vec_filepath)
    
    for i in range(1,12):
    
        food2vec.train(trigram_sentences)
        food2vec.save(word2vec_filepath)