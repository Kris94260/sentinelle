import React, { useState } from 'react';
import './list.css';
import FilesList from './fileslist/fileslist';
import { Box } from '@mui/material';


const FileList = () => {
  const [jsonFiles, setjsonFiles] = useState('');

  const ListJsonFile = async () => {
    try {
      const jsonData = { request: 'list',name: null, date:null,carte:null }; 

      const response = await fetch('http://localhost:8000', {
        method: 'POST',
        body: JSON.stringify(jsonData),
      });

      if (!response.ok) {
        throw new Error('Erreur lors de la requête');
      }

      const responseData = await response.json(); // Si le serveur renvoie des données JSON
      setjsonFiles(responseData)
    } catch (error) {
      console.error('Erreur:', error.message);
    }
  };
  
  return (
    <Box  border="4px solid #13191E" borderRadius={8} boxShadow={3} p={2} sx={{ m: 4 }} width= {"28%"} >
      <div className='listFile'>
          <div>
            <p>Liste des rapports</p>
          </div>
          <div>
            <button onClick={ListJsonFile}>Actualiser la liste</button>
            {jsonFiles && (
              
              <ul>
                {jsonFiles.fichiers.map((file, index) => (
                  <FilesList file={file} index={index}/>
                ))}
              </ul>
            )}
          </div>
      </div>
    </Box>
  );
};


export default FileList;