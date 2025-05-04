import logo from './logo.svg';
import './App.css';

import React from 'react';
import moment from 'moment';
import First from './components/first';

export default function App() {
  const currentDateTime = moment().format('YYYY-MM-DD HH:mm:ss');

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Prueba React 👋
        </p>
        <button onClick={botonPulsar} style={{marginLeft: '100px'}}>Pulsar</button>
        <p>
          Current Date and Time: {currentDateTime}
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

const botonPulsar = () => {
  alert('Botón pulsado');
}