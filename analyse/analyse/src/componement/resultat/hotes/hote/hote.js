import './hote.css';
import React, { useState } from 'react';
import {  useSelector } from 'react-redux';


const Hote = (hote) => {

    const varstor = useSelector(state => state);
    
    
    return (
      <div className='hote' >
      
        <p><strong>{hote.hote.IP}</strong></p>
        <p>{hote.hote.Map_ports.http_port ? 'HTTP' : ''}</p>
        <p>{hote.hote.Map_ports.ssh_port ? 'SSH' : ''}</p>
        <p>{hote.hote.Map_ports.sql_port ? 'SQL' : ''}</p>
        <p>{hote.hote.Map_ports.ftp_port ? 'FTP' : ''}</p>
        <span className='pouce'>{hote.hote.Hote_pingable ? '👍' : '👎'}</span>
        
      </div>
    );
  };
  
  
  export default Hote;

