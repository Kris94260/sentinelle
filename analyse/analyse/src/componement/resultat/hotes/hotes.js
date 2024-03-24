import React from 'react';
import { Box } from '@mui/material';
import { useSelector } from 'react-redux';
import Hote from './hote/hote';
import './hotes.css';
import { useDispatch } from 'react-redux';
import { displayHote,filtreDisplay } from '../../../redux/store1';
import { styled } from '@mui/system';

const Hotes = () => {
    let retour = "";
    const varstor = useSelector(state => state);
    const dispatch = useDispatch();
    const jsonFiles = varstor.DataJson;
    const StyledBox = styled(Box)({
        '&:hover': {
          boxShadow: '0px 0px 18px lightblue',
          borderRadius: 8,
          transition: 'transform 0.3s ease',
          transform: 'scale(1.04)',
          cursor: 'pointer',
        }
      });


    
    const handleBoxClick = (hote) => {
        
        dispatch(displayHote(hote));
        dispatch(filtreDisplay('information'));
        
      }
      

    if (jsonFiles) { 
        try {
            const data = JSON.parse(jsonFiles);
            if (data.Hotes) {
                retour = data.Hotes.map((hote, index) => (
                    <StyledBox>
                    <Box 
                        
                        borderRadius={8} 
                        boxShadow={3} 
                        p={2}
                        sx={{m: 1,padding: 1, border: '1px solid', borderRadius: 2, backgroundColor:hote.Hote_pingable ? "rgb(0, 255, 0,0.3)" : "rgb(255, 0, 0,0.3)"}} 
                        onClick={() => handleBoxClick(hote)}>
                        <Hote key={index} hote={hote}/>
                    </Box>
                    </StyledBox>
                ));
            }
        } catch (error) {
            retour ="Erreur "+ error.message;
        }
    } else {
        retour = "Aucun fichier selectionné";
    }

    return (
        <Box p={2} width="100%">
            <p><u>Fichier selectionné: {varstor.FileSelected}</u></p>
            <div className='hotes'>
                {retour}
            </div>
        </Box>
    );
};

export default Hotes;
