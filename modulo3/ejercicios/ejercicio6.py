class Celular:
    def __init__(self,marca,modelo,os):
        self.marca=marca
        self.modelo=modelo
        self.os=os # sistema operativo
        self.status=False # si esta prendido o apagado
    def config(self,email):
        self.email=email
        pass
    def onMobile(self):
        self.status=True
        pass
    def offMobile(self):
        self.status=False
    def getStatus(self):
        estado=""
        if self.status:
            estado="Prendido"
        else:
            estado="Apagado"
        return f"el equipo {self.modelo} esta {estado}"


class Iphone(Celular):
    clavePIN=None
    def __init__(self, modelo):
        super().__init__('apple', modelo, 'iOs')
    pass
    def onMobile(self):
        email=input("ingrese su email")
        self.config(email)
        super().onMobile()
        print(self.status)
    def config(self,email):
        super().config(email)
        self.clavePIN=input("ingrese su clave PIN")


class SamsungGalaxy(Celular):
    clavePIN=None
    def __init__(self, modelo):
        super().__init__('samsung', modelo, 'Android')
    def onMobile(self):
        email=input("ingrese su email")
        self.config(email)
        super().onMobile()
        print(self.status)
    def config(self,email):
        super().config(email)
        self.clavePIN=input("ingrese su clave PIN")
    def offMobile(self):
        clavePINTMP=input("ingresa tu clave PIN")
        if clavePINTMP == self.clavePIN:
            super().offMobile()
        else:
            print("no puede apagar el equipo porque no es la clave PIN")

iphone12=Iphone('Iphone12')
samsungS20= SamsungGalaxy('Samsung S20')

print(iphone12.getStatus())
print(samsungS20.getStatus())

iphone12.onMobile()
#samsungS20.onMobile()

print(iphone12.getStatus())
#print(samsungS20.getStatus())

print(iphone12.clavePIN)