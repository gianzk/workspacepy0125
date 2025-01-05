# primero con if
renta=float(input("ingrese su renta:"))
tasa=0.05

if renta<=10000:
    tasa=0.05
elif renta>10000 and renta<=15000:
    tasa=0.15
elif renta>15000 and renta<=20000:
    tasa=0.20
elif renta>20000 and renta<=40000:
    tasa=0.25
else:
    tasa=0.3


impuesto=renta*tasa
print("if")
print("el impuesto a pagar el año es ",impuesto)

