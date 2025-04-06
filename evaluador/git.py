import os
import subprocess
from datetime import date

def commit_and_push_evaluacion(carpeta_estudiante):
    """
    Realiza commit y push de los archivos de evaluación en el repositorio del estudiante.
    
    Args:
        carpeta_estudiante (str): Ruta a la carpeta del estudiante
    
    Returns:
        bool: True si el proceso fue exitoso, False en caso contrario
    """
    try:
        # Cambiar al directorio del estudiante
        os.chdir(carpeta_estudiante)
        
        # Añadir el archivo de evaluación al staging
        subprocess.run(["git", "add", "evaluacion1.txt"], check=True)
        
        # Crear el commit con la fecha actual
        fecha_actual = date.today().strftime("%Y-%m-%d")
        mensaje_commit = f"Evaluación del {fecha_actual}"
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
        
        # Push al repositorio remoto
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        # Volver al directorio original
        os.chdir("..")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error en Git para {carpeta_estudiante}: {e}")
        # Volver al directorio original en caso de error
        os.chdir("..")
        return False
