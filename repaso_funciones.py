class persona():
    def __init__(self,nombre,apellido,dni) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni

    def saludar(self):
            return  f"Hola {self.nombre.capitalize()}"


dario = persona("Nestor ","sbarbati",34149964)
print(dario.saludar())