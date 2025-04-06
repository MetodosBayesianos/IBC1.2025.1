import random

# Fijar una semilla global para asegurar que las respuestas aleatorias sean consistentes
# entre diferentes ejecuciones y para todos los estudiantes
random.seed(42)

# Generamos las respuestas aleatorias una vez al inicio
respuestas_prefijadas = {}

def _1_1():
    """
    No hay una forma correcta de evaluar diferentes opiniones alternativas.
    Respuesta correcta: Falso
    """
    return "Falso"

def _1_2():
    """
    Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías.
    ¿Dónde está el regalo?
    
    En lugar de generar una respuesta aleatoria cada vez, usamos un valor prefijado
    o lo generamos una sola vez y lo almacenamos.
    """
    if '_1_2' not in respuestas_prefijadas:
        # Solo se ejecuta la primera vez
        caja_correcta = random.randrange(3)
        respuestas_prefijadas['_1_2'] = f"Caja {caja_correcta + 1}"
        
    return respuestas_prefijadas['_1_2']

# Inicializar todas las respuestas aleatorias al cargar el módulo
# Esto asegura que se generen una sola vez
def inicializar_respuestas():
    """Inicializa todas las respuestas aleatorias"""
    # Llamar a todas las funciones que generan respuestas aleatorias
    _1_2()  # Esto generará y almacenará la respuesta
    
    print("Respuestas correctas inicializadas:")
    for nombre, valor in respuestas_prefijadas.items():
        print(f"  {nombre}: {valor}")

# Inicializar al cargar
inicializar_respuestas()
