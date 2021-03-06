import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter } from 'react-router-dom';
import { YMaps } from 'react-yandex-maps';

import App from './App';

import GlobalStateContext from './state/context/globalStateContext';

import './global.css';


ReactDOM.render(
  <React.StrictMode>
    <GlobalStateContext>
          <YMaps
            query={{
              apikey: '963076a9-b9f8-4a7f-b5a4-4fd8d2e08ea8',
            }}
          >
            <HashRouter>
              <App />
            </HashRouter>
        </YMaps>
    </GlobalStateContext>
  </React.StrictMode>,
  document.getElementById('root')
);

