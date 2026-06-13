# Fake News Detection Chrome Extension

A simple, custom-built Chrome extension with a Flask backend that uses a trained SVM model to classify news text as real or fake.

## Project Structure

- `ML_model/`: contains the Flask backend, the trained model artifacts, and extension assets.
- `ML_model/app.py`: custom Flask application that preprocesses input text and returns predictions.
- `ML_model/popup.html`: browser extension interface for pasting news stories.
- `ML_model/popup.js`: frontend logic that sends text to the backend and shows the result.
- `ML_model/manifest.json`: the Chrome extension configuration.

## Installation

1. Clone or download the repository.
2. Install Python 3.x if needed.
3. Install project dependencies:

   ```bash
   pip install -r ML_model/requirements.txt
   ```

## Running the Backend

1. Open a terminal and change to the model folder:

   ```bash
   cd ML_model
   ```

2. Start the backend server:

   ```bash
   python app.py
   ```

3. The server listens on `http://127.0.0.1:5000`.

## Loading the Chrome Extension

1. Open Chrome and navigate to `chrome://extensions`.
2. Enable Developer mode.
3. Click `Load unpacked` and select the `ML_model` folder.
4. Open the extension and paste the news text.

## Usage

- Paste the news text into the extension textarea.
- Click the Analyze button.
- The extension will send the text to the local Flask backend and display whether it is real or fake.

## Implementation Notes

- The backend performs a small text normalization step before vectorizing input.
- The model is loaded from `svm_model.pkl` and the vectorizer from `vectorizer.pkl`.
- This repository is arranged as a tailored project, not a generic boilerplate.

## Technologies Used

- Python
- Flask
- JavaScript
- HTML
- CSS
