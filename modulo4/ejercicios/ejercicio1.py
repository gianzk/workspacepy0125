
import os
class Student:
    def __init__(self,name,id,level):
        self.name=name
        self.id=id
        self.level=level
    def setLevel(self):
        if self.level>0 and self.level<5:
            self.levelCurso='BASICO'
        elif self.level >5 and self.level <10:
            self.levelCurso="INTERMEDIO"
        else:
            self.levelCurso="AVANZADO"
    def GetLevel(self):
        self.setLevel()
        return self.levelCurso
    def toInsert(self)->str:
        return f"{self.id},{self.name},{self.GetLevel()}\n"
    def __str__(self):
        return "este es mi clase student"

def initRegister():
    pathFile="./modulo4/ejercicios/files/studentsv1.txt"
    if not os.path.isfile(pathFile):
        with open(pathFile,mode='a') as F:
            F.write("id,name,level")
    else :
        print(f"el archivo {pathFile} , ya existe valida la estructura")

def RegisterUser():
    pathFile="./modulo4/ejercicios/files/studentsv1.txt"
    name=input("ingrese su nombre: ")
    id=input("ingrese su id: ")
    level=int(input("ingrese su level: "))
    s1=Student(name,id,level)
    s1Insert=s1.toInsert()
    print(type(s1Insert))
    with open(pathFile,mode='a') as FileStudent:
        FileStudent.write(s1Insert)
        FileStudent.close()

def RegisterCustomer():
    pathFile="./modulo4/ejercicios/files/customer.txt"
    pass

def getData():
    pathFile="./modulo4/ejercicios/files/studentsv1.txt"
    with open(pathFile) as Fs:
        data=Fs.read()
        Fs.close()
    print(data)
#initRegister()
getData()
