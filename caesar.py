class Encoder():
    def __init__(self,shift):
        self.shift=shift
    def encode(self,message):
        ret=''
        for i in range(len(message)):
            m=ord(message[i])
            if m<=90 and m>=65:
                temp=chr((((m-65)+self.shift)%26)+65)
                ret+=temp
            else:
                ret+=message[i]
        return ret
    def decode(self,message):
        ret=''
        for i in range(len(message)):
            m=ord(message[i])
            if m<=90 and m>=65:
                temp=chr((((m-65)-self.shift)%26)+65)
                ret+=temp
            else:
                ret+=message[i]
        return ret

    def encrypt_file(self,file_path,name):
        with open(file_path,'r') as f_in:
            lines=f_in.readlines()
            for line in lines:
                encrypt=self.encode(line)
                with open(name+'.txt','a') as f_out:
                    f_out.write(encrypt+'\n')

def addFile(string):
    f=open("datei.txt",'w')
    f.write(string)






print(ord('A'))
print(chr(66))

e=Encoder(2)
print(e.decode(e.encode("ABcdZ")))

addFile("Hallo wIe geht es\n"
        "dir heUte")
e.encrypt_file('datei.txt','geheim.txt')