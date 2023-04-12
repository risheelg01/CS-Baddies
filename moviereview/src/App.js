import { useState } from 'react';
import logo from './Logo.svg';
import './App.css';

function App() {
  const [textValue, setTextValue] = useState('');
  const [result, setResult] = useState('');

  function handleTextareaChange(event) {
    setTextValue(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();

    // Here, you can send a POST request to the backend with the textValue
    // variable as the payload.
    console.log('Submitting form with text value:', textValue);

    // Simulating a backend response delay of 2 seconds
    setTimeout(() => {
      setResult('This is the result!');
    });
  }

  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      handleSubmit(event);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <span class>The best tool to give you movie reviews!</span>
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
