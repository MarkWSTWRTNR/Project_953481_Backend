import string
import numpy as np
import pandas as pd
from rank_bm25 import BM25Okapi


def searchByTitle(query):
    data = pd.read_csv('src/resource/anime.csv')
    title = data['title']
    corpus = title.to_numpy().tolist()
    cleaned_corpus = []
    for doc in corpus:
        cleaned_doc = remove_puncts(doc, string)
        cleaned_corpus.append(cleaned_doc)
    tokenized_clean_corpus = []
    # Ex. {[dragon ball]} -> {[dragon], [ball]}
    for doc in cleaned_corpus:
        doc = doc.split()
        tokenized_clean_corpus.append(doc)
    bm25 = BM25Okapi(tokenized_clean_corpus)
    # Create txt file
    # ac.trainTitleTextFile(ac.get_text(tokenized_clean_corpus))
    relevent_document = 0
    tokenized_query = remove_puncts(query, string).split(" ")
    doc_scores = bm25.get_scores(tokenized_query).tolist()
    for score in doc_scores:
        if score != 0.0:
            relevent_document += 1
    rank = np.argsort(doc_scores)[::-1]

    return data.iloc[rank[:relevent_document]]

def searchByDescription(query):
    data = pd.read_csv('src/resource/anime.csv')
    Description = data['synopsis']
    corpus = Description.to_numpy().tolist()
    cleaned_corpus = []
    for doc in corpus:
        cleaned_doc = remove_puncts(doc, string)
        cleaned_corpus.append(cleaned_doc)
    tokenized_clean_corpus = []
    # Ex. {[dragon ball]} -> {[dragon], [ball]}
    for doc in cleaned_corpus:
        doc = doc.split()
        tokenized_clean_corpus.append(doc)
    bm25 = BM25Okapi(tokenized_clean_corpus)
    # Create txt file
    # ac.trainTitleTextFile(ac.get_text(tokenized_clean_corpus))
    relevent_document = 0
    tokenized_query = remove_puncts(query, string).split(" ")
    doc_scores = bm25.get_scores(tokenized_query).tolist()
    for score in doc_scores:
        if score != 0.0:
            relevent_document += 1
    rank = np.argsort(doc_scores)[::-1]

    return data.iloc[rank[:relevent_document]]
    # delete special symbols +-*/!@#$


def remove_puncts(input_string, string):
    return str(input_string).translate(str.maketrans('', '', string.punctuation)).lower()
