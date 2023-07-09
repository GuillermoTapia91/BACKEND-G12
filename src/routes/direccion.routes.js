import { Router } from "express";
import * as DireccionController from "../controllers/direccion.controller.js";
import { validarToken } from "../utils/validador.js";

export const direccionRouter = Router();
direccionRouter.post(
  "/direcciones",
  validarToken,
  DireccionController.crearDireccion
);
