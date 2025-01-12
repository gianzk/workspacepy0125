# mini sistema logistico con funciones
Almacen={
    "ubicaciones":["A","B","C","D"],
    "products":{
        "product1":{
            "ubicacion":"A",
            "precio-lista":3.5,
            "costo/almancen":0.1
        },
        "product2":{
            "ubicacion":"C",
            "precio-lista":1.5,
            "costo/almancen":0.05
        },
        "product3":{
            "ubicacion":"B",
            "precio-lista":15,
            "costo/almancen":0.4
        }
    }
}

def mostrarOpciones():
    print("BIENVENIDO AL DATUX LOGISTIC")
    print(
        """
        1. Agregar producto
        2. contar cuantos productos tiene por ubiacion
        3. dar costo por almacenaje
        4. salir
    """
    )
def agregarProducto():
    print("agregando producto ......")
    flagProduct=True
    productList=[*Almacen["products"].keys()]
    productName=None
    ubicacionName=None
    while flagProduct:
            productName=input("Ingrese el nombre del product(todo junto y en miniscula):")
            print(productList)
            if productName.lower() not in productList:
                    print("el producto no se encuentra registrado")
                    flagProduct=False
            else:
                print("el producto ya se encuentra registrado")
    flagAlmancen=True
    while flagAlmancen:
            ubicacionName=input("Ingrese la ubicacion del producto")
            if ubicacionName.upper() in Almacen["ubicaciones"]:
                print("ubicacion existe")
                flagAlmancen=False
            else: 
                print("la ubicacion no existe")
    precioListaR=float(input("ingrese el precio del producto"))
    costoAlR=float(input("ingrese el cost del almacen/dia"))
    Almacen["products"][productName.lower()]={
            "ubicacion":ubicacionName.upper(),
            "precio-lista":precioListaR,
            "costo/almancen":costoAlR
    }
    print(Almacen)
def agregarUbicacion():
    product_ubicacion={}
    list_product=Almacen["products"]
    for clave,valor in list_product.items():
        ubi=valor["ubicacion"]
        if ubi in product_ubicacion.keys():
            product_ubicacion[ubi]+=1
        else:
            product_ubicacion[ubi]=1
    print(product_ubicacion)

while True:
    mostrarOpciones()
    opcion=int(input("ingrese opcion a elegir: "))
    match opcion:
        case 1:
            agregarProducto()
            continue
        case 2:
            agregarUbicacion()
        case 3:
            print("ingrese el producto a calcular ")
            ## el producto a calcular
            dias=int(input("cuantos dias necesita calcular"))
            print(dias*Almacen["products"]["product1"]["costo/almancen"])
            continue
        case 4:
            print("gracias por usar datux logist, hasta luego")
            break
        case defaul:
             print("ingrese una opcion valida !")