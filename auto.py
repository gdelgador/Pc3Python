

class Auto:
    """Clase -> Molde la cual me permitirá generar objetos"""
    
    # variable
    color = 'rojo' # constantes
    
    # Atributos o variables o caracterísctas
    def __init__(self, modelo, marca, placa, fecha_fabricacion):
        """Inicializar un conjunto de variables a brindar a mi clase"""
        self.marca = marca # 
        self.modelo = modelo
        self.placa = placa
        self.fecha_fabricacion = fecha_fabricacion
        
    # funcionalidades - métodos - para que sirve?
    def encender_motor(self):
        print('Encendiendo el motor ....')
        pass

    def acelerar(self):
        print('Acelerando....')
        pass
    
    def realizar_cambios(self):
        print('Realizando el cambio')
        pass
    
    def frenar(self):
        print('Frenando')
        pass
    


# Generando objetos
auto1 = Auto('Mercedes Bens', 'Mercedes', 'AZ9454', 1995)
auto2 = Auto('Kia rio', 'Kia', 'PE789', 2011)


# de mis objetos puedo acceder a sus atributos y metodos

print(f'Auto1 - placa: {auto1.placa} ')
print(f'Auto2 - placa: {auto2.placa} ')


auto1.encender_motor()
auto1.acelerar()




