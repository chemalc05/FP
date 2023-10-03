#def solicita_nota():
#   nombre= input("introduzca su nombre")
#  t1 = float(input("introduzca la nota del examen teorico 1(- si no se hapresentado)"))
# t2 = float(input("introduzca la nota del examen teorico 2(- si no se hapresentado)"))
#t3 = float(input("introduzca la nota del examen teorico 3(- si no se hapresentado)"))
#t4 = float(input("introduzca la nota del examen teorico 4(- si no se hapresentado)"))
#p1 = float(input("introduzca la nota del examen practico 1(- si no se hapresentado)"))
#p2 = float(input("introduzca la nota del examen practico 2(- si no se hapresentado)"))



#def mostrar_notas():
    #pass

from calificaciones import *



def solicita_nota():
    nombre = input("introduzca su nombre:")
    notas_teoria= lee_notas("teorico",4)
    notas_practica=lee_notas("practico",2)
    return (nombre,notas_teoria,notas_practica)

def lee_notas(tipo_examen,numero_examenes):
    res= []
    for indice in range(1,numero_examenes + 1):
        valor=float(input(f"introduzca la nota del examen{tipo_examen} {indice}(- si no se ha presentado)"))
        res.append(valor)
    return res

def check(valor):
    if valor=="-":
     res=None
    else:
     res=float(valor)
    return res


def mostrar_notas(entrada):
   
    nombre = entrada[0]
    ntc1=nota_teoria(entrada[1][0],entrada[1][1])
    p1=entrada[2][0]
    c1=nota_cuatrimestre(entrada[1][:2],p1)
    
    ntc2=nota_teoria(entrada[1][2],entrada[1][3])
    p2=entrada[2][1]
    c2=nota_cuatrimestre(entrada[1][2:],p2)
   
    nota_final=nota_continua(entrada[1],entrada[2])
   
   
   
   
print(f"hola¨,{nombre}")
print("tus notas del primer cuatrimestre son:")
print(f"teoria{ntc1},practica{p1},cuatrimestre{c1}")
print("tus notas del segundo cuatrimestre son:")
print(f"teoria{ntc2},practica{p2},cuatrimestre{c2}")
print(f"tu nota final de la asignatura es {nota_final}")    

if __name__=="__main__":
    notas = solicita_notas()
    mostrar_notas(notas)
    