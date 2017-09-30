#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:20:07 2017

@author: magananoronha
"""

import os
import spacy
import string
import codecs
import pandas as pd
import itertools as it
from gensim.models import Phrases, Word2Vec
from gensim.models.word2vec import LineSentence
from collections import Counter

import probablepeople as pp


#from gensim.corpora import Dictionary, MmCorpus
#from gensim.models.ldamulticore import LdaMulticore
#
#import pyLDAvis
#import pyLDAvis.gensim
#import warnings



def line_review(df):
    """
    generator function to read in reviews from the file
    and un-escape the original line breaks in the text
    """
    for i, body in df['body'].iteritems():
        yield body
        
        
def clean_names(people):
    """
    helper function that takes in a list of spacy tokens id'ed as PERSON names,
    converts them to strings and removes punctuation and denotation of possesion
    
    modifcations occur in place
    
    returns None 
    """        
    for i in range(len(people)):
        people[i] = str(people[i])
        people[i] = people[i].replace(string.punctuation,'')
        people[i] = people[i].replace("’s",'')
        

def agg_names(people):
    """
    helper function that takes in a list of names and 
    aggregates names that are identical
    
    returns a list of unique names
    """
    return list(set(people))


def label_names(people):
    """
    helper function that takes in a list of unique names, uses
    probablepeople to split name into labled parts
    
    returns a list of tuples 
    """    
    labeled_names = []
    for i in range(len(people)):
        labeled_names.append(pp.parse(people[i]))
    return labeled_names


def filter_names(labeled_names):
    people_names = []
    for name in labeled_names:
        has_surname = False
        surname_index = None
        has_givenname = False
        givenname_index = None        
        for i in range(len(name)):
            if name[i][1] == 'Surname':
                has_surname = True
                surname_index = i
            if name[i][1] == 'GivenName':
                has_givenname = True
                givenname_index = i
        if has_surname and has_givenname:
            people_names.append(' '.join([name[givenname_index][0], name[surname_index][0]]))
        if has_surname and not has_givenname:
            people_names.append(name[surname_index][0])
    return people_names
            
        
def find_people(spacy_doc):
    """
    helper function that takes in a document parsed by spacy
    aggregates a list of named entities flagged as PERSON
    
    returns a list spacy tokens 
    """        
    entities = spacy_doc.ents
    people = []
    for ent in entities:
        if ent.label_ == 'PERSON':
            people.append(ent)
    clean_names(people)
    people = agg_names(people)
    labeled_names = label_names(people)
    people = filter_names(labeled_names)
    return people


def lemmatized_sentence_corpus(df):
    """
    generator function to use spaCy to parse reviews,
    lemmatize the text, and yield sentences
    """
    names = []
    for spacy_doc in nlp.pipe(line_review(df), batch_size=10000, n_threads=4):
        names.append(find_people(spacy_doc))
    return names


if __name__ == '__main__':
    
    df = pd.read_pickle('second_postgres.pkl')
    df = df[(df.body).notnull()]
    
    nlp = spacy.load('en')
    
    df['names'] = lemmatized_sentence_corpus(df)
    df.to_pickle('names.pkl')



#unigram_sentences_filepath = os.path.join(intermediate_directory,
#                                          'unigram_sentences_all.txt')    
#
#unigram_sentences = LineSentence(unigram_sentences_filepath)
#
#
#unigram_dict = Dictionary(unigram_sentences)
#
#
#
#bigram_model_filepath = os.path.join(intermediate_directory, 'bigram_model_all')
#
#bigram_model = Phrases(unigram_sentences)
#
#bigram_model.save(bigram_model_filepath)
#
#bigram_sentences_filepath = os.path.join(intermediate_directory,
#                                         'bigram_sentences_all.txt')
#
#
#with codecs.open(bigram_sentences_filepath, 'w', encoding='utf_8') as f:
#    
#    for unigram_sentence in unigram_sentences:
#        
#        bigram_sentence = u' '.join(bigram_model[unigram_sentence])
#        
#        f.write(bigram_sentence + '\n')
#
#
#bigram_sentences = LineSentence(bigram_sentences_filepath)
#
#trigram_model = Phrases(bigram_sentences)
#
#
#trigram_model_filepath = os.path.join(intermediate_directory,
#                                      'trigram_model_all')
#
#trigram_model = Phrases(bigram_sentences)
#
#trigram_model.save(trigram_model_filepath)
#    
#trigram_model = Phrases.load(trigram_model_filepath)
#
#trigram_sentences_filepath = os.path.join(intermediate_directory,
#                                          'trigram_sentences_all.txt')
#
#with codecs.open(trigram_sentences_filepath, 'w', encoding='utf_8') as f:
#    
#    for bigram_sentence in bigram_sentences:
#        
#        trigram_sentence = u' '.join(trigram_model[bigram_sentence])
#        
#        f.write(trigram_sentence + '\n')
#        
#trigram_sentences = LineSentence(trigram_sentences_filepath)