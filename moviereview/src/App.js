import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
  <header className="App-header">
     <img src={logo} className="App-logo" alt="logo" /> 
    <p>
  <span class="highlight">The best tool to give you movie reviews!</span>
  </p>
  {/*
    <a
      className="App-link"
      href="https://reactjs.org"
      target="_blank"
      rel="noopener noreferrer"
    >
      Learn React
    </a>
    */}
    <label>
      <textarea name></textarea>
    </label>
    <span class="highlight">Result:</span>
  </header>
</div>

  );
}

export default App;
