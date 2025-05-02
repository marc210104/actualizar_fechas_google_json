# actualizar_fechas_google_json
Actualiza la fecha de creación y modificación de fotos y vídeos exportados desde Google Fotos (Google Takeout), usando los archivos .json que acompañan a cada medio.

Funcionamiento:
- Recorre recursivamente las carpetas dentro de una ruta indicada.
- Busca archivos .json y extrae el nombre original del archivo ("title") y el timestamp real de captura ("photoTakenTime").
- Si encuentra el archivo de imagen o vídeo, actualiza su fecha usando os.utime().
- Si falta el archivo o el JSON no contiene datos válidos, informa en consola.

Requisitos:
- Python 3.x
- No requiere librerías externas

Uso:
1. Cambia la ruta al directorio base en la variable `carpeta_prueba`.
2. Ejecuta el script:
   python actualizar_fechas_google.py

Ejemplo de JSON esperado:
{
  "title": "IMG_20200101_123456.jpg",
  "photoTakenTime": {
    "timestamp": "1577883296"
  }
}

Notas:
- Solo se actualizan los archivos que existen físicamente.
- El script no modifica los archivos .json ni crea nuevos archivos.

Autor: Adaptado para uso personal sobre archivos de Google Takeout.

-------------------------------

ENGLISH
-------

Description:
This Python script updates the creation and modification dates of photos and videos exported from Google Photos (via Google Takeout), using the metadata stored in associated .json files.

Functionality:
- Recursively scans a specified folder.
- Locates .json files and extracts the original filename ("title") and real capture timestamp ("photoTakenTime").
- If the media file exists, updates its timestamp using os.utime().
- If the file is missing or the JSON is invalid, prints a warning to the console.

Requirements:
- Python 3.x
- No external libraries needed

Usage:
1. Modify the `carpeta_prueba` variable to point to your Takeout directory.
2. Run the script:
   python actualizar_fechas_google.py

Expected JSON example:
{
  "title": "IMG_20200101_123456.jpg",
  "photoTakenTime": {
    "timestamp": "1577883296"
  }
}

Notes:
- Only updates existing files.
- Does not alter .json files or create new ones.

Author: Adapted for personal use on Google Takeout files.
