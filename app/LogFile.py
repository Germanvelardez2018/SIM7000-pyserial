import os
from datetime import date, datetime

HEADER_LOG = """
--------------------------------
log file : {}
Date:{}
---------------------------------
"""






class LogFile:
    File= None
    OBJNAME ="LOGFILE"
    def __init__(self,name,header=HEADER_LOG):
        self.name = name
        self.header = header
        self._init_file()
        self.count = 0


    def _init_file(self):
        #Create the file, if already exist, just open
        
        if os.path.exists(self.name) != True:
            #create the file
            self.File =open(self.name,"w")
            now = datetime.now()
            self.File.write((self.header.format(self.name,now)))



    def write_file(self,text):
        try:
            with open(self.name,mode="a",encoding="utf-8") as file:
                file.write(text)
        except Exception:
            print("[{}]WriteError".format(self.OBJNAME))


    def read_all(self):
        try:
            with open(self.name,encoding="utf-8") as f:
                print("[{}]Read all: ".format(self.OBJNAME))
                lines=f.readlines()
                for line in lines:
                    print(str(line))
        except IOError:
            print("[{}]Error File ".format(self.OBJNAME))
        except Exception:
            print("[{}]Error".format(self.OBJNAME))



    def clear_all(self):
        print("[{}]clear the file ".format(self.OBJNAME))
        try:
            os.remove(self.name)
            self._init_file()
        except IOError:
            print("[{}]Error to clear the file".format(self.OBJNAME))
        #create a new one
        #create the file

        self.File =open(self.name,"w")
        now = datetime.now()
        self.File.write((self.header.format(self.name,now)))
        



        




if __name__ == "__main__":
    print("create my log file")
    file = LogFile("mylogfile")
    file.read_all()
    file.write_file("numeros aleatorio\n")

    file.write_file("numeros aleatorio\n")

    file.write_file("numeros aleatorio\n")
    file.write_file("composicion")
    file.read_all()