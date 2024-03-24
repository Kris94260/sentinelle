const path = require('path');

class Fichier {
 constructor(nomFichier) {
    this.fichier = nomFichier;
    this.nom = path.basename(nomFichier, path.extname(nomFichier));
    this.extension = path.extname(nomFichier).toLowerCase().slice(1);
  }

  
  toJSON() {
    return {
      "nom": this.nom,
      "extension": this.extension
    };
  }
}

module.exports = Fichier;
