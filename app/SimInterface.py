
"""
 Author: German Velardez
 email: germanvelardez16@gmail.com
 
 description: Api to comunicate with SIM7000G


"""

from posix import POSIX_FADV_NOREUSE
from LogFile import LogFile
from Sim7000G import *

from os import write
import time
import sys
import glob
import time    
import serial
from serial.serialutil import SerialException, SerialTimeoutException, Timeout
from datetime import date, datetime




BAUDRATE_LIST = [9600,19200,38400,57600,115200] #Valid Baudrate

MIN_SIGNAL_LEVEL = 15.0




class SimInterface:
   
    END_CMD="\r\n" # It is necessary that the sim7000 can understand the command
    LOG_FILE_PATH = "log_file.txt" # Path to the log file
    LOG_FILE = None

    def __init__(self,name_device="SIM DEVICE",baudrate=115200,debug_out=True):
        
        self.debug_out = debug_out
        self.name_device = name_device
        self.port = self._init_port()
        print("port init {}".format(self.port))
        self.set_baudrate(baudrate)
        self.LOG_FILE = LogFile(self.LOG_FILE_PATH)
        
    def debug_print(self,message,output= True):
        if self.debug_out == True:
            now = datetime.now()
            if output == True:
                flow = "=>"
                space = ""
            else:
                flow = "<="
                space= "     "
            out = "[{}]{} {}:{}:{} {} {}".format(self.name_device,space,now.hour,now.minute,now.second,flow,message)
            print(out)
            self.LOG_FILE.write_file(out+  "\n")
    
    
    def _clear_log_file(self):
        self.LOG_FILE.clear_all()
       
        



    def _init_port(self):
        
        print("Start Serial interface")
        ports = self._read_ports()
        print("Select number of ports availables")
        count = 1
        print("0)  Exit")
        for port in ports:
            print (str(count)+") " + port)
            count +=1
        print("Select the port: " ,end="")
        s = True
        while s:
            try:
                port_selected =int(input()) 
                if (not(port_selected >0 and port_selected < count)):
                    if port_selected == 0 :
                        s=False
                    else:
                        raise Exception
                else:
                    s = False   # out to the loop while
            except(Exception):
                print("Error:invalid value. Try again. ")
        return ports[port_selected-1]  


        

    
    def _read_ports(self):
        """
        Return serial ports
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        list = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                list.append(port)
            except (OSError, serial.SerialException):
                pass
        return list



    def set_baudrate(self,baudrate):
        
        if (type(baudrate) is int):
            if baudrate <= BAUDRATE_LIST[0]:
                self.baudrate = BAUDRATE_LIST[0]
            else:
                for baud in BAUDRATE_LIST:
                    if baudrate >= baud :
                        self.baudrate = baud
        print("the baudrate is {}".format(self.baudrate))


    def _send_cmd__set(self,cmd,timeout=1):
        
        cmd = cmd + self.END_CMD
        buf_rx = ""
        try:
            with serial.Serial(self.port,self.baudrate,timeout= timeout) as s:
             
                out = bytes((cmd),"utf-8")
                w= s.write(out)
                self.debug_print(str(out).replace("b",""))
                lines=s.readlines()
                for line in lines:
                    buf_rx = buf_rx + str(line)
                    line_formated = (str(line)).replace("b","" )
                    print(line)
                    self.debug_print(line_formated,False)
                         
        except SerialException:
            print("ocurrio un error ")
        except SerialTimeoutException:
            print(f"el comando no obtuvo respuesta")
        
        return buf_rx
       

    #Serial functions

    def _send_cmd(self,cmd,answer,timeout=1):
        """
        Send a commands and wit a response
        """
        cmd = cmd + self.END_CMD
        return self._send_cmd_raw(cmd,answer=answer,timeout=timeout) 
        


    def _send_cmd_raw(self,cmd,answer,timeout,encoding = True):
      
        res = False
        try:
            with serial.Serial(self.port,self.baudrate,timeout= timeout) as s:
                if encoding == True:
                    out = bytes((cmd),"utf-8")
                else:
                    out = bytes(cmd)
                    
                
                w= s.write(out)
                self.debug_print(str(out).replace("b",""))
                lines=s.readlines()
                for line in lines:
                    line_formated = (str(line)).replace("b","" )
                    print(line)
                    self.debug_print(line_formated,False)
                    if (str(line).count("OK")) > 0:
                        res = True
                        print("Se recibio respuesta esperada: "+answer)         
        except SerialException:
            print("ocurrio un error ")
        except SerialTimeoutException:
            print(f"el comando no obtuvo respuesta")

        return res
        
    #TOP LEVEL FUNCTIONS

    def send_message(self,phone,message):
        #Activate the message function
        #Activate the msm function
        self._send_cmd( CMD_SMS_SET_FUNCTION,"OK")
        time.sleep(1)
        #Set the number to send the message
        cmd =CMD_SEND_MSM.format(str(phone)) 
        
        self._send_cmd(cmd,"> ",5)

    

        self._send_cmd(message ,"OK",1)
        # BUFFER end      [26]
        buff_hex = [26,]
        self._send_cmd_raw(buff_hex,"OK",20,encoding=False)
       

    def get_signal(self):
        """
        Return signal level (float).
        """
        values = self._send_cmd__set(cmd=CMD_GET_SIGNAL_LEVEN,timeout=1)
        signal = 0
     
        pos = values.find(":")
        
        if pos >0:
            number = values[pos+2:pos+7].replace(",",".")
          
            try:
                n = float(number)
                signal = n
              
            except Exception:
                print("error signal value")
            
        return signal






if __name__ == "__main__":
    app = SimInterface("sim7000g")
    time.sleep(2)

    app._clear_log_file()

    res = app._send_cmd("AT","OK",1)
    while res == False:
        time.sleep(1)
        print("try again")
        res = app._send_cmd("AT","OK",1) 


    print("try to send a text message to a cellphone")
    signal_value =app.get_signal()
    if signal_value <MIN_SIGNAL_LEVEL:
        print("low signal") 
    #app.send_message(3856870066,"mensaje de pruebas del sistema")
    #app.send_message(3856870066,"Error en GPS")
    #app.send_message(3856870066,"simo INTI v1")

