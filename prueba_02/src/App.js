import logo from './logo.svg';
import './App.css';

import React from 'react';
import { useState } from 'react';
import First from './components/first';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          EditXCV <code>src/App.js</code> and save to reload.
        </p>
        <p>
          Prueba de la clase de React 👋
        </p>
        <First />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
