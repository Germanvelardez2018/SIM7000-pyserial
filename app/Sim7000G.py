""""
 Author: German Velardez
 email: germanvelardez16@gmail.com
 
 description: Commands for SIM7000G



"""







#Definitions

CMD_ASK         = "=?"
CMD_DEFAULT_CONFIG = "ATZ"     #Return to default configuration 
CMD_AT             = "AT"      #Return OK if the devices is alive
CMD_INFO_DEVICE    = "ATI"     #Return information about the device
CMD_BAUDRATE   ="AT+IPR"        #R

CMD_SMS_FUNCTION  ="AT+CMGF"
CMD_SMS_SET_FUNCTION  = CMD_SMS_FUNCTION + "=1"  #Format TEXT
CMD_SMS_CLEAR_FUNCTION= CMD_SMS_FUNCTION + "=0"  # Format PDU

CMD_SEND_MSM     ="AT+CMGS="

CMD_ASK_BAUDRATE  =  CMD_BAUDRATE +  CMD_ASK



CMD_READ_IMEI   = "AT+CGSN"