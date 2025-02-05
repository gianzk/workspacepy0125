import sqlite3

class BaseDatos:

    def __init__(self,name):
        self.name=name
    def conect(self):
        #if not hasattr(self,'conection'):
        self.conection=sqlite3.connect(self.name)
    def getConection(self):
        return self.conect
    def execute(self,query:str):
        cursor=self.conection.cursor()
        cursor.execute(query)
        self.conection.commit()
    def fetchAll(self,table):
        query=f"SELECT * FROM {table}"
        cursor=self.conection.cursor()
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)

    def close(self):
        self.conection.close()

b1=BaseDatos('/workspaces/workspacepy0125/Fundamentos/Modulo4/base2.db')
b1.conect()
#sentencia = """
#INSERT INTO ventas (id,fecha, producto, cantidad, precio_unitario)
#VALUES (12,'2024-07-03', 'producto2', 5, 1.50);
#"""
#b1.execute(sentencia)
b1.fetchAll('ventas')
