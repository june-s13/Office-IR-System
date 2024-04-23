import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def index_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), 'r') as f:
                documents.append(f.read())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    with open("inverted_index.pkl", "wb") as f:
        pickle.dump((vectorizer, tfidf_matrix), f)

if __name__ == "__main__":
    index_documents("output/")
