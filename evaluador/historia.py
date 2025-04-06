import json
import os
import numpy as np
from datetime import date

class SeguimientoProgreso:
    """
    Clase para gestionar el seguimiento del progreso de los estudiantes
    a lo largo de múltiples evaluaciones.
    """
    
    def __init__(self, ruta_base="./"):
        self.ruta_base = ruta_base
        self.archivo_historico = "historico_evaluaciones.json"
    
    def cargar_historico(self, carpeta_estudiante):
        """Carga el histórico de evaluaciones de un estudiante"""
        ruta_archivo = os.path.join(self.ruta_base, carpeta_estudiante, self.archivo_historico)
        
        if not os.path.exists(ruta_archivo):
            return []
        
        try:
            with open(ruta_archivo, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar histórico de {carpeta_estudiante}: {e}")
            return []
    
    def guardar_historico(self, carpeta_estudiante, datos_historico):
        """Guarda el histórico de evaluaciones de un estudiante"""
        ruta_archivo = os.path.join(self.ruta_base, carpeta_estudiante, self.archivo_historico)
        
        try:
            with open(ruta_archivo, 'w') as f:
                json.dump(datos_historico, f, indent=4)
            return True
        except Exception as e:
            print(f"Error al guardar histórico de {carpeta_estudiante}: {e}")
            return False
    
    def registrar_evaluacion(self, carpeta_estudiante, num_evaluacion, log_evidence, errores=None):
        """Registra una nueva evaluación en el histórico del estudiante"""
        historico = self.cargar_historico(carpeta_estudiante)
        
        # Convertir log_evidence a probabilidades
        probs = {k: 2**v for k, v in log_evidence.items() if not np.isinf(float(v))}
        
        # Calcular puntaje (producto de probabilidades)
        puntaje = np.prod(list(probs.values())) if probs else 0
        
        # Crear registro de la evaluación actual
        evaluacion_actual = {
            "fecha": date.today().isoformat(),
            "num_evaluacion": num_evaluacion,
            "log_evidence": log_evidence,
            "probabilidades": probs,
            "puntaje": float(puntaje),
            "errores": errores if errores else {}
        }
        
        # Añadir al histórico
        historico.append(evaluacion_actual)
        
        # Guardar histórico actualizado
        return self.guardar_historico(carpeta_estudiante, historico)
    
    def generar_informe_progreso(self, carpeta_estudiante):
        """Genera un informe de progreso del estudiante basado en su histórico"""
        historico = self.cargar_historico(carpeta_estudiante)
        
        if not historico:
            return "No hay datos históricos disponibles."
        
        # Ordenar por número de evaluación
        historico_ordenado = sorted(historico, key=lambda x: x["num_evaluacion"])
        
        # Extraer puntajes y fechas
        puntajes = [h["puntaje"] for h in historico_ordenado]
        fechas = [h["fecha"] for h in historico_ordenado]
        evaluaciones = [h["num_evaluacion"] for h in historico_ordenado]
        
        # Calcular tendencia
        if len(puntajes) >= 2:
            tendencia = "positiva" if puntajes[-1] > puntajes[-2] else "negativa"
        else:
            tendencia = "neutral"
        
        # Generar informe
        informe = f"Informe de Progreso para {carpeta_estudiante}\n"
        informe += f"===================================\n\n"
        informe += f"Evaluaciones completadas: {len(historico)}\n"
        informe += f"Puntaje más reciente: {puntajes[-1]:.4f} (Evaluación {evaluaciones[-1]})\n"
        informe += f"Puntaje promedio: {sum(puntajes)/len(puntajes):.4f}\n"
        informe += f"Tendencia: {tendencia}\n\n"
        
        informe += "Historial de Puntajes:\n"
        for i, (eval_num, fecha, puntaje) in enumerate(zip(evaluaciones, fechas, puntajes)):
            informe += f"  Evaluación {eval_num} ({fecha}): {puntaje:.4f}\n"
        
        return informe
    
    def generar_informe_curso(self, carpetas_estudiantes):
        """Genera un informe comparativo de todos los estudiantes"""
        informe = "Informe del Curso\n"
        informe += "=================\n\n"
        
        datos_estudiantes = []
        
        for estudiante in carpetas_estudiantes:
            historico = self.cargar_historico(estudiante)
            if not historico:
                continue
                
            # Obtener la evaluación más reciente
            ultima_eval = max(historico, key=lambda x: x["num_evaluacion"])
            
            datos_estudiantes.append({
                "estudiante": estudiante,
                "ultimo_puntaje": ultima_eval["puntaje"],
                "evaluacion": ultima_eval["num_evaluacion"],
                "fecha": ultima_eval["fecha"]
            })
        
        # Ordenar por puntaje (descendente)
        datos_ordenados = sorted(datos_estudiantes, key=lambda x: x["ultimo_puntaje"], reverse=True)
        
        # Generar tabla de clasificación
        informe += "Clasificación basada en la evaluación más reciente:\n\n"
        
        for i, datos in enumerate(datos_ordenados, 1):
            informe += f"{i}. {datos['estudiante']}: {datos['ultimo_puntaje']:.4f} "
            informe += f"(Evaluación {datos['evaluacion']}, {datos['fecha']})\n"
        
        return informe
