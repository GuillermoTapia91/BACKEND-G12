-- DDL (DATA DEFITION LANGUAGE)
-- CREATE   > Crear DB o Tablas o Columna o Indices, etc.
-- ALTER    > Modificar las tablas, DB, columnas, etc
-- DROP     > Eliminar tablas, Db, Columnas, etc
-- TRUCANTE > Eliminar todos los registros de una tabla
-- COMMENT  > Agregar comentarios a diccionario de datos
-- RENAME   > Renombrar Tablas, Columnas, ETC
CREATE DATABASE prueba;
--Crear Tabla
CREATE TABLE alumnos(
    id SERIAL         NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NULL,
    apellido_materno TEXT NULL,
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    habilitado BOOLEAN DEFAULT true
);

-- DML (DATA MANIPULATION LANGUAGE)
-- INSERT > Insertar data a las tablas
-- SELECT > Seleccionar la data de las tablas
-- UPDATE > Actualizar la informacion contenida en las tablas
-- DELETE > Eliminar la informacion de las tablas

INSERT INTO alumnos (id, nombre, apellido_paterno, apellido_materno, correo, fecha_nacimiento, habilitado) VALUES
(DEFAULT,'Guillermo', 'Tapia', 'Alcazar', '123@gmail.com', '1991-08-31', DEFAULT);
(DEFAULT, 'Juana', 'Martinez', 'Manrique', 'jmartinez@gmail.com', '1992-11-01', DEFAULT),
(DEFAULT, 'Pedro', 'Choquehuanca', 'Gil', 'pchoquehuanca@gmail.com', '2000-05-15', false),
(DEFAULT, 'Martin', 'Ancco', 'Perez', 'mancco@gmail.com', '1998-09-25', DEFAULT),
(DEFAULT, 'Roxana', 'Juarez', 'Rodriguez', 'rjuarez@gmail.com', '2005-02-09', false);

SELECT nombre FROM alumnos;
SELECT nombre, correo FROM alumnos;

--si sale END , AGRANDAMOS LA PANTALLA Y LUEGO ESCRIBIMOS Q
