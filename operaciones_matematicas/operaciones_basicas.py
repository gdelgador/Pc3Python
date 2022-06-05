"""Contiene funcionalidades del tipo suma, resta, multiplicacion ..."""
import math

def sumar(x:float, y: float)->float :
    """Retorna la suma de x + y"""
    return x + y

def restar(x:float, y: float)->float :
    """Retorna la resta de x - y"""
    return x - y

def multiplicar(x:float, y: float)->float :
    """Retorna la multiplicacion de x * y"""
    return x * y

def dividir(x:float, y: float)->float :
    """Retorna la división de x / y"""
    return x / y


if __name__ == '__main__':
    
    s = sumar(7,8)
    print(s == 15)
    
    
    
    pass