import { TipoUsuario } from "@prisma/client";
import Joi from "joi";

export const registroUsuarioDto = Joi.object({
  nombre: Joi.string().required(),
  apellido: Joi.string(),
  email: Joi.string().email().required(),
  password: Joi.string().required().regex(new RegExp("^[a-zA-Z0-9!@#]{3,20}$")),
  tipoUsuario: Joi.string()
    .regex(new RegExp(`${TipoUsuario.ADMIN}|${TipoUsuario.CLIENTE}`))
    .required(),
});

export const loginDto = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().required(),
});
