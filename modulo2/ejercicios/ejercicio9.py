x=0

def sumaTres(v):
    v=v+3
    print('dentro de sumarTres',v)
    #return v
    #x+=3
sumaTres(x)
print('print fuera',x)


lista=[1,2,3,4,5,4,6]

def cambiarInitList(listaNew:list):
    listaNew[0]=10
    print(listaNew)
cambiarInitList(lista)
print('esta lista es de afuera',lista)