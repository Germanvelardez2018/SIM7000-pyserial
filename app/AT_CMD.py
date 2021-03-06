""""
Base Class to work with commnands AT by serial port

"""

from abc import ABC, abstractclassmethod
import serial




class AT_CMD:

    POS_CMD = ""
    PRE_CMD = ""

    SERIAL = None

    




    @abstractclassmethod
    def _send_cmd_raw(self,buffer_tx,response="OK",timeout=1):
        pass


    """
    Send a command and wait a response. If it checks to response return True
    
    """

    @abstractclassmethod
    def _send_cmd(self,cmd,response = "OK",timeout = 1):
        pass




    @abstractclassmethod
    def _send_list_cmd(self,list_cmd,list_response,timeout = 1):
        pass


    
    @abstractclassmethod
    def get_buffer_response(cmd,response="OK",timeout=1):
      pass


    @abstractclassmethod
    def _init_interface(self):
        pass

    @abstractclassmethod
    def _deinit_interface(self):
        pass



    

