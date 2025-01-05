suma = 3 +7 # int

# Opcion 1
print("El valor de la suma es "+  str(suma)) # str(suma) -> concadenacion solo sirve para strings

# Opcion 2 -> Mejor opcion
print(f"El valor de la suma es: {suma}") # formatea el numero a texto

# opcion 3 -> Otra buena Opcion
print("El valor de la suma es: {}".format(suma))

#opcion 4 -> coma parametros
print("El valor de la suma es:",suma)


# viendo para variables 
fecha=2025
curso="Python"
print("el valor :"+ str(suma)+ "para el dia " + str(fecha)+"del curso"+curso)
print(f"El valor: {suma} para el dia {fecha} del curso {curso}" ) #(ok)
print("El valor: {} para el dia {} del curso {}".format(suma,fecha,curso))#(ok)
print("El valor de la suma es ",suma,"para el dia",fecha,"del curso",curso)

