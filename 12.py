fras=input("Introduce una frase: ")
letra=input("Introduce una letra: ")
contador=0
for i in fras:
    if i==letra:
        contador+=1
print("En la frase '",fras,"' la letra '",letra,"' aparece ",contador," veces")