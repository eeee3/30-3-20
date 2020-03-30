num=int(input("Ingrese un numero positivo: "))
num1=1
contador=1
while num1<=num:
    for i in range(contador):
        print("*", end="")
    print()
    contador+=1
    num1+=1