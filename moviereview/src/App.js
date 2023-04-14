import { useState } from 'react';
import logo from './Logo.svg';
import './App.css';

function App() {
  const [textValue, setTextValue] = useState('');
  const [result, setResult] = useState('');

  // Handler function to update text value state on input change
  function handleTextareaChange(event) {
    setTextValue(event.target.value);
  }

  // Handler function to handle form submission
  function handleSubmit(event) {
    event.preventDefault();

    // Send POST request to backend with text value
    fetch('http://127.0.0.1:8000/movies_backend/', {
      method: 'POST',
      body: JSON.stringify({ data: textValue }),
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors'
    })
    .then(response => response.json()) // Parse response data as JSON
    .then(data => setResult(data["message"])) // Update result state with response message
    .catch(error => console.error(error)); // Log any errors to console

    console.log('Submitting form with text value:', textValue); // Log the form submission
  }

  // Handler function to trigger form submission on Enter key press
  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      handleSubmit(event);
    }
  }

  // app UI
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <span>The best tool to give you movie reviews!</span>
        </p>
        <form onSubmit={handleSubmit}>
          <div>
            <label>
              <input
                type="text"
                placeholder="Enter Movie"
                value={textValue}
                onChange={handleTextareaChange}
                onKeyPress={handleKeyPress}
              />
            </label>
            <button type="submit">Review</button>
          </div>
        </form>
        <span className="result">{result}</span>
      </header>
    </div>
  );
}

export default App;
