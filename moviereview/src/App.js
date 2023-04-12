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

    // Replace this with your actual code to get the result from the backend
    const mockResult = 'This is the result!';
    setResult(mockResult);
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
              <textarea name="text" value={textValue} onChange={handleTextareaChange}></textarea>
            </label>
            <br></br>
            <button type="submit">Review</button>
          </div>
        </form>
        {result && (
          <div>
            <span>Result:</span>
            <p>{result}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
