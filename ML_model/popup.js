// Get the extension form element from the popup
const newsForm = document.getElementById('news-form');

// Listen for the form submit event
newsForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Read the news text entered by the user
  const articleText = document.getElementById('news-text').value;

  try {
    // Send text to the Flask backend for prediction
    const serverResponse = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: articleText}),
    });

    if (serverResponse.ok) {
      const jsonData = await serverResponse.json();
      const classification = jsonData.prediction;
      const outputElement = document.getElementById('prediction-result');
      outputElement.innerText = classification === 0 ? 'The news is Real' : 'The news is Fake';
    } else {
      console.error('Prediction request failed:', serverResponse.status);
    }
  } catch (error) {
    console.error('Prediction request failed:', error);
  }
});
