
import React from 'react';
import './filtre.css';
import TextField from '@mui/material/TextField';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormGroup from '@mui/material/FormGroup';
import { Box } from '@mui/material';
import { useDispatch, useSelector } from 'react-redux';
import { filtreIP, filtreProtocol, filtrePing, filtreDate, filtreDisplay} from '../../../redux/store1';



const Filtre = () => {

  const dispatch = useDispatch();
  const varstor = useSelector(state => state);

  const handleInputIPChange = (event) => {
    const value = event.target.value;
    const ipRegex = /^(\d{1,3}\.){3}\d{1,3}$/;

    if (ipRegex.test(value) || value=='') {
        dispatch(filtreIP(value));
    };
  }

  const handleSelectProtocolChange = (event) => {
    const value = event.target.value;
    dispatch(filtreProtocol(value));
  };

  const handleCheckboxPingChange = (event) => {
    dispatch(filtrePing(event.target.checked)); 
  };

  const handleDateChange = (event) => {
    dispatch(filtreDate(event.target.value));
  };

  return (
    <Box width={"100%"} borderRadius={8} boxShadow={3} p={2} sx={{ m: 4 }} border="4px solid #13191E">
      <div className='filtre'>
        <div className='optionFiltre'>
          <form noValidate>
              <TextField
                id="date"
                label="Date"
                type="date"
                defaultValue="2024-02-08" 
                InputLabelProps={{
                  shrink: true,
                }}
                onChange={handleDateChange}
              />
          </form>
        </div>

        <div className='optionFiltre'>
          <TextField
            id="Date"
            label="IP input"
            variant="outlined"
            onChange={handleInputIPChange}
          />
        </div>
        
        <div className='optionFiltre'>
          <Select className='select'
            label="Protocol"
            value={""} 
            onChange={handleSelectProtocolChange}
          >
            <MenuItem value="">
              Sélectionnez un protocole
            </MenuItem>
            <MenuItem value="all">all</MenuItem>
            <MenuItem value="http">http</MenuItem>
            <MenuItem value="ssh">ssh</MenuItem>
            <MenuItem value="sql">sql</MenuItem>
            <MenuItem value="ftp">ftp</MenuItem>
          </Select>
        </div>

        <div className='optionFiltre'>
          <FormGroup>
            <FormControlLabel
              control={<Checkbox checked={varstor.checkPing} onChange={handleCheckboxPingChange} />}
              label="Only pingable"
            />
          </FormGroup>
        </div>
      </div>
  </Box>
    
  );
};

export default Filtre;
