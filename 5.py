cantidad=float(input("Introduce la cantidad a invertir: "))
interes=float(input("Introduzca el interes anual: "))
anos=int(input("Introduzca la cantidad de años: "))
for i in range(anos):
    cantidad *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))