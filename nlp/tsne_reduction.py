#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 07:32:05 2017

@author: magananoronha
"""

from sklearn.manifold import TSNE
import os

if __name__ == '__main__':

    word2vec_filepath = os.path.join(data_directory, 'word2vec_model_all')
    data_directory = os.path.join('/home/ubuntu/workspace/climate-blog-scraper/data')
    
    blog2vec = Word2Vec.load(word2vec_filepath)
    
    blog2vec.init_sims()
    
    ordered_vocab = [(term, voc.index, voc.count)
             for term, voc in blog2vec.wv.vocab.items()]
    
    ordered_terms, term_indices, term_counts = zip(*ordered_vocab)
    word_vectors = pd.DataFrame(blog2vec.wv.syn0norm[term_indices, :],
                                index=ordered_terms)
    
    
    tsne_vectors_filepath = os.path.join(data_directory,
                                         u'tsne_vectors.npy')
    
    
    tsne = TSNE()
    tsne_vectors = tsne.fit_transform(word_vectors.values)
    
    with open(tsne_filepath, 'w') as f:
        pickle.dump(tsne, f)
    
#    pd.np.save(tsne_vectors_filepath, tsne_vectors)
#    
#    with open(tsne_filepath) as f:
#        tsne = pickle.load(f)
#        
#    tsne_vectors = pd.np.load(tsne_vectors_filepath)
#    
#    tsne_vectors = pd.DataFrame(tsne_vectors,
#                                index=pd.Index(tsne_input.index),
#                                columns=[u'x_coord', u'y_coord'])