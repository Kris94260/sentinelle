import './App.css';
import Entete from './componement/entete/entete';
import React from 'react';
import Corp from './componement/corp/corp';
import CssBaseline from '@mui/material/CssBaseline';

const App = () => {

  return (
    <div>
      <CssBaseline />
        <div className="App">
          <Entete text={"Krxs94"}/>
          <Corp />
        </div>
    </div>
    
  );
};


export default App;
