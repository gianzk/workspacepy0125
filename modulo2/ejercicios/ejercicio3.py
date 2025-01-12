#otra opcion

while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
    4) otra opcion x""")

    opcion = int(input("ingrese la opcion a realizar: "))

    match opcion:
        case 1:
            print("Hola, espero que te lo estés pasando bien")
            continue
        case 2:
            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))
            continue
        case 3:
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        case default:
            print("comando desconocido")