'''
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
'''
# Correcta
class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'Open'

    def add_item(self, name: str, quantity: int, price: float)-> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total

class PaymentProcess(Order):
    def pay(self, order:Order, security_code: str)->float:
        print('Procesando el pago')
        print(f'Verificando codigo de seguridad: {security_code}')
        total = order.total_price()
        print(f'El total de su compra es: {total:.2f} dolares')
        order.status = 'PAID'

order = Order()

order.add_item('iphone', 2, 300 )
order.add_item('ipad', 5, 500)
order.add_item('macbook', 3, 1500)

process = PaymentProcess()
process.pay(order, '242526')
print(f'El estado de su orden es: {order.status}')

# Incorrecto

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        pass
    
    def sekd_email(self):
        pass

# Correcto
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserService:
    def save_to_database(self):
        pass

class EmailService:
    def sekd_email(self, email, message):
        pass


''' 
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
'''

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class User:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

class Loan():
    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append(
                {'user_id': user.id, 'book_title': book.title})
            return True
        return False
    
    def return_book(self, user, book):
        for loan in self.loans:
            if loan['user_id'] == user.id and loan['book_title'] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
            return False
    
class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False
    
    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False
            
        
book = Book('Sidharta', 'Hess', 4)
book = Book('Potter', 'Rollings', 6)
library = Library()
library.add_book('Sidharta')
library.add_book('Potter')
#print(book.author + '   ' + book.title + '    ' + str(book.copie))
print(library.books)

user = User('Adolfo', '1234', 'aloza@gmail.com')
user = User('Pedro', '1235', 'pedro@gmail.com')
library.add_user('Adolfo')
library.add_user('Pedro')
#print(user.name + '   ' + user.id + '    ' + user.email)
print(library.users)


loan = Loan()
libro = Loan.loan_book ('1234', 'Sidharta')
library.loans_service()
#print(loan.loan_book)









        