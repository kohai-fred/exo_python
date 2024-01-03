const express = require('express');
const app = express();
const port = 3000;

// Middleware pour le traitement des données JSON
app.use(express.json());

// Endpoint de test
app.get('/', (req, res) => {
    res.send('Bienvenue sur mon API Node.js !');
});

// Endpoint pour une requête POST
app.post('/api/data', (req, res) => {
    const data = req.body;
    // Faites quelque chose avec les données, par exemple, renvoyez-les
    res.json({ message: 'Données reçues avec succès', data });
});

// Démarrer le serveur
app.listen(port, () => {
    console.log(`Serveur en cours d'exécution sur http://localhost:${port}`);
});
