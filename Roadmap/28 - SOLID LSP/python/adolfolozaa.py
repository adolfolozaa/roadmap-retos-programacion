'''
EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *

'''

#incorrecto

class Birds:
    def fly(self):
        return 'flying'
    

class Chicken(Birds):
    def fly(self):
        raise Exception('Los pollos no vuelan')
    
'''birds = Birds()
print(birds.fly())
chicken = Chicken()
print(chicken.fly()) # es incorrecto porque no se pueden intercambiar las clases, tuvimos que modificar el comportamiento de la funcion fly()'''

# Correcto
class Birds:
    def move(self):
        return 'moving'
    
class Chicken(Birds):
    def move(self):
        return 'walk'
    
birds = Birds()
print(birds.move())
chicken = Chicken()
print(chicken.move()) # deberiamos probar intercambiandolos y ver que no afecten




'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.

'''

class Vehiculos:
    def __init__(self, speed = 0) -> None:
        self.speed = speed
    def acelerar(self, increment):
        self.speed += increment
        print(f'velocidad actual: {self.speed} Km/h ')

    def frenar(self, decrement):
        self.speed -=  decrement
        if self.speed <= 0:
            self.speed = 0
        print(f'velocidad actual: {self.speed} Km/h ')

class Suv(Vehiculos):
    def accelerate(self, increment):
        print('El  SUV esta acelerando')
        super().acelerar(increment)

    def brake(self, decrement):
        print('El SUV esta frenando')
        super().frenar(decrement)

class Sedan(Vehiculos):
    def accelerate(self, increment):
        print('El  Sedan esta acelerando')
        super().acelerar(increment)

    def brake(self, decrement):
        print('El Sedan esta frenando')
        super().frenar(decrement)

class Moto(Vehiculos):
    def accelerate(self, increment):
        print('La Moto esta acelerando')
        super().acelerar(increment)

    def brake(self, decrement):
        print('La Moto esta frenando')
        super().frenar(decrement)

#Añadimos otra funcion para probar acelerar y frenar 
def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)

#vehiculos = Vehiculos()
suv = Suv()
suv.accelerate(10)
suv.brake(5)

sedan = Sedan()
sedan.accelerate(12)
sedan.brake(6)

moto = Moto()
moto.accelerate(8)
moto.brake(4)

test_vehicle(suv)
test_vehicle(sedan)
test_vehicle(moto)






