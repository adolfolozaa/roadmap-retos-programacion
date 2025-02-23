'''
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
'''
def print_call(function):       #Decorador

    def print_function():
        print(f"La funcion {function.__name__} ha sido llamada")
        return function
    return print_function

@print_call
def example_function():
    pass

@print_call
def example_function2():
    pass
@print_call
def example_function3():
    pass

example_function()
example_function2()
example_function3()


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.

'''

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {counter_function.call_count}' veces.")
        return function

    counter_function.call_count = 0
    return counter_function


@call_counter
def example_funct():
    pass

@call_counter
def example_funct2():
    pass

@call_counter
def example_funct3():
    pass

example_funct2()
example_funct()
example_funct3()
example_funct2()
example_funct()
