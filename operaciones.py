def mcd(x,y):
    if x<y:
        x,y=y,x
    else:
        residuo = y 
        while residuo!=0:
            residuo = x%y
            x,y=y,residuo
    return x

def fracciones(x,y):
    num=int(x/mcd(x,y))
    den=int(y/mcd(x,y))
    if den == 1:
        print(num)
    elif num ==0:
        print(0)
    elif den == 0:
        print('Error division por cero')
    else: 
        print(num,'/',den)
    
    
def suma(n1,d1,n2,d2):
    num = (n1*d2)+(d1*n2)
    den = d1*d2
    if d1==0 or d2==0:
        print('Error división por cero')
    else:
        return fracciones(num,den)

def resta(n1,d1,n2,d2):
    num = (n1*d2)-(d1*n2)
    den = d1*d2
    if d1==0 or d2==0:
        print('Error división por cero')
    else:
        return fracciones(num,den)   

def multiplicacion(n1,d1,n2,d2):
    num = n1*n2
    den = d1*d2
    if d1==0 or d2==0:
        print('Error división por cero')
    else:
        return fracciones(num,den)

def division(n1,d1,n2,d2):
    num = n1*d2
    den = d1*n2
    if d1==0 or d2==0:
        print('Error división por cero')
    else:
        return fracciones(num,den)
        