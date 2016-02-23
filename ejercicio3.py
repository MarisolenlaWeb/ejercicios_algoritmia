n1 =int(input("Ingresa numero 1: "))
n2 =int(input("Ingresa numero 2: "))
op =input("Ingresa operador matematico: ")
total = 0

if op == "+" :
    total = n1 + n2
    print(total)

elif op == "*":
    total = n1 * n2
    print(total)

elif op == "/":
    total = n1 / n2
    print(total)

elif op == "-":
    total = n1 - n2
    print(total)
