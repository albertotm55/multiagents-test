#!/bin/bash

# Script para generar el contenido de un archivo, crear el archivo y ejecutarlo en un entorno bash

# Verifica si se proporcionó el nombre del archivo
if [ -z "$1" ]; then
    echo "Por favor, proporciona un nombre de archivo."
    exit 1
fi

# Crea el archivo y agrega contenido
echo "echo 'Hola, mundo!'" > "$1"

# Da permisos de ejecución al archivo
chmod +x "$1"

# Ejecuta el archivo
./"$1"