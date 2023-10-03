from calificaciones import *

if __name__=="__main__":
    print("Prueba nota teoria")
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))
    print(nota_cuatrimestre((10,6), 5))
    print(nota_continua((6,7,3,8) ,(7,5)))