# Hacer un programa que tenga un catalogo de una tienda 
# ROPA
# codigo desordenado
class ProductoRopa:
    codigo_producto=None
    nombre_producto=None
    marca=None
    precio=None
    stock=None
    def __init__(self,codigo_producto,nombre_producto,marca,precio,stock):
        self.codigo_producto=codigo_producto
        self.nombre_producto=nombre_producto
        self.marca=marca
        self.precio=precio
        self.stock=stock
        """  self.precios:dict={
            'x':120,
            's':145
        } """
    def setDescuento(self,desc:int):
        self.descuento=100-desc
    def setSizes(self,listaTallas:list):
        self.sizes=listaTallas
    def priceFinal(self):
        if hasattr(self,'descuento'):
            self.priceFinal=self.precio*self.descuento/100
        self.priceFinal=self.precio
    def __str__(self):
        return f"Producto:{self.codigo_producto},{self.nombre_producto},{self.marca},{self.precio},{self.stock}"

pr1=ProductoRopa('pr_2','polos','adidas',50,10)
pr2=ProductoRopa('pr_1','casaca','columbia',120,15)
""" getKeys=pr1.precios.keys()
tall=input("ingrese la talla que deseas tener el precio")
if tall in getKeys:
    pr1.precios[tall]
else:
    print("esta talla no existe") """
""" pr1.setDescuento(20)
pr1.setSizes(['x','xs','s','m','l'])

print(pr1)
print(pr2) """



class Categoria:
    name=None
    codigo_categoria=None
    productos=None
    def __init__(self,name,codigo_categoria):
        self.name=name
        self.codigo_categoria=codigo_categoria
        self.productos=[pr1,pr2]
        pass
    def mostrarProductos(self):
        for i in self.productos:
            print(i)
    def agregarProducto(self,codigo_producto,nombre_producto,marca,precio,stock):
        prx=ProductoRopa(codigo_producto,nombre_producto,marca,precio,stock)
        self.productos.append(prx)
    def __str__(self):
        return f"esta es la categoria {self.name},{self.codigo_categoria}"
    
c1=Categoria('ROPA','RP-1')
""" print(c1)
c1.mostrarProductos()
c1.agregarProducto('prxas','pantalon','pioner',150,20)
c1.mostrarProductos() """

class TiendaRopaDatux:
    sede=None
    horario_apertura=None
    horario_clausura=None
    def __init__(self,sede,horario_inicial,horario_final):
        self.sede=sede
        self.horario_apertura=horario_inicial
        self.horario_clausura=horario_final
        self.categoria=[]
        self.categoriaName=[]
    def agregarCategoriaName(self,categoria:Categoria):
        self.categoriaName.append(categoria.name)
    def agregarCategoria(self,categoria:Categoria):
        self.categoria.append(categoria)
    def verCategoria(self):
        self.categoria[0].mostrarProductos()


Tienda=TiendaRopaDatux('Lima',8,23)
Tienda.agregarCategoria(c1)
Tienda.verCategoria()