import random
import time
import threading

'''
* EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
'''
def get_square(val):
	print (val ** 2)
def caller(func, val):
	val = val*2
	return func(val)
#caller(get_square, 5)


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 '''

def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
        confirm_callback(dish_name)
        time.sleep(random.randint(1,10))
        
        ready_callback(dish_name)
        time.sleep(random.randint(1,10))

        
        delivered_callback(dish_name)
        time.sleep(random.randint(1,10))
		
    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
	print(f'Tu pedido   {dish_name}     ha sido confirmado')
	
def order_ready(dish_name: str):
	print(f'Tu pedido   {dish_name}     esta listo')    
	
def order_delivered(dish_name: str):
	print(f'Tu pedido   {dish_name}     ha sido entregado')

order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Salami", confirm_order, order_ready, order_delivered)
order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza Vegetariana", confirm_order, order_ready, order_delivered)




