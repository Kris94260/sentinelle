import './fileslist.css';
import { useSelector, useDispatch } from 'react-redux';
import { changeFile } from '../../../../redux/store1';

const get_json_file = async (file) => {
    try {
      const jsonData = JSON.stringify({ request: "file",name:file }); // Remplacez par les données JSON que vous souhaitez envoyer
      const response = await fetch('http://localhost:8000', {
        method: 'POST',
        body: jsonData,
      });
  
      if (!response.ok) {
        throw new Error('Erreur lors de la requête');
      }
  
      const responseData = await response.json(); // Si votre serveur renvoie des données JSON
  
      return responseData;
    } catch (error) {
      console.error('Erreur:', error.message);
    }
  };


function FilesList({file,index}) {
    const varstor = useSelector(state => (state));
    const fichier_select= varstor.FileSelected;
    const dispatch = useDispatch();

    const handleClick =async  () => {
        const data = await get_json_file(file);
        dispatch(changeFile(data,file));


        
    }
    let retour;
    if (fichier_select == file){
         retour = <div className="file_select" onClick={handleClick} key={index}>{file}</div>
    }
    else{
        retour = <div className="file" onClick={handleClick} key={index}>{file}</div>
    }
    return (
        retour
    );
  }
  
  export default FilesList;