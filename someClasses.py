class Geburtstag():
    def __init__(self,tag,monat,jahr):
        self.tag=tag
        self.monat=monat
        self.jahr=jahr
    def print(self):
        print(str(self.tag)+"."+str(self.monat)+"."+str(self.jahr))
    def nice_print(self):
        dict={
            1:"Januar",
            2:"Februar",
            3:"März",
            4:"April",
            5:"Mai",
            6:"Juni",
            7:"Juli",
            8:"August",
            9:"September",
            10:"Oktober",
            11:"November",
            12:"Dezember"
        }
        print(str(self.tag)+"."+dict.get(self.monat)+" "+str(self.jahr))
    def nice_print2(self):
        dict={
            1:"Januar",
            2:"Februar",
            3:"März",
            4:"April",
            5:"Mai",
            6:"Juni",
            7:"Juli",
            8:"August",
            9:"September",
            10:"Oktober",
            11:"November",
            12:"Dezember"
        }
        return str(self.tag)+"."+dict.get(self.monat)+" "+str(self.jahr)
class Polynom():
    def __init__(self,liste):
        self.koeffizienten=tuple(liste)
    def add(self,koef):
        l1=self.koeffizienten
        l2=koef
        list=[]
        for index in range(len(max(l2,l1))):
            if index>len(l2):
                list.append(l1[index])
            elif index>len(l1):
                list.append(l2[index])
            else:
                list.append(l2[index]+l1[index])
        return tuple(list)
    def sub(self,koef):
        l1=self.koeffizienten
        l2=koef
        list=[]
        for index in range(max(len(l2),len(l1))):
            if index>=len(l2):
                list.append(l1[index])
            elif index>=len(l1):
                list.append(-l2[index])
            else:
                list.append(l1[index]-l2[index])
        return tuple(list)
    def multi(self,f):
        list=[]
        for index in range(len(self.koeffizienten)):
            list.append(self.koeffizienten[index]*f)
        return tuple(list)
    def grad(self):
        return len(self.koeffizienten)-1
    def __str__(self):
        res=""
        l=len(self.koeffizienten)
        for i in range(l):
            res+=str(self.koeffizienten[i])+"x^"+str(i)
            if(i<l-1):
                res+="+"
        return res
    def __ente__(self):
        return Ente(quaks=self.grad())

def ente(arg):
    return arg.__ente__()


class Ente :
    """ Eine einfache Entenklasse """
    def __init__(self,quaks =1):
        """ Erstellt eine Ente .
        Die Anzahl der quaks kann uebergeben werden . """
        self.quaks = quaks

    def __str__ (self):
        return self.quaks*' Quack !'
p1=Polynom([1,2,3,5])
e=ente(p1)
print(e)