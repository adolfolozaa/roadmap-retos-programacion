'''
 EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
'''
 
for numero in range(1,11):
    print(str(numero) + ' ', end="")
    if numero == 10:
        print('\n')

numero = 1
while numero < 11:
    print(str(numero) + ' ', end="")
    if numero == 10:
        print('\n')
    numero += 1

mytuple = (1,2,3,4,5,6,7,8,9,10)
myit = iter(mytuple)

print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print(str(next(myit)) + ' ', end ='')
print('\n')


'''
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 '''
def count_ten(i=1):
    if i <= 10:
        print(str(i) + ' ', end="")
        count_ten(i + 1)

        if i == 10:
            print('\n')

count_ten()

# iterar lista
for e in [1, 2, 3, 4]:
    print(e)

# iterar set
for e in {1, 2, 3, 4}:
    print(e)

# iterar tuplas
for e in (1, 2, 3, 4):
    print(e)

# iterar diccionario
for e in {1: 'a', 2: 'b', 3:'c', 4:'d'}:
    print(e)

# iterar diccionario values
for e in {1: 'a', 2: 'b', 3:'c', 4:'d'}.values():
    print(e)

# iterar  indice y valor
for e, f in enumerate(['a', 'b', 'c', 'd']):
    print(f' indice: {e} y su valor {f}')

# lista de manera concisa (complexion list)
print(*[i for i in range(1,11)], sep=' ')

# cadena de texto
for c in 'Pyhton':
    print(c)

# iterar lista en reversa
for e in reversed([1, 2, 3, 4]):
    print(e)

