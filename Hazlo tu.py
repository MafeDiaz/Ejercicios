print("Ingrese las notas obtenidas en los talleres")

notas =0
cantidad =0
for i in range(1,2,1):
    taller1=float(input("Ingrese la nota obtenida"))
    taller2=float(input("Ingrese la nota obtenida"))
    taller3=float(input("Ingrese la nota obtenida"))
    taller4=float(input("Ingrese la nota obtenida"))
    totalnotas= taller1+taller2+taller3+taller4

print("Nota final", totalnotas)    