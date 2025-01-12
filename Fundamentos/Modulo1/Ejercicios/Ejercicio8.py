lista_alumno_1=[]
lista_alumno_1=["gianz","7775646","python","basico",0]
# el primer elemneto incia con 0
print(lista_alumno_1[0])
#?
print(type(lista_alumno_1[0]))
## luego de una evaluacion
# cambiamos la nota a 12

# lista_alumno_1[4]=12
lista_alumno_1[-1]=12

print(lista_alumno_1)
lista_flag=[]
### 
if lista_alumno_1[-1]>11:
    #lista_flag=[True]
    # o puedes usar esto
    lista_alumno_1.append(True)
else:
    lista_flag=[False]

lista_new_alumno=lista_alumno_1+lista_flag
print(lista_new_alumno)

# nota 
## ultima posicion de una lista
### la cantidad de elementos -1
## como obtengo la cantidad delementos con len
ultima_posicion=len(lista_alumno_1)-1 # que pasas si len =0 => -1
### agregar apellido
lista_alumno_1.reverse()
print(lista_alumno_1)
lista_alumno_1.append("Gutierrez")
lista_alumno_1.reverse()
print(lista_alumno_1)

if "gian" in lista_new_alumno:
    print("el alumno existe")
else:
    print("el alumno no existe")

lista_alumno_2=["carlos","7775236","python","basico",0]

lista_alumnos=[lista_alumno_1,lista_alumno_2]

print(lista_alumnos)


