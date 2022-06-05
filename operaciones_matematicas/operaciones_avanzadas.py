import math


def get_factorial_recursivo(x: int)->int:
    """Retorna factorial x! de forma recursiva"""
    if x==1:
        return 1
    elif x>1:
        return x * get_factorial_recursivo(x-1)




def es_divisible(numero, i):
    """Evalua si el número es divisible por un número 'i' o no. Devuelve True o False"""
    return (numero % i == 0)


def es_primo(n: int)->bool:
    """Retorna True si el número ingresado es primo, en otro caso retorna False
    """
    primo = True
    x = int(math.sqrt(n)) + 1
    
    for i in range(2,x):
        if es_divisible(n, i):
            primo=False # demuestras que no es primo
            break
    
    return primo
    



