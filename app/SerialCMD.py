
"""
 Author: German Velardez
 email: germanvelardez16@gmail.com
 
 description: Api to comunicate with SIM7000G


"""

from Sim7000G import *

from os import write
import sys
import glob
import time    
import serial
from serial.serialutil import SerialException, SerialTimeoutException







class SerialInterface:

    def __init__(self,port,baudrate=115200,cmd_end="\r\n"):
        self.port = port
        self.baudrate = baudrate
        self.cmd_end = cmd_end

    def send_cmd_hex(self,hex_buff,expected_response,timeout=1, info_debug = False):
        """
        Send a cmd and wait a response
        """
        if info_debug == True:
            print("puerto seleccionado : ", end="")
            print(self.port)
        res = False
    
        try:
            with serial.Serial(self.port,self.baudrate,timeout= timeout) as s:
                
                w= s.write(bytes(hex_buff))
                lines=s.readlines()
                for line in lines:
                    line_formated = (str(line)).replace("b","-> " )
                    print(line_formated )
                    if (str(line).count("OK")) > 0:
                        res = True
                        if info_debug == True:
                            print("Se recibio respuesta esperada: "+expected_response)             
        except SerialException:
            print("ocurrio un error ")
        except SerialTimeoutException:
            print(f"el comando no obtuvo respuesta")

        return res

    def send_cmd(self,cmd,expected_response, timeout=1, info_debug = False):
        """
        Send a cmd and wait a response
        """
        if info_debug == True:

            print("puerto seleccionado : ", end="")
            print(self.port)
        res = False
    
        try:
            with serial.Serial(self.port,self.baudrate,timeout= timeout) as s:
                
                w= s.write(bytes((cmd+self.cmd_end),"utf-8"))
                lines=s.readlines()
                for line in lines:
                    line_formated = (str(line)).replace("b","-> " )
                    print(line_formated )
                    if (str(line).count("OK")) > 0:
                        res = True
                        if info_debug == True:
                            print("Se recibio respuesta esperada: "+expected_response)         
        except SerialException:
            print("ocurrio un error ")
        except SerialTimeoutException:
            print(f"el comando no obtuvo respuesta")

        return True
    

    def send_message(self,number,message, info_debug= False):
        #Activate the msm function
        self.send_cmd( CMD_SMS_SET_FUNCTION,"OK",info_debug= info_debug)
        time.sleep(1)
        #Set the number to send the message
        cmd =CMD_SEND_MSM.format(str(number)) 
        self.timeout = 5
        self.send_cmd(cmd,"> ",4,info_debug= info_debug)

    

        self.send_cmd(message ,"OK",1,info_debug= info_debug)
        # BUFFER end      [26]
        buff_hex = [26,]
        self.send_cmd_hex(buff_hex,"OK",10,info_debug= info_debug)
       

        self.timeout = 1




def read_ports():
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
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result   





def init_port():
    print("Start Serial interface")
    ports = read_ports()
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

    return ports,port_selected        

        









        
   


if __name__ == "__main__":
   ports,port_selected = init_port()
   if port_selected == 0:
       print("end to the program")
       exit()
   else:

       # instance a SerialInterface
       print("inicio interface")

       S_Interface = SerialInterface((ports[port_selected-1]),115200)
       
       res = S_Interface.send_cmd("AT","OK")
       while  res == False:
            
            time.sleep(1)
            print("wait for the SIM7000G")
            res = S_Interface.send_cmd("AT","OK")

       print("SIM7000G ready")

     
       S_Interface.send_message(3856870066,"Posicionx =134 Posiciony = 222 ")
      
       time.sleep(1)
      
