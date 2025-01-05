tasa_km=1.5
tarifa_app=0.05

destino_inicio=int(input("ingrese su destino en coordenadas"))
destino_final=int(input("ingrese su destino en coordenadas"))

km_total= destino_final-destino_inicio

resutlado_total=(tasa_km*km_total)*(1+tarifa_app)
print("La tarifa es",resutlado_total)
acepta=input("ingrese s/n,para aceptar o rechazar")

if "s".upper()==acepta:
    print("el vehiculo esta en camino")
else:
    print("desea buscar otro vehiculo")



