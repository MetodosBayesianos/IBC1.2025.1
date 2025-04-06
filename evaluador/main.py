import os
import importlib
import inspect
import numpy as np
from datetime import date

# Importar funciones auxiliares (creadas en los artefactos anteriores)
# Nota: Estas importaciones deberían ajustarse según la organización real del código
from evaluador import evaluar_con_manejo_errores
from retroalimentacion import generar_retroalimentacion, escribir_evaluacion_con_feedback
from historia import SeguimientoProgreso
from git import commit_and_push_evaluacion

def evaluar_estudiantes(ruta_modulos=".", modulo_correctas="correctas", 
                        num_evaluacion=1, hacer_commit=True):
    """
    Función principal para evaluar a todos los estudiantes.
    
    Args:
        ruta_modulos (str): Ruta base donde se encuentran las carpetas de estudiantes
        modulo_correctas (str): Nombre del módulo con las respuestas correctas
        num_evaluacion (int): Número de la evaluación actual
        hacer_commit (bool): Si es True, realiza commit y push de los resultados
    """
    # Importar módulo de respuestas correctas
    correctas = importlib.import_module(modulo_correctas)
    
    # Obtener carpetas de estudiantes
    carpetas_estudiantes = [
        nombre for nombre in os.listdir(ruta_modulos) 
        if os.path.isdir(os.path.join(ruta_modulos, nombre)) 
        and nombre.startswith("estudiante")
    ]
    
    # Inicializar seguimiento de progreso
    seguimiento = SeguimientoProgreso(ruta_modulos)
    
    for carpeta in carpetas_estudiantes:
        try:
            # Importar módulo del estudiante
            try:
                nombre_modulo = f"{carpeta}.enunciado"
                estudiante = importlib.import_module(nombre_modulo)
                print(f"Módulo '{carpeta}' importado correctamente.")
            except ImportError as e:
                print(f"Error al importar el módulo '{nombre_modulo}': {e}")
                continue
            
            # Evaluar respuestas con manejo de errores
            respuestas_correctas, log_evidence, errores = evaluar_con_manejo_errores(
                estudiante, correctas
            )
            
            # Generar retroalimentación personalizada
            retroalimentacion = {}
            for nombre_funcion in respuestas_correctas:
                if nombre_funcion in errores:
                    retroalimentacion[nombre_funcion] = f"Error: {errores[nombre_funcion]}"
                else:
                    try:
                        distribucion = estudiante.__dict__[nombre_funcion]()
                        retroalimentacion[nombre_funcion] = generar_retroalimentacion(
                            nombre_funcion, distribucion, respuestas_correctas[nombre_funcion]
                        )
                    except Exception as e:
                        retroalimentacion[nombre_funcion] = f"No se pudo generar retroalimentación: {str(e)}"
            
            # Escribir archivo de evaluación
            fecha_actual = date.today()
            archivo_evaluacion = f"{carpeta}/evaluacion{num_evaluacion}.txt"
            
            escribir_evaluacion_con_feedback(
                archivo_evaluacion, fecha_actual, respuestas_correctas, 
                log_evidence, errores, retroalimentacion
            )
            
            print(f"Evaluación de {carpeta} completada. Escrita en {archivo_evaluacion}")
            
            # Registrar en el histórico
            seguimiento.registrar_evaluacion(carpeta, num_evaluacion, log_evidence, errores)
            
            # Generar informe de progreso
            informe_progreso = seguimiento.generar_informe_progreso(carpeta)
            with open(f"{carpeta}/progreso.txt", 'w') as f:
                f.write(informe_progreso)
            
            # Realizar commit y push si está habilitado
            if hacer_commit:
                exito = commit_and_push_evaluacion(carpeta)
                if exito:
                    print(f"Commit y push realizados para {carpeta}")
                else:
                    print(f"No se pudo realizar commit y push para {carpeta}")
        
        except Exception as e:
            print(f"Error general al procesar {carpeta}: {e}")
    
    # Generar informe del curso
    informe_curso = seguimiento.generar_informe_curso(carpetas_estudiantes)
    with open("informe_curso.txt", 'w') as f:
        f.write(informe_curso)
    
    print("Evaluación de todos los estudiantes completada.")

# Si se ejecuta como script principal
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Sistema de evaluación para Inferencia Bayesiana Causal')
    parser.add_argument('--ruta', default='.', help='Ruta base de las carpetas de estudiantes')
    parser.add_argument('--correctas', default='correctas', help='Módulo con respuestas correctas')
    parser.add_argument('--evaluacion', type=int, default=1, help='Número de evaluación')
    parser.add_argument('--no-commit', action='store_true', help='No realizar commit automático')
    
    args = parser.parse_args()
    
    evaluar_estudiantes(
        ruta_modulos=args.ruta,
        modulo_correctas=args.correctas,
        num_evaluacion=args.evaluacion,
        hacer_commit=not args.no_commit
    )
