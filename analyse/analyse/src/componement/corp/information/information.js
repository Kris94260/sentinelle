import './information.css';
import React from 'react';
import { useSelector } from 'react-redux';
import { Button } from '@mui/material';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import { useDispatch } from 'react-redux';
import { filtreDisplay} from '../../../redux/store1';
import { Box } from '@mui/material';
 

function Information() {
  const varstor = useSelector(state => state);
  const dispatch = useDispatch();
  const handleClick = () => {
    dispatch(filtreDisplay('list'))
  };
  let retour = '';
  if (varstor.hoteObj){
    let httpopen=[]
    varstor.hoteObj.Map_ports.http_port.Ports.forEach((element) => {if (element.Status == "open"){httpopen.push(element.Numero)}});
    let sshopen=[]
    varstor.hoteObj.Map_ports.ssh_port.Ports.forEach((element) => {if (element.Status == "open"){sshopen.push(element.Numero)}});
    let sqlopen=[]
    varstor.hoteObj.Map_ports.sql_port.Ports.forEach((element) => {if (element.Status == "open"){sqlopen.push(element.Numero)}});
    let ftpopen=[]
    varstor.hoteObj.Map_ports.ftp_port.Ports.forEach((element) => {if (element.Status == "open"){ftpopen.push(element.Numero)}});
    
    retour = (
        <div>
            <h1>{varstor.hoteObj.IP}</h1>
            <p>Hote pingable :{JSON.stringify(varstor.hoteObj.Hote_pingable)}</p>
            <p>HTTP :{JSON.stringify(httpopen )}</p>
            <p>SSH :{JSON.stringify(sshopen)}</p>
            <p>SQL :{JSON.stringify(sqlopen)}</p>
            <p>FTP :{JSON.stringify(ftpopen)}</p>
            <p>{JSON.stringify(varstor.hoteObj.Map_ports.http_port.Ports)}</p>
        </div>
    )   
  }
  return (
    <div className='Information'>
    <div className="Back">
      <Button variant="contained" onClick={handleClick}>
        <ChevronLeftIcon />
        Retour
      </Button>
    </div>
    <div className="Content">
      {<Box sx={{ padding: 2, border: '1px solid', borderRadius: 2, overflow: 'visible' }}>
        {retour}
      </Box>}
    </div>
  </div>
);
};


export default Information;
