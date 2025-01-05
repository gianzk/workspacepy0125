# determine si la persona puede sacar un credito
risk=0.5
edad=int(input("ingrese su edad: "))
riskClient=float(input("ingrese el riesgo"))
salario=float(input("ingrese el salario"))
if edad>=18:
    print("tiene mayor a 18")
    if riskClient<=risk:
        if salario>=1200:
            print("cuenta bancaria okay")
        else:
            print("salario menor al minimo")
    else:
        print("riesgo mayor ")
else:
    print("no puede sacar su cuenta bancaria porque es mayor a 18")
