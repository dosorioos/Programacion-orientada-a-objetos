#Area y circunferencia 
import numpy

radio = float(input("ingrese el radio del circulo: "))
area = numpy.pi*radio**2
L = 2*radio*numpy.pi

print("El área del circulo es:", area)
print("La longitud de la circunferencia es:", L)
