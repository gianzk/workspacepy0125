def Saludarv1():
    print("hola como estas")
def Saludarv2():
    print("hola como estas, soy gianmarco")
def Saludarv3(nombre="Sin Name"):
    print(f"hola como estas, soy {nombre}")
Saludarv1()
Saludarv2()
Saludarv3("antonio")
Saludarv3()


### otro ejemplo de parametro

def sumaN(n):
    suma=n*(n+1)/2
    return suma

suma100=sumaN(100)
suma200=sumaN(200)
print(suma100,suma200)

# calcula el impuesto
planilla=[
    {
        "dni":"24646464",
        "salario":1500
    },
    {
        "dni":"24621464",
        "salario":1100
    },
    {
        "dni":"1421464",
        "salario":2500
    },
    {
        "dni":"467979874",
        "salario":1800
    }
]

def fxPlanilla(salario):
    descuentobase=salario*0.9
    descuentoRenta=descuentobase*0.05
    neto=salario-descuentobase-descuentoRenta
    return [salario,descuentobase,descuentoRenta,neto]
def mostrarDatos(lista:list):
        print("datos totales")
        for i in lista:
            print(i)
for i in planilla:
    listPlanilla=fxPlanilla(i["salario"])
    mostrarDatos(listPlanilla)