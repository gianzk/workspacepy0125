
#forma generica de manejar errores
# el try va junto si o si con el except
try: 
    #lista=[12,213,12]
    tupla=(12,2)
    #tupla[1]=2
    print(0/0)
    #print(lista[12])
except Exception as mesageError:
    print(mesageError)
# else (son opcionales) # cuando el try pasa okay
# finally (son opcionales) #finally siempre se ejecuta