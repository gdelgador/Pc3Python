# Escribe un código el cual consista en un menú y contenga 5 funcionalidades

# 1. Importar librerias -> aquella la cual contenga un conjunto de funciones que puedo aprovechar

# import <nombre_archivo> (opcional) as nombre_alias
# from <nombre_carpeta> import <nombre_archivo> (opcional) as nombre_alias
# import <nombre_carpeta>.<nombre_archivo>  (opcional) as nombre_alias
import ingreso_datos
from operaciones_matematicas import operaciones_basicas as basics
from operaciones_matematicas import operaciones_avanzadas as a
import mimes.mimes as m


# 2. Constantes (CONTANTES SE ESCRIBEN EN MAYUSCULAS)
BIENVENIDA = "Bienvenido al menú interactivo"
MSG = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) factorial de un número
    3) Evaluar si un número es primo
    4) MIMES según nombre de archivo
    5) Piramide Mario
    6) Salir
    Opcion: """

# 3. funciones y/o clases
def opcion1():
    n1 = ingreso_datos.get_float('Ingrese el primer numero: ')
    n2 = ingreso_datos.get_float('Ingrese el segundo numero: ')
    
    s = basics.sumar(n1, n2)
    print(f'la suma de los numero es  : {s}')

def opcion2():
    x = ingreso_datos.get_int()
    if x<=0:
        print('No se puede calcular')
    else:
        factorial = a.get_factorial_recursivo(x)
        print(f'{x}! = {factorial}')

def opcion3():
    x = ingreso_datos.get_int()
           
    if a.es_primo(x):
        print('Numero es primo')
    else:
        print('Numero no es primo')

def opcion4():
    # obtenemos dato
    file_name  = ingreso_datos.get_str_clean('Ingrese nombre de archivo: ')
    file_name = file_name.lower()
    
    # imprimimos
    m.get_mime(file_name)
    pass

def opcion5():
    
    h = ingreso_datos.get_int('Ingrese la altura del triangulo: ')
    
    if h>0 and h<=8:
        for i in range(h+1):
            espacios = h-i
            print(espacios*" " + "#"*i)
    else:
        print('La altura del triangulo debe ser entre 1-8')
        return opcion5()
    
def main():
    print(BIENVENIDA)
    while True:
        opcion = input(MSG)
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            opcion4()
        elif opcion == '5':
            opcion5()
        elif opcion =='6':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. mi programa
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)
