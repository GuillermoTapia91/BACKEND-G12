import express from "express";
import { usuarioRouter } from "./routes/usuario.routes.js";

const servidor = express();

servidor.use(express.json());

const puerto = process.env.PORT ?? 3000;

// Agregar rutas
servidor.use(usuarioRouter);

servidor.listen(puerto, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${puerto}`);
});
