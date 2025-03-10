import math
import random
import inspect
import warnings


# El examen consiste en distribuir creencias entre las hipótesis mutuamente contradictorias en cada una de las afirmaciones o pregunta que se realizan.

def es_distribucion_de_creencias(respuestas, funcion, enunciado):
    """
    Verifica que la respuesta sea una distribución de creencias.
    """
    suma_1 = math.isclose(
        sum([respuestas[r] for r in respuestas]),
        1.0
    )
    positivas_o_nulas = math.isclose(
        sum([respuestas[r]<0 for r in respuestas]),
        0.0
    )
    if not (suma_1 and positivas_o_nulas):
      warnings.warn(f"""La respuesta al enunciado {funcion} '{enunciado}' no es una distribución de creencias""", RuntimeWarning)

    return (suma_1 and positivas_o_nulas)

def maxima_incertidumbre(respuestas):
    """
    Si no se proveé una respuesta que sea una distribución de creencias, se construye una dividiendo la creencia en partes iguales.
    """
    n = len(respuestas)
    return {r: 1/n for r in respuestas}

#######################################
##### Selección Múltiple Semana 1 #####

random.seed(0)

def _1_1(enunciado = """Todas las opiniones son válidas porque no hay una forma correcta, universal, de evaluar las diferentes opiniones alternativas."""):

    respuestas = {}

    # Verdadero, no hay una forma correcta de evaluar las diferentes opiniones alternativas
    respuestas["Verdadero"] = 0.0

    # Falseo, sí existe una forma correcta de evaluar las diferentes opiniones alternativas
    respuestas["Falso"] = 0.0

    # Revisa si es una distribución de creencias (que sume 1)

    valida = es_distribucion_de_creencias(
        respuestas,
        inspect.currentframe().f_code.co_name,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)

def _1_2(enunciado = """Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. ¿Dónde está el regalo?"""):
    respuestas = {}
    respuestas["Caja 1"] = 0.0
    respuestas["Caja 2"] = 0.0
    respuestas["Caja 3"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        inspect.currentframe().f_code.co_name,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)

def _1_3(enunciado = """La ciencia tiene pretensión de alcanzar verdades, es decir, proposiciones que valgan para todas las personas más allá de sus subjetividades individuales. Las ciencias puramente formales, como la matemática, validan sus proposiciones derivando teoremas en sistemas axiomáticos cerrados sin incertidumbre. Las ciencias con datos, desde la física hasta las ciencias sociales, deben validar sus proposiciones en sistemas naturales abiertos que contienen siempre regiones ocultas a nuestra percepción. ¿Es posible determinar el valor de verdad de una proposición en contextos de incertidumbre si justamente tenemos incertidumbre sobre su estado real?"""):
    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    respuestas["Sí"] = 0.0
    respuestas["No"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)


def _1_4(enunciado = """Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Luego, una persona elige al azar una de las cajas que no contiene el regalo, y nos muestra que el regalo no está ahí adentro. ¿Cuál de todos los universos paralelos va a ocurrir? ¿El regalo está en la caja 1 y nos muestran la caja 1? ¿El regalo está en la caja 1 y nos muestran la caja 2? ... ¿El regalo está en la caja 3 y nos muestran la caja 2? ¿El regalo está en la caja 3 y nos muestran la caja 3?"""):
    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    # El regalo está en la caja 1
    respuestas["Regalo = 1, Abren = 1"] = 0.0
    respuestas["Regalo = 1, Abren = 2"] = 0.0
    respuestas["Regalo = 1, Abren = 3"] = 0.0
    # El regalo está en la caja 2
    respuestas["Regalo = 2, Abren = 1"] = 0.0
    respuestas["Regalo = 2, Abren = 2"] = 0.0
    respuestas["Regalo = 2, Abren = 3"] = 0.0
    # El regalo está en la caja 3
    respuestas["Regalo = 3, Abren = 1"] = 0.0
    respuestas["Regalo = 3, Abren = 2"] = 0.0
    respuestas["Regalo = 3, Abren = 3"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)


def _1_5(enunciado = """Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Luego, una persona elige al azar una de las cajas que no contiene el regalo y nos muestra que el regalo no está en la caja 2. ¿Dónde está el regalo?"""):
    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    # El regalo está en la caja 1
    respuestas["Regalo = 1"] = 0.0
    respuestas["Regalo = 2"] = 0.0
    respuestas["Regalo = 3"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)


