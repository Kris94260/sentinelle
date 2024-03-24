import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { Provider } from 'react-redux';
import store1 from './redux/store1';



const root = createRoot(document.getElementById('root'));

root.render(
  <Provider store={store1}>
      <App />
  </Provider>
);

