header="name,fecha,direccion,pedido,estado"
cadena_sucia="gian     ,01/01/25,calle x urb z,464967979,pagado"
# limpiar esta cadena
lista_row=cadena_sucia.split(',')
for i,j in enumerate(lista_row):
    print(i,j)
    lista_row[i]=j.strip().upper()

cadena_clean=",".join(lista_row)
print(cadena_clean)
