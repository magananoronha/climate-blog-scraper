#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:33:43 2017

@author: magananoronha
"""
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import os

    
if __name__ == '__main__':
    
    data_directory = os.path.join('/home/ubuntu/workspace/climate-blog-scraper/data')
    final_filepath = os.path.join(data_directory, 'final.txt')
    
    preprocessed_text = LineSentence(final_filepath)
    word2vec_filepath = os.path.join(data_directory, 'word2vec_model_all')
    
    blog2vec = Word2Vec(preprocessed_text, size=100, window=5,
                        min_count=20, sg=1, workers=20)
    
    blog2vec.save(word2vec_filepath)
    
    for i in range(1,12):
        blog2vec.train(preprocessed_text)
        blog2vec.save(word2vec_filepath)