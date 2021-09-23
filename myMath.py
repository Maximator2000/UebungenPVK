def istDurch2Teilbar(n):
    if n==0:
        return True
    elif n==-1:
        return False
    else:
        return istDurch2Teilbar(n-2)
def sort(listeMitZahlen):
    list=listeMitZahlen
    if len(list)>1:
        n=len(list)-1
        while n>0:
            for index in range(0,n):
                if list[index]>list[index+1]:
                    temp=list[index+1]
                    list[index+1]=list[index]
                    list[index]=temp
            n-=1
        return list
    else:
        return "Du musst eine Liste übergeben"
def sortString(listeMitZeichen):
    list=listeMitZeichen
    if len(list)>1:
        n=len(list)-1
        while n>0:
            for index in range(0,n):
                if list[index].lower()>list[index+1].lower():
                    temp=list[index+1]
                    list[index+1]=list[index]
                    list[index]=temp
            n-=1
        return list
    else:
        return "Du musst eine Liste übergeben"
def fak(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res

def expo(x):
    sum=0
    for k in range(100):
        sum+=(x**k)/fak(k)
    return sum
def ln(x):
    sum=0
    for k in range(1000):
        sum+=(((x-1)/(x+1))**(2*k+1))*(1/(2*k+1))
    return 2*sum
#e**x=5 ln(5)=x e**ln(a)=a  a**x=y=e**(ln(a)*x) ln(y)=ln(a)*x ln(y)/ln(a)=x      loga(y)=x
def log(basis,x):
    return ln(x)/ln(basis)
def power(x,y):
    return expo(y*ln(x))
def sin(x):
    return cos(x+3.141/2)
def cos(x):
    sum=0
    for k in range(20):
        sum+=((-1)**k)*((x**(2*k))/(fak(2*k)))
    return sum
def sqrt(x):
    if(x>0):
        a=x
        while not (a/x>x-0.0001):
            x=(x+a/x)/2
        return x
    elif(x==0):
        return 0

def letzteSeite(b,c,alpha):
    c1=cos(alpha)*b
    c2=c-c1
    h=sin(alpha)*b
    a=sqrt(h**2+c2**2)
    return a

def mitternachtsformel(a,b,c):
    radikant=(b**2)-(4*a*c)
    if radikant<0:
        return None
    elif radikant==0:
        return -b/2*a
    else:
        x1=(-b+sqrt(radikant))/(2*a)
        x2=(-b-sqrt(radikant))/(2*a)
        return x1,x2