def _1_6(enunciado = """La teoría de la probabilidad es usada como sistema de razonamiento en contextos de incertidumbre en todas las ciencias con datos. Sus reglas comenzaron a formalizarse a finales del siglo 18. En la actualidad, luego de 250 años, estamos presenciando el desarrollo de poderosos sistemas de inteligencia artificial. ¿Cuántas reglas de la probabilidad existen?"""):

    respuestas = {}
    # El regalo está en la caja 1
    respuestas["Menos de 2"] = 0.0
    respuestas["Entre 2 y 3"] = 0.0
    respuestas["Entre 4 y 7"] = 0.0
    respuestas["Entre 6 y 15"] = 0.0
    respuestas["Entre 16 y 31"] = 0.0
    respuestas["Entre 32 y 63"] = 0.0
    respuestas["Entre 64 y 127"] = 0.0
    respuestas["Entre 128 y 255"] = 0.0
    respuestas["Entre 256 y 511"] = 0.0
    respuestas["No existe un límite, se siguen descubriendo"] = 0.0


def _1_7(enunciado = """Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Nos permiten tirar un dado para reservar una de las cajas. La caja que reservamos será igual al módulo 3 del valor del dado + 1. Luego, una persona elige al azar una de las cajas que no contenga el regalo y no haya sido reservada. Supongamos que el dado salió 6 por lo que se reservó la caja 1. ¿Cuál de todos los universos paralelos va a ocurrir? ¿El regalo está en la caja 1 y nos muestran la caja 1? ¿El regalo está en la caja 1 y nos muestran la caja 2? ... ¿El regalo está en la caja 3 y nos muestran la caja 2? ¿El regalo está en la caja 3 y nos muestran la caja 3?"""):
    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    # El regalo está en la caja 1 y reservamos caja 1
    respuestas["Regalo = 1, Abren = 1"] = 0.0
    respuestas["Regalo = 1, Abren = 2"] = 0.0
    respuestas["Regalo = 1, Abren = 3"] = 0.0
    # El regalo está en la caja 2 y reservamos caja 1
    respuestas["Regalo = 2, Abren = 1"] = 0.0
    respuestas["Regalo = 2, Abren = 2"] = 0.0
    respuestas["Regalo = 2, Abren = 3"] = 0.0
    # El regalo está en la caja 3 y reservamos caja 1
    respuestas["Regalo = 3, Abren = 1"] = 0.0
    respuestas["Regalo = 3, Abren = 2"] = 0.0
    respuestas["Regalo = 3, Abren = 3"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)


def _1_8(enunciado = """Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Nos permiten tirar un dado para reservar una de las cajas. La caja que reservamos será igual al módulo 3 del valor del dado + 1. Luego, una persona elige al azar una de las cajas que no contenga el regalo y no haya sido reservada. Supongamos que el dado salió 6 por lo que se reservó la caja 1. ¿Dónde está el regalo?"""):
    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    respuestas["Regalo = 1"] = 0.0
    respuestas["Regalo = 2"] = 0.0
    respuestas["Regalo = 3"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)

def _1_9(enunciado = """En probabilidad, ¿cómo se predice un evento todavía no observado?"""):

    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    # El regalo está en la caja 1 y reservamos caja 1
    respuestas["Se ofrece la distribución de probabilidad marginal de la hipótesis a priori"] = 0.0
    respuestas["Se ofrece la distribución de probabilidad marginal de la hipótesis a posteriori"] = 0.0
    respuestas["Se propone la hipótesis que maximizó la predicción de los datos previamente observados"] = 0.0
    respuestas["Se proponen la hipótesis que maximiza la predicción de todos los datos observados"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)


def _1_10(enunciado = """En probabilidad, ¿cómo se incorpora la información contenida en un nuevo dato?"""):

    nombre = inspect.currentframe().f_code.co_name,

    respuestas = {}
    # El regalo está en la caja 1 y reservamos caja 1
    respuestas["Se preserva la creencia previa que sigue siendo compatible con el dato"] = 0.0
    respuestas["Se entrena el modelo, seleccionando los parámetros que mejor ajustan a los datos"] = 0.0

    valida = es_distribucion_de_creencias(
        respuestas,
        nombre,
        enunciado)

    if valida:
        return respuestas
    else:
        return maxima_incertidumbre(respuestas)

if __name__ == '__main__':
    print(_1_1())
    print(_1_2())
    print(_1_3())
    print(_1_4())
    print(_1_5())
    print(_1_6())
    print(_1_7())
    print(_1_8())
    print(_1_9())
    print(_1_10())
