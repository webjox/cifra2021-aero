import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

import App from './App';

import GlobalStateContext from './state/context/globalStateContext';

import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <GlobalStateContext>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </GlobalStateContext>
  </React.StrictMode>,
  document.getElementById('root')
);
