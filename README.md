# Fake News Detection Chrome Extension

A lightweight Chrome extension and Flask backend for classifying news text as real or fake.

## Project Structure

- `ML_model/`: contains the Flask app, model files, and browser extension assets.
- `ML_model/app.py`: Flask server that loads the trained SVM model and returns predictions.
- `ML_model/popup.html`: browser extension UI for entering news text.
- `ML_model/popup.js`: sends text to the Flask backend and displays the prediction.
- `ML_model/manifest.json`: Chrome extension manifest.

## Installation

1. Clone or download the repository.
2. Install Python 3.x if needed.
3. Install the Python dependencies:

   ```bash
   pip install -r ML_model/requirements.txt
   ```

## Running the Flask Backend

1. Open a terminal and change to the model folder:

   ```bash
   cd ML_model
   ```

2. Start the Flask server:

   ```bash
   python app.py
   ```

3. The backend will listen on `http://127.0.0.1:5000`.

## Loading the Chrome Extension

1. Open Chrome and go to `chrome://extensions`.
2. Enable Developer mode.
3. Click `Load unpacked` and select the `ML_model` folder.
4. Click the extension icon and enter the news text.

## Usage

- Enter or paste the article text into the extension popup.
- Click `Predict` to determine whether the text is likely real or fake.
- The extension sends the text to the Flask backend and displays the result.

## Notes

- Make sure the Flask backend is running before using the extension.
- The extension currently connects to `http://localhost:5000/predict`.

## Technologies Used

- Python
- Flask
- JavaScript
- HTML
- CSS
