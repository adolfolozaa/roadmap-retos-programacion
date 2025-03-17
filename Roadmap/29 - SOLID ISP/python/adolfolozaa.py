'''
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.

'''
from abc import ABC, abstractmethod


#Incorrecto
class AnimalInterfaz(ABC):
    @abstractmethod
    def nadar(self):
        pass
    @abstractmethod
    def caminar(self):
        pass

class Fish(AnimalInterfaz):
    def nadar(self):
        return super().nadar()
    
    def caminar(self):     #los peces no caminan, incumple el Principio  SOLID de Segregación de Interfaces ISP
        return super().caminar()
    
#Correcto

class NadarInterfaz(ABC):
    @abstractmethod
    def nadar(self):
        pass

class CaminarInterfaz(ABC):
    @abstractmethod
    def caminar(self):
        pass

class AnimalTerrestre(CaminarInterfaz):
    def caminar(self, animal):
        print(f'El {animal} esta caminando')

class AnimalMarino(NadarInterfaz):
    def nadar(self, animal):
        print(f'El {animal} esta nadando')

class AnimalAnfibio(CaminarInterfaz, NadarInterfaz):
    def caminar(self, animal):
        print(f'El {animal} esta caminando')

    def nadar(self, animal):
        print(f'El {animal} esta nadando')

animal_marino = AnimalMarino()
animal_marino.nadar('delfin')

animal_terrestre = AnimalTerrestre()
animal_terrestre.caminar('perro')

animal_anfibio = AnimalAnfibio()
animal_anfibio.caminar('lagarto')
animal_anfibio.nadar('lagarto')


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
'''

class ImprimirColorInterfaz(ABC):
    @abstractmethod
    def imprimir_color(self, doc: str):
        pass        
class ImprimirBWInterfaz(ABC):
    @abstractmethod
    def imprimir_bw(self, doc: str):
        pass

class ScanningInterfaz(ABC):
    @abstractmethod
    def scaneando(self, doc:str) -> str:
        pass

class FaxingInterfaz(ABC):
    @abstractmethod
    def faxing(self, doc: str):
        pass

class ImprimirColor(ImprimirColorInterfaz):
    def imprimir_color(self, doc):
        print(f"imprimiendo en color el {doc} ahora")
        
class ImprimirBW(ImprimirBWInterfaz):
    def imprimir_bw(self, doc):
        print(f"imprimiendo en BW el {doc} ahora") 

class Multifuncion(ImprimirBWInterfaz, ImprimirColorInterfaz, ScanningInterfaz, FaxingInterfaz):
    def imprimir_bw(self, doc):
        print(f"imprimiendo en BW el {doc} ahora") 

    def imprimir_color(self, doc):
        print(f"imprimiendo en color el {doc} ahora")

    def scaneando(self, doc) -> str:
        print(f"escaneando el {doc} ahora")
        return f'retornando el {doc} escaneado'

    def faxing(self, doc):
        print(f"Faxeando el {doc} ahora")

imprimir_color = ImprimirColor()
imprimir_color.imprimir_color('CV ALA')

imprimir_bw = ImprimirBW()
imprimir_bw.imprimir_bw('CV ALA')

multifuncion = Multifuncion()
print(multifuncion.scaneando('CV ALA'))
multifuncion.faxing('CV ALA')
multifuncion.imprimir_bw('CV ALA')
multifuncion.imprimir_color('CV ALA')






