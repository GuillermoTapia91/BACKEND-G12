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
SELECT * FROM alumnos;

SELECT * FROM alumnos WHERE habilitado = true;

SELECT * FROM alumnos
WHERE habilitado = true AND apellido_materno='Manrique';

SELECT * FROM alumnos
WHERE habilitado = true AND apellido_materno='Manrique';

-- busca los nombre que tengan la letra un sin importar lo qe haya antes o despues
prueba=# SELECT nombre FROM alumnos WHERE nombre LIKE '%u%';

-- Si usamos ILIKE no sera sencible a mayusculas o minusculas
SELECT nombre FROM alumnos WHERE nombre  ILIKE '%e%';

--debe tener la o en la segunda posicion
SELECT nombre FROM alumnos WHERE nombre  ILIKE '_o%'

SELECT * FROM alumnos WHERE correo  ILIKE '%gmail%' OR correo ILIKE '%hotmail%';

CREATE TABLE direcciones (
    -- una columna llamada id que sea primary key y autoincrementable
    id  SERIAL PRIMARY KEY,
    -- calle  y tiene que ser text y no puede ser nula
    calle TEXT NOT NULL,
    -- numero numeral y no puede ser nulo
    numero INT NOT NULL,
    -- referencia tiene que ser text y puede ser nulo
    referencia TEXT NULL,
    -- alumno_id tiene que ser un numero y no puede ser nulo
    alumno_id INT NOT NULL,
    -- RELACIONES
    CONSTRAINT fk_direcciones_alumnos FOREIGN KEY(alumno_id) 
    REFERENCES alumnos(id)
);

INSERT INTO direcciones (id, calle, numero, referencia, alumno_id) VALUES
(DEFAULT, 'Av Ejercito', 1050, 'Al frente del Hospital', 1),
(DEFAULT, 'Av Tulipanes', 123, NULL, 1),
(DEFAULT, 'Calle Jose Olaya', 333, NULL, 2),
(DEFAULT, 'Giron Los Girasoles', 576, 'Al frente del parque', 3),
(DEFAULT, 'Pje. B', 8664, 'Al lado del periodiquero', 2),
(DEFAULT, 'Calle Los Martires', 123, NULL, 4),
(DEFAULT, 'Av Las condes', 252, 'En la esquina la casa blanca', 3);

SELECT * FROM direcciones WHERE referencia IS NULL;

SELECT * FROM direcciones WHERE referencia IS  NOT  NULL;

SELECT * FROM direcciones WHERE (calle ILIKE '%Av%' OR calle ILIKE '%Calle%') AND  referencia IS  NULL;

SELECT * FROM direcciones
INNER JOIN alumnos

ON direcciones.alumno_id = alumnos.id;










