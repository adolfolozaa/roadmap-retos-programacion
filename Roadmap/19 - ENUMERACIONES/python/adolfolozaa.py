'''
EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 '''
from enum import Enum

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

def get_days(number: int):
    print(Weekday(number).name)

get_days(6)

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
'''

class OrderStatus(Enum):
    Pendiente = 1
    Enviado = 2
    Entregado = 3
    Cancelado = 4

'''pedidos = {'pedido1': 1, 'pedido2':2, 'pedido3': 3, 'pedido4':4}
# ruta  pendiente --> enviado --> entregado o pendiente --> cancelado

print(Pedidos(4).name)'''

class Order:
    status = OrderStatus.Pendiente

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.Pendiente:
            self.status = OrderStatus.Enviado
            self.display_status()
        else:
            print('El pedido ya ha sido enviado o cancelado')

        
    def deliver(self):
        if self.status == OrderStatus.Enviado:
            self.status = OrderStatus.Entregado
            self.display_status()
        else:
            print('El pedido necesita ser enviado antes de entregarse')

    def cancel(self):
        if self.status != OrderStatus.Entregado:
            self.status = OrderStatus.Cancelado
            self.display_status()

        else:
            print('El pedido ya se ha entregado')

    def display_status(self):
        print(f'el estado del pedido {self.id} es: {self.status.name}')


order_1 = Order(1)
order_1.deliver()
order_1.cancel()
order_1.ship()
order_1.deliver()
        



