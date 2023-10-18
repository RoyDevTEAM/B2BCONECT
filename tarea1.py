"""
#Este codigo es para sumar 2 numeros con 2 variables
numero1 = input("Por favor ingrese el primer numero que desee sumar:\n")
numero2 = input("Ahora ingrese el segundo numero que sumara al primero:\n")
#En es te apartado iran las operaciones que realizaremos para ejecutar el comando
numero3= int(numero1)+int(numero2)
print("El resultado de sumar ",numero1," y ",numero2," es ",numero3)
#Fase uno completada"""
#El sieguiente ejercicio es para allar el descuento de una tienda de ropa
tasadesuento=0.20
compra=input("Ingrese porfavor el monto de su compra:\n")
if float(compra)>400:
    print("Usted adquirio un descuento del 20% en su compra")
    descuento= float(compra)*tasadesuento
    costototal=float(compra)-descuento
    print(f"Total a pagar {costototal}")
else:
    print("Usted no adquirio ningun descuento en su compra")
    print(f"Total a pagar {compra}")

"""nombre = "Juan"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años.")"""
