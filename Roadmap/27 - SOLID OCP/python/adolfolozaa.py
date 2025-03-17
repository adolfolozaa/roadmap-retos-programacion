from abc import ABC, abstractmethod


'''
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
'''
#incorrecta
class Form:
    def draw(self):
        print('Dibujar forma cuadrado')

    #sigo añadiendo codigo a mi clase original cuando quiero dibujar un circulo

    def dra_circle(self):
        print('Dibujar forma circulo')

#correcta

class Form:   #No se topa mas, solo se añaden mas clases adicionales
    def draw(self):
        pass

class Square(Form):
    def draw(self):
        print('Dibujar forma cuadrado')


class Circle(Form):
    def draw(self):
        print('Dibujar forma circulo')

class Triangle(Form):
    def draw(self):
        print('Dibujar forma triangulo')



'''
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
'''

#Creamos clases abstractas con from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Operation):
    def execute(self, a, b):
        return a + b
    
class Substraction(Operation):
    def execute(self, a, b):
        return a - b
    
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
class Division(Operation):
    def execute(self, a, b):
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b
    
class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f'La Operacion {name} no existe')
        return self.operations[name].execute(a, b)
    
calculator = Calculator()
calculator.add_operation('addition', Addition())
calculator.add_operation('substraction', Substraction())
calculator.add_operation('multiplication', Multiplication())
calculator.add_operation('division', Division())
calculator.add_operation('power', Power())

print(calculator.calculate('addition', 10, 5))
print(calculator.calculate('substraction', 10, 5))
print(calculator.calculate('multiplication', 10, 5))
print(calculator.calculate('division', 10, 5))
print(calculator.calculate('power', 10, 5))
