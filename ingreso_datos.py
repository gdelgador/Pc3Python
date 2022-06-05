"""Contiene Funciones para el ingreso de los datos"""


def get_int(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return get_int(msg)

def get_float(msg: str='Ingrese un número decimal: ')->float:
    """Solicita un número decimal"""
    try:
        x = float(input(msg))
        return x
    except:
        return get_float(msg)
    
def get_str_clean(msg:str='Ingrese un texto: ')->str:
    """Permite el ingreso de un dato de tipo texto, limpiando espacios"""
    response = input(msg)
    return response.strip()