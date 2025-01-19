def sumar2(number):
    print(number+2)


numeroInit=float(input("ingrese un valor"))
try:
    numeroNuevo=10/numeroInit
    print("se ejecuto bien el codigo")
    pass
except:
    numeroNuevo=1
    print("sucedio un error")
    pass
else:
    print("el codigo se ejecuto correctamente")
    pass
finally:
    sumar2(numeroNuevo)