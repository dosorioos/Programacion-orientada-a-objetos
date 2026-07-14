class Pedido:
    def __init__(self):
        pass
 
    def pedido(self, primer_plato, valor_primer_plato, bebida, valor_bebida, segundo_plato = None, 
                 valor_segundo_plato = 0, postre = None, valor_postre = 0 ):
        total = valor_bebida + valor_primer_plato
        descripcion = primer_plato

        if segundo_plato is not None:
            total += valor_segundo_plato
            descripcion += f" + {segundo_plato}"
        
        if postre is not None:
            total += valor_postre
            descripcion += f" + {postre}"

        descripcion += f" + {bebida}"
        print(f"El costo total de {descripcion} es: ${total}")

class Suma:
    def __init__(self):
        pass

    def suma_enteros(self,a,b,c=0):
        suma = a + b
        if c != 0:
            suma += c
        
        print(f"El resultado de la suma de los numeros enteros es: {suma}")

    def suma_decimales(self,a,b,c=0.0):
        suma = a + b
        if c != 0:
            suma += c
        
        print(f"El resultado de la suma de los numeros decimales es: {suma}")
    
Pedido1 = Pedido()
Pedido1.pedido("Sancocho",5000,"Gaseosa",2000)
Pedido2 =Pedido()
Pedido2.pedido("Crema de Verduras",5000,"Gaseosa",2000,"Churrasco",6000)
Pedido3 =Pedido()
Pedido3.pedido("Crema de espinacas",5000,"Gasesosa",2000,"Salmon",10000,"Tiramisu",5000)
Suma1 = Suma()
Suma2 = Suma()
Suma1.suma_enteros(2,4)
Suma2.suma_enteros(2,4,6)
Suma1.suma_decimales(2.5,4.5)
Suma2.suma_decimales(2.5,4.5,6.5)


        

