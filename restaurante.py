class Restaurant:
    
    # atributos por defecto
    horario_apertura = 12
    horario_cierre = 23 
    
    # atributos de inicializacion
    def __init__(self, nombre, tipo_comida) -> None:
        
        self.name = nombre
        self.cuisine_type = tipo_comida
        pass
    
    # metodos
    def describe_restaurante(self):
        print(f'Nombre: {self.name} de tipo {self.cuisine_type} ')
    
    def open_restaurante(self, hora):
        
        if hora >=self.horario_apertura and hora <= self.horario_cierre:
            print('El restaurante se encuentra abierto')
        else:
            print('El restaurante se encuentra cerrado')
            
    def cambiar_horario(self, nueva_hora_apertura, nueva_hora_cierre):
        
        self.horario_apertura = nueva_hora_apertura
        self.horario_cierre = nueva_hora_cierre
        
        print(f'Nuevo horario de {self.horario_apertura} a {self.horario_cierre}')
        pass

r1 = Restaurant('Mcdonals', 'fastfood')
r1.describe_restaurante()
r1.cambiar_horario(13, 22)
r1.open_restaurante(12.5)


r2 = Restaurant('Chillis', 'fastfood')
r2.describe_restaurante()
r2.open_restaurante(12.5)

