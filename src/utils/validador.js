import jwt from "jsonwebtoken";
import { conexion } from "../base_de_datos.js";

export function validarData({ error, message, data }) {
  //SI hay un error emitiremos un error para detener el proceso
  if (error) {
    throw new Error(JSON.stringify({ message, content: error.details }));
  } else {
    //si no hay error, retomaremos la data
    return data;
  }
}

export async function validarToken(req, res, next) {
  //next> si todo

  if (!req.headers.authorization) {
    return res.status(403).json({
      message: "Se necesita un token para realizar esta petición",
    });
  }

  //Bearer xxxxx.xxxx.xxxx
  const token = req.headers.authorization.split(" ")[1];

  if (!token) {
    return res.status(400).json({
      message: 'El formulario tiene que ser "Bearer <YOUR_TOKEN>"',
    });
  }

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    const usuario = await conexion.usuario.findUniqueOrThrow({
      where: { id: payload.id },
    });
    req.user = usuario;
    //NEXT > pase al sgt controlador
    next();
  } catch (error) {
    return res.status(403).json({
      message: "Error en la token",
      content: error.message,
    });
  }
}
