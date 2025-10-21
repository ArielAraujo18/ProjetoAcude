import express from "express";
import mysql from "mysql2/promise";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const pool = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "IRani18@#",
  database: "SegurancaAcude"
});

app.get("/casas", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT CoordenadasM FROM cadastroGeral");

    const pontos = [];

    rows.forEach(row => {
      const coords = row.CoordenadasM.split(",").map(c => parseFloat(c.trim()));

      for (let i = 0; i < coords.length; i += 2) {
        // Corrige latitude e longitude para negativas
        const lat = -Math.abs(coords[i]);
        const lng = -Math.abs(coords[i + 1]);

        pontos.push({ lat, lng });
      }
    });

    res.json(pontos);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Erro ao buscar casas" });
  }
});

app.listen(5002, () => console.log("Servidor node rodando na porta 5002 "));
