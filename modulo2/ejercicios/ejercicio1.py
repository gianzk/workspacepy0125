#bucle infinito

flag=True
while flag:
    print("bucle infinito")
    valor=input("ingrese S/N si desea continuar o terminar el proceso: ")
    if valor.upper()=="N":
        break
        #flag=False
    print("esto se ejecuta si es que utilizo el flag con break no ")


