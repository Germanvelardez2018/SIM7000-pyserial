


"""
 Author: German Velardez
 email: germanvelardez16@gmail.com
 
 description: Api to comunicate with SIM7000G


"""

import time    


from SerialCMD import SerialInterface, init_port


"""
Interface to work with SIM7000G
"""


def main():
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
        S_Interface.send_message(3856870066,"hola mundo")
        time.sleep(1)
      
if __name__ == "__main__":
    print("start the code")
    main()




