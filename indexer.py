import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def index_documents(directory):
    # Load documents
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), 'r') as f:
                documents.append(f.read())
    
    # Compute TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Save index with pickle
    with open("inverted_index.pkl", "wb") as f:
        pickle.dump((vectorizer, tfidf_matrix), f)

index_documents("output/")
