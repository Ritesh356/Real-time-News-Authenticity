from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the SVM model and Tf-idf vectorizer from the pickle files
with open('svm_model.pkl', 'rb') as f:
    svm_classifier = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Accept either JSON or regular form payload
    payload = request.get_json(silent=True)
    article_text = None

    if payload:
        article_text = payload.get('text')
    else:
        article_text = request.form.get('text')

    if article_text:
        # Transform the user input using the loaded Tf-idf vectorizer
        input_vector = tfidf_vectorizer.transform([article_text])

        # Predict using the loaded SVM classifier
        predicted_label = svm_classifier.predict(input_vector)[0]

        return jsonify({'prediction': int(predicted_label)})

    return jsonify({'error': 'Input text not provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
