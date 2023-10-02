def nota_teoria(nota1,nota2):
    t1=a_cero(nota1)
    t2=a_cero(nota2)
    res = (t1+t2)/ 2 
    if res< 4:
        res = 0
    return res

def a_cero(nota):
    res=nota
    if nota == None:
        res = 0
    return res


def nota_cuatrimestre(t,p):
    t1 = a_cero(t[0])
    t2 = a_cero(t[1])
    p = a_cero(p)
    if nota_teoria(t1,t2)>=4:
        res= 0.1*t1 + 0.1*t2 + 0.8*p
    else:
        res = 0
    return res
    

def nota_continua(nt,np)
    t1= a_cero(nt[0])
    t2= a_cero(nt[1])
    t3= a_cero(nt[2])
    t4= a_cero(nt[3])
    p1= a_cero(np[0])
    p2= a_cero(np[1])
    nota_c1 = nota_cuatrimestre((nt[0], nt[1],)np[0])
