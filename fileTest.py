def addFile(string):
    f=open("datei.txt",'w')
    f.write(string)
def sort():
    list=[]
    with open('datei.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            words=line.split(' ')
            for word in words:
                list.append(word)
    print(list)
    list.sort()
    print(list)
    with open('datei_sorted.txt','w') as f:
        string=''
        for word in list:
            string+=word+'\n'
        f.write(string)

addFile("eine unsortierte Liste ist nicht gut")
sort()