import sys 
print(sys.argv)

def fxActivar(*args):
    for i,j in enumerate(args):
        print(i,j)

fxActivar(*sys.argv)
fxActivar(5,"Hola",[1,2,3,4,5],{'dia':'sabado'})


def fxActivarv2(**kwargs):
    for key in kwargs:
        print(key)
        print("value",kwargs[key])
fxActivarv2(name="gian",cursos=["python"],date="19-01-2025")