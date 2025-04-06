def evaluar_con_manejo_errores(estudiante, correctas):
    """
    Evalúa las respuestas del estudiante con manejo robusto de errores.
    
    Args:
        estudiante: Módulo importado del estudiante
        correctas: Módulo con las respuestas correctas
    
    Returns:
        tuple: (respuestas_correctas, log_evidence, errores)
    """
    import numpy as np
    import inspect
    import traceback
    
    creencias = dict(inspect.getmembers(estudiante, inspect.isfunction))
    realidad = dict(inspect.getmembers(correctas, inspect.isfunction))
    
    respuestas_correctas = {}
    log_evidence = {}
    errores = {}
    
    # Valor mínimo de probabilidad para evitar -inf
    epsilon = 1e-10
    
    for nombre_funcion in [k for k in realidad.keys() if k.startswith("_")]:
        try:
            # Verificar si la función existe en el código del estudiante
            if nombre_funcion not in creencias:
                errores[nombre_funcion] = "Función no implementada"
                log_evidence[nombre_funcion] = np.log2(epsilon)
                continue
                
            # Obtener la respuesta correcta
            resp_correcta = realidad[nombre_funcion]()
            respuestas_correctas[nombre_funcion] = resp_correcta
            
            # Obtener distribución de creencias del estudiante
            distribucion_estudiante = creencias[nombre_funcion]()
            
            # Verificar si la distribución es válida
            if not isinstance(distribucion_estudiante, dict):
                errores[nombre_funcion] = "La respuesta no es un diccionario"
                log_evidence[nombre_funcion] = np.log2(epsilon)
                continue
                
            if resp_correcta not in distribucion_estudiante:
                errores[nombre_funcion] = f"La respuesta correcta '{resp_correcta}' no está en las opciones"
                log_evidence[nombre_funcion] = np.log2(epsilon)
                continue
            
            # Calcular log evidence con protección contra -inf
            prob_asignada = max(distribucion_estudiante[resp_correcta], epsilon)
            log_evidence[nombre_funcion] = np.log2(prob_asignada)
            
        except Exception as e:
            errores[nombre_funcion] = f"Error: {str(e)}\n{traceback.format_exc()}"
            log_evidence[nombre_funcion] = np.log2(epsilon)
    
    return respuestas_correctas, log_evidence, errores
