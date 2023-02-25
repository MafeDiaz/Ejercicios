gasto = "s"
presupuesto = 150000
cantgast = 0

while gasto == "s" or gasto=="S":
    print("Presupuesto inicial", presupuesto)
    vgasto = int(input("Ingrese el valor gasto:\n"))
    presupuesto = presupuesto-vgasto
    cantgast = cantgast + 1
    print("Valor gasto", vgasto)
    print("Nuevo presupuesto", presupuesto)
    
    if cantgast == 3:
        print ("Usted supero su limite de gastos los cuales son 3")
        
    else:
        gasto = input("Desea registrar un nuevo gasto? oprima s/S para registrar o cualquier tecla para salir: \n")
    
    print ("El total de sus gastos fue = ", vgasto)    
    print ("Su nuevo presupuesto = ", presupuesto)
