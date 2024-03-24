const Fichier = require('./fichier');

const fs = require('fs');
const path = require('path');


class GestionnaireRepertoire {
  constructor() {
    this.request = null;
    this.name = null;
    this.date =null;
    this.carte = null;

    this.contenufile=null;

    this.fichiers = [];
	  this.extensionsPermises = ['.json'];

  }

  analyse_requete(body) {
    if (body.request){
      switch (body.request) {
        case "list":
          this.request = body.request;
          this.date =body.date;
          this.carte = body.carte;
          return this.listerContenu();

        case "file":
          this.request = body.request;
          this.name = body.name;
          return this.afficherContenu();
          
        default:
          return
      }
    }
  }


  listerContenu() {
    const monRep = "./data";
    const cheminComplet = path.join(monRep);
    
	  const statChemin = fs.statSync(cheminComplet);

    if (statChemin.isFile()) {
      return; // Ne rien faire si c'est un fichier
    }
	
    const contenu = fs.readdirSync(cheminComplet);

    contenu.forEach(item => {
        this.fichiers.push(item);
    });
    const jsonData = { Reponse: 'list',fichiers: this.fichiers };
    return jsonData;
  }

  afficherContenu(){

    const monRep = "./data";
    const cheminComplet = path.join(monRep,this.name);
    
	  const statChemin = fs.statSync(cheminComplet);

    if (statChemin.isFile()) {
      this.contenufile =  fs.readFileSync(cheminComplet, 'utf8');
    }
    return { "Reponse" : "file", "contenu" :this.contenufile };
  }
  
  toJSON() {
    return {
      "fichiers": this.fichiers
    };
  }
}

module.exports = GestionnaireRepertoire;
