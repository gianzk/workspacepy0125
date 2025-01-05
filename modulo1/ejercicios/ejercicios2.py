# desarrolle un programa que determine si una persona cumple con caracteristicas para acceder a un crediot

# constantes para definir el credito 

sueldoMin=1500
edadMinima=22
edadMaxima=60
riskPorcentajeMin=0.2
riskPorcentajeMax=0.8
numeroActivos=1

# las variables del cliente
salary=float(input("Ingrese su sueldo"))
edad=int(input("Ingrese su edad"))
risk=float(input("Ingrese su risk"))
activo=int(input("Ingrese su numeroActivos"))

# proceso
resultado=((edad>=edadMinima)and (edadMaxima>=edad))and(salary>sueldoMin)and((risk<=riskPorcentajeMax)or (activo>=numeroActivos))
# resultado
print("el resultado de su evaluacion es :",resultado)

