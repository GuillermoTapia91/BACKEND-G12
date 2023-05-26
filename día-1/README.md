Crear un entorno virtual
python3 -m venv nombre_entorno


Activar el entorno virtual
# Linux
source nombre_entorno/bin/activate

# Windows
nombre_entorno\Scripts\activate

# Mac OS
source nombre_entorno/bin/activate

# Git Bash
source nombre_entorno/Scripts/activate

## Instalar dependencias
 pip install flask

## Consultar dependencias
pip freeze
pip list

## CREAR archivo requirements.txt
pip freeze > requirements.txt