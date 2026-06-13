document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('news-form');
  const textInput = document.getElementById('news-text');
  const resultLabel = document.getElementById('prediction-result');
  const submitButton = document.getElementById('submit-button');
  const apiEndpoint = 'http://127.0.0.1:5000/predict';

  const updateResult = (message) => {
    resultLabel.textContent = message;
  };

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const content = textInput.value.trim();

    if (!content) {
      updateResult('Please paste the news text before analyzing.');
      return;
    }

    submitButton.disabled = true;
    updateResult('Analyzing the text…');

    try {
      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: content }),
      });

      if (!response.ok) {
        throw new Error(`Server responded with status ${response.status}`);
      }

      const data = await response.json();
      updateResult(data.label || 'Unable to determine the news type.');
    } catch (error) {
      console.error('Prediction error:', error);
      updateResult('Unable to reach the backend. Make sure the Flask app is running.');
    } finally {
      submitButton.disabled = false;
    }
  });
});
