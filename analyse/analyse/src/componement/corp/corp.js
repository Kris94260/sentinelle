import './corp.css';
import FileList from './list/list';
import Filtre from './filtre/filtre';
import Resultat from '../resultat/resultat';
import Information from './information/information';
import React from 'react';
import { Box } from '@mui/material';
import { useSelector } from 'react-redux';

function Corp() {
  const varstor = useSelector(state => state);
  let show ='';
  switch (varstor.display) {
    case 'list':
      show = (<div><Filtre /> <Resultat /> </div>)
      break;
    case 'information':
      show = (<div><Information /></div>)
      break;
    default:
      show = (<div>Page not found : {varstor.display}</div>); 
      break;
  }

  return (
      <div className="Corp">
      
        <FileList />  
          {show}
      
      </div>
  );
}

export default Corp;
