import './resultat.css';
import React from 'react';
import { Box } from '@mui/material';
import { useSelector } from 'react-redux';
import Hotes from './hotes/hotes';


const Resultat = () => {

    const varstor = useSelector(state => state);
    
    return (
    <Box width={"100%"} borderRadius={8} boxShadow={3} p={2} sx={{ m: 4 }} border="4px solid #13191E">
        <div className='contenu'>
            <div className='filtres'>
                <p>Dates: {varstor.selectedDate}  </p>
                <p>Filtre IP: {varstor.inputIP}  </p>
                <p>Filtre protocol: {varstor.selectedProtocol}  </p>
                <p>Pingable: {String(varstor.checkPing)}</p>
            </div>
            <div>
                <Hotes />
            </div>
        </div>
    </Box>
    );
  };
  
  
  export default Resultat;


