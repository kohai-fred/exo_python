import express from "express";
import populations from "./populations.js";

const app = express();
const port = 3000;

app.use(express.json());

app.get("/api/populations", (req, res) => {
  res.json(populations);
});

// Endpoint pour ajouter un produit au panier
app.get("/api/person/:id", (req, res) => {
  const id = req.params?.id || undefined;
  const person = populations.find((p) => p.id == id);
  if (person) {
    res.status(200).json(person);

    return;
  }

  res.status(404).json({ message: "Personne non trouvée" });
});

app.listen(port, () => {
  console.log(`Microservice gestion des persons ${port}`);
});
