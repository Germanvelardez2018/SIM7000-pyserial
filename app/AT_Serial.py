""""
Serial Interface to work with AT commads
"""





from AT_CMD import AT_CMD




class AT_Serial(AT_CMD):

    INTERFACE = None    # hardware interface





    def _send_cmd_raw(self,buffer_tx,response="OK",timeout=1):
        pass


    """
    Send a command and wait a response. If it checks to response return True
    
    """

    def _send_cmd(self,cmd,response = "OK",timeout = 1):
        pass




    def _send_list_cmd(self,list_cmd,list_response,timeout = 1):
        pass


    
    def get_buffer_response(cmd,response="OK",timeout=1):
      pass


    def _init_interface(self):
        pass


    def _deinit_interface(self):
        pass


