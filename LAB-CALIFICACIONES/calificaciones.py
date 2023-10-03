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
    

def nota_cuatrimestre(nt,np):
   
    t1=a_cero(nt[0])
    t2=a_cero(nt[1])
    p=a_cero(np)
    if nota_teoria(t1,t2)>=4:
        res=0.1*t1+0.1*t2+0.8*p
    else:
        res=0
    return res

def nota_continua(nt,np):
    c1=nota_cuatrimestre(nt[:2],np[0])
    c2=nota_cuatrimestre(nt[2:],np[1])
    res= {c1+c2}/2
    if c1<4 or c2<4:
        res=min(4,res)
    return res