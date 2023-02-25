count=0 #definir variable númerica e iniciar antes del ciclo
total=0
for i in range(1,6,1):
    #Aqui instrucciones que deseas repetir
    price=int(input("Ingrese un valor:"))
    cantidad=int(input("Ingrese la cantidad:"))
    count=count+1 #iniciar el contador dentro del ciclo
    subtotal=price*cantidad
    print("Subtotal= ",subtotal)
    total=total+subtotal

print("El total a pagar es", total)
billete=int(input("Ingrese el valor del billete"))
cambio=billete-total

print ("El billete recibido es=", billete)
print("Su cambio es= ",cambio)

#print("Se registraron ",count, "referencias")
