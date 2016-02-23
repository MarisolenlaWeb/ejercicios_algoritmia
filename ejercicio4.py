mensaje=input("Ingresa letras con vocales y consonantes...NADA MAS\n")
vocales = 0
cons = 0
omit=["1","2","3","4","5","6","7","8","9","0", " ", "-", "_", "/"]
for i in mensaje:
    if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocales += 1
    elif i in omit:
        cons += 0
    else:
        cons += 1

print ("Tu mensaje tiene este numero de vocales: " , vocales)

print ("Tu mensaje tiene este numero de consonantes: " , cons)
