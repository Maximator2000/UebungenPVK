import time
def addFile(string):
    f=open("datei.txt",'w')
    f.write(string)
def sort(name):
    list=[]
    with open(name+'.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            words=line.split(' ')
            for word in words:
                list.append(word)
    print(list)
    list.sort()
    print(list)
    with open(name+'_sorted.txt','w') as f:
        string=''
        for word in list:
            string+=word+'\n'
        f.write(string)

#addFile("eine unsortierte Liste ist nicht gut")

def sortAndTime(name):
    start=time.time()
    sort('shakespeare_sonnets')
    end=time.time()
    print(end-start)
sortAndTime('shakespeare_sonnets')