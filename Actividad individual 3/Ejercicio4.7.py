from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass

class canidos(Animal):
    pass

class felinos(Animal):
    pass

class Perros(canidos):
    def get_sonido(self):
        return "Ladrido"

    def get_nombre_cientifico(self):
        return "Canis lupus familiaris"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Doméstico"
    
class Lobos(canidos):
    def get_sonido(self):
        return "Aullido"

    def get_nombre_cientifico(self):
        return "Canis lupus"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Bosque"
    
class Leones(felinos):
    def get_sonido(self):
        return "Rugido"

    def get_nombre_cientifico(self):
        return "Panthera leo"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Pradera"
    
class Gatos(felinos):
    def get_sonido(self):
        return "Maullido"

    def get_nombre_cientifico(self):
        return "Felis silvetris catus"

    def get_alimentos(self):
        return "Ratones"

    def get_habitat(self):
        return "Doméstico"
    
class PruebaAnimales:
    def __init__(self):
        animales = [Perros(), Lobos(), Leones(), Gatos()]

        for animal in animales:
            print(animal.get_nombre_cientifico())
            print(f"Sonido: {animal.get_sonido()}")
            print(f"Alimentos: {animal.get_alimentos()}")
            print(f"Habitat: {animal.get_habitat()}")
            print()

class Numerica(ABC):
    @abstractmethod
    def stringtostring(self):
        pass

    @abstractmethod
    def booleanequals(self, object):
        pass

    @abstractmethod
    def numericaSuma(self, numero):
        pass

    @abstractmethod
    def numericaResta(self, numero):
        pass

    @abstractmethod
    def numericaMultiplicacion(self, numero):
        pass

    @abstractmethod
    def numericaDivision(self, numero):
        pass

class Fraccion(Numerica):
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        
    def stringtostring(self):
        return f"{self.numerador}/{self.denominador}"
    
    def booleanequals(self, other):
        if not isinstance(other, Fraccion):
            return False
        return (self.numerador == other.numerador) & (self.denominador == other.denominador)
    
    def numericaSuma(self):
        return self.numerador + self.denominador
    
    def numericaResta(self):
        return self.numerador - self.denominador
    
    def numericaMultiplicacion(self):
        return self.numerador * self.denominador
    
    def numericaDivision(self):
        return self.numerador / self.denominador
    
class PruebaNumeros():
    def __init__(self):
        fraccion1 = Fraccion(1, 2)
        fraccion2 = Fraccion(3, 4)

        print("Fracción 1:", fraccion1.stringtostring())
        print("Fracción 2:", fraccion2.stringtostring())
        print()
        print("Suma:", fraccion1.numericaSuma())
        print("Resta:", fraccion1.numericaResta())
        print("Multiplicación:", fraccion1.numericaMultiplicacion())
        print("División:", fraccion1.numericaDivision())
        print("¿Son iguales?", fraccion1.booleanequals(fraccion2))
    

PruebaAnimales()
PruebaNumeros()