'''
- Añade un elemento al principio.
- Añade varios elementos en bloque al final.
- Añade varios elementos en bloque en una posición concreta.
- Elimina un elemento en una posición concreta.
- Actualiza el valor de un elemento en una posición concreta.
- Comprueba si un elemento está en un conjunto.
- Elimina todo el contenido del conjunto.
'''
data = [1, 2, 3, 4, 5]
# anadir al final
data.append(6)
print(data)
# anadir bloque al inicio 
data.insert(0, 0)
print(data)

# anadir un bloque al final
data.extend([7, 8, 9])
print(data)

# anadir un bloque en posicion concreta
data[3:3] = [-1, -2, -3]  # slice
print(data)

# eliminar un elemento concreto
del data[3]
print(data)

# actualiza un elemento concreto
data[3] = -1
print(data)

# Comprueba si un dato esta en una estructura
print(f'comprobar si un elemento existe: {-1 in data}')

# eliminar todo el contenido
data.clear()
print(data)

'''
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.'''

# Union list  No sirve porque se duplican
data1 = [1, 2, 3, 4]
data2 = [5, 6, 7, 8]
data = data1 +data2
print(data)
# union sets
set1 = {1, 2, 3, 5}
set2 = {5, 6, 7}
union_set = set1.union(set2)
print(union_set)

# Interseccion
interseccion_set = set1.intersection(set2)
print(interseccion_set)

# diferencia.  resta los que se repiten
dif = set1.difference(set2)
print(dif)

#diferencia simetrica muestra los que no se repiten. solo resta el repetido y anade los del set2
dif_simet = set1.symmetric_difference(set2)
print(dif_simet)
