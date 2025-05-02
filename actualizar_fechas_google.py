import os
import json
from datetime import datetime

def update_file_date(file_path, timestamp):
    """Actualiza la fecha de creación y modificación de un archivo."""
    try:
        # Convierte el timestamp a formato de sistema operativo
        os.utime(file_path, (timestamp, timestamp))
        print(f"Fecha actualizada para: {file_path}")
    except Exception as e:
        print(f"Error al actualizar la fecha de {file_path}: {e}")

def process_files_in_folder(folder_path):
    """Procesa todos los archivos JSON y sus fotos/videos en una carpeta."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_file_path = os.path.join(root, file)
                
                # Lee el JSON
                with open(json_file_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
                
                # Obtiene el nombre del archivo original (ej: "102D2X8351B.jpg")
                original_file_name = metadata.get("title")
                if not original_file_name:
                    print(f"No se encontró título en el JSON: {json_file_path}")
                    continue
                
                # Obtiene el timestamp de la fecha real
                photo_time = metadata.get("photoTakenTime", {}).get("timestamp")
                if not photo_time:
                    print(f"No se encontró 'photoTakenTime' en el JSON: {json_file_path}")
                    continue
                
                # Convierte el timestamp a formato UNIX
                timestamp = int(photo_time)
                
                # Busca el archivo asociado (foto o video)
                original_file_path = os.path.join(root, original_file_name)
                if os.path.exists(original_file_path):
                    update_file_date(original_file_path, timestamp)
                else:
                    print(f"Archivo no encontrado: {original_file_path}")

# Ruta específica para tu carpeta de respaldo de Google Fotos
carpeta_prueba = r"\\DS1522\home\Photos\Marc_Backup_Google\Takeout\Google Fotos"
process_files_in_folder(carpeta_prueba)
