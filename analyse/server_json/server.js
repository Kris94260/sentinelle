const GestionnaireRepertoire = require('./gestionnaire');

const http = require('http');

const host = 'localhost';
const port = 8000;

const requestListener = function (req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*'); // Autoriser toutes les origines (à ajuster selon vos besoins)
  res.setHeader('Access-Control-Allow-Methods', 'GET'); // Les méthodes HTTP autorisées (GET dans ce cas)
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type'); // Les en-têtes autorisés

  if (req.method === 'GET') {
    res.setHeader('Content-Type', 'html/text');
    res.writeHead(404);
    console.log("connexion GET");
    res.end("GET n'est pas autorisé");

  } else if (req.method === 'POST' ) {
    res.setHeader('Content-Type', 'application/json');
    res.writeHead(200);
    let body = '';
    req.on('data', (chunk) => {
      body += chunk.toString();
    });

    req.on('end', () => {
      body =  JSON.parse(body);
      console.log('Corps du message reçu:', body);
      
      const gestionnaire = new GestionnaireRepertoire();
      conte=gestionnaire.analyse_requete(body);
      console.log(conte);
      let k = JSON.stringify(conte, null, 2);
      // Traitez le corps du message ici
      res.end(k);
    });
  }
};


const server = http.createServer(requestListener);
server.listen(port, host, () => {
  console.log(`Server is running on http://${host}:${port}`);
});
