from flask import Flask, request, jsonify, render_template
import pickle
import re
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app, resources={r'/predict': {'origins': '*'}})


def normalize_text(article: str) -> str:
    article = article.strip().lower()
    article = re.sub(r'http[s]?://\S+', ' ', article)
    article = re.sub(r'[^a-z0-9\s]', ' ', article)
    article = re.sub(r'\s+', ' ', article)
    return article


with open('svm_model.pkl', 'rb') as model_file:
    svm_classifier = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vector_file:
    tfidf_vectorizer = pickle.load(vector_file)


@app.route('/')
def home() -> str:
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict() -> tuple:
    request_data = request.get_json(silent=True)
    news_text = None

    if isinstance(request_data, dict):
        news_text = request_data.get('text')
    else:
        news_text = request.form.get('text')

    if not news_text:
        return jsonify({'error': 'Article text is required.'}), 400

    cleaned_text = normalize_text(news_text)
    features = tfidf_vectorizer.transform([cleaned_text])
    predicted_label = int(svm_classifier.predict(features)[0])
    label_name = 'Real news' if predicted_label == 0 else 'Fake news'

    return jsonify({
        'prediction': predicted_label,
        'label': label_name,
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
