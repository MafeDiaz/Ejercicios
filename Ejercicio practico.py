hombre=0
mujer=0
acum=0
for i in range(1,11,1):

    genero=int(input("Ingrese 1 si es hombre o 2 si es mujer"))
    if genero==1:
        hombre = hombre + 1
    else:
        mujer = mujer + 1

    cantidadpersonas =hombre+mujer

print("Mujeres=", mujer)
print("Hombre=", hombre)  
print("Cantidad de personas", cantidadpersonas)          