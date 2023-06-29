//CommonJS
//Cuando el archivo tenga la extension cjs indicara que este esta escrito en commonJs

const { saludar } = require("./funcionabilidad.cjs");

console.log("Hola Mundo");

const resultado = saludar();

console.log(resultado);
