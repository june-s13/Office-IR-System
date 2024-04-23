from flask import Flask, request, jsonify
import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    try:
        # Simulate loading of index data, normally from a file
        with open('inverted_index.pkl', 'rb') as f:
            vectorizer, tfidf_matrix = pickle.load(f)
    except Exception as e:
        return jsonify({"error": f"Failed to load index: {str(e)}"}), 500

    try:
        data = request.get_json(force=True)
        query_text = data['query']
        k = int(data['k'])
        query_vec = vectorizer.transform([query_text])
        cos_sim = cosine_similarity(query_vec, tfidf_matrix)
        top_k_indices = np.argsort(cos_sim[0])[-k:]
        return jsonify({"results": top_k_indices.tolist()})
    except Exception as e:
        return jsonify({"error": f"Error processing query: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
