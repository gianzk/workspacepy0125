cantidad_numeros = int(input('Cuanto numero desea ingresar: '))
suma=0
for i in range(1,cantidad_numeros+1):
    suma+=i

print("la media es",suma/cantidad_numeros)
