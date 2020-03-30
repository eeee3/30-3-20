num=int(input("Introduce un numero positivo mayor que dos: "))
num1=2
while num%num1 !=0:
    num1+= 1
if num1==num:
    print(num, " es primo")
else:
    print(num, " no es primo")