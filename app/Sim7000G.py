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




""""
 Author: German Velardez
 email: germanvelardez16@gmail.com
 
 description: Commands for SIM7000G



"""
#APNS
APN_PERSONAL = "datos.personal.com"
APN_USR_PASS_PERSONAL = "datos"



#actions
ACT_ASK         = "=?"
ACT_SET         = "="
ACT_GET         = "?"
#Definitions

CMD_SIM_REGS = "AT+CREG" +ACT_GET   #[ (0,0) (0,1) , (0,2) , (0,3)] = > [not registerd, registered, searching operator,register denid]

CMD_DEFAULT_CONFIG = "ATZ"     #Return to default configuration 
CMD_AT             = "AT"      #Return OK if the devices is alive
CMD_INFO_DEVICE    = "ATI"     #Return information about the device
CMD_BAUDRATE   ="AT+IPR"        #R

CMD_SMS_FUNCTION  ="AT+CMGF"
CMD_SMS_SET_FUNCTION  = CMD_SMS_FUNCTION + "=1"  #Format TEXT
CMD_SMS_CLEAR_FUNCTION= CMD_SMS_FUNCTION + "=0"  # Format PDU

CMD_SEND_MSM     ='AT+CMGS= "{}"'
CMD_ASK_BAUDRATE  =  CMD_BAUDRATE +  ACT_ASK



CMD_READ_IMEI   = "AT+CGSN"

CMD_IS_CHIP_READY = "AT+CPIN?"

CMD_GET_IP        = "AT+CIFSR"    # GET IP



CMD_ECHO_OFF =  "ATE0"   # OFF ECHO,
CMD_ECHO_ON  =  "ATE1"    # ON ECHO


CMD_GET_SIGNAL_LEVEN = "AT+CSQ"


#DATA SERVICES

CMD_DATA_SERVICE = " AT+CGATT"    #1 CONNECTED , 0 DISCONECTES. FUNCTION ALLOWS SET AND GET


CMD_SET_APN = "AT+CSTT=\"{}\",\"{}\""




#HTTP(S) THINGS
"""
Error Codes
    600 Not HTTP PDU
    601 Network Error
    602 No memory
    603 DNS Error
    604 Stack Busy
"""
CMD_HTTP_INIT = "AT+HTTPINIT"
CMD_HTTP_END = "AT+HTTPTERM"
