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



#SET FUNCTIONS :
# 0 MINUMUN FUNC, 1 FULL FUNC(DEFAULT), 4 DESABLE PHONE, 5 FACTORY TEST, 6 RESET,7 OFFLINE 
CMD_SET_FUNC = "AT+CFUN {}"



#APNS
#PERSONAL
APN_PERSONAL = "datos.personal.com"
APN_USR_PASS_PERSONAL = "datos"
#TUENTI
APN_TUENTI = "internet.movil"
APN_USER_PASS_TUENTI = "internet"

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



#CELPHONE OPERATOR
CMD_OPERATOR= "AT+COPS{}"
CMD_GET_OPERATOR = "AT+COPS?"

#DATA SERVICES

CMD_DATA_SERVICE = " AT+CGATT"    #1 CONNECTED , 0 DISCONECTES. FUNCTION ALLOWS SET AND GET


CMD_SET_APN = "AT+CSTT=\"{}\",\"{}\""


#mqtt thhings


CMD_OPEN_CONN = 'AT+CNACT=1,"{}"'
CMD_DISCONECT_MQTT= "AT+SMDISC"
CMD_CLOSE_MQTT_CONN =  "AT+CNACT=0"
CMD_GET_CONN  = "AT+CNACT?"

#PARAMS CONFIG MQTT

CMD_PARAM_MQTT ="AT+SMCONF"
CMD_MQTT_SET_URL = CMD_PARAM_MQTT+      '="URL","{}"'
CMD_MQTT_SET_KEEPTIME= CMD_PARAM_MQTT+  '="KEEPATIME",{}'
CMD_MQTT_SET_USERNAME = CMD_PARAM_MQTT+ '=USERNAME,"{}"'
CMD_MQTT_SET_PASSWORD = CMD_PARAM_MQTT+ '=PASSWORD,"{}"'
CMD_MQTT_SET_QOS =  CMD_PARAM_MQTT+ '=QOS,{}'   # VALID VALUES 1,2,3 (NUMBERS)
CMD_MQTT_SUBSCRIBE = 'AT+SMSUB?"{}",1,1'  # ADD TOPICS
CMD_MQTT_UNSUBSCRIBE = 'AT+SMUNSUB="{}'

CMD_MQTT_CHECKS_PARAMS = "AT+SMCONN"

CMD_MQTT_PUBLISH= 'AT+SMPUB="{}","{}",1,1' # PARAMS 1TOPIC, 2LENMESSAGE
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


#set mode
CMD_SET_MODE = "AT+CNMP=" # MODES : 2 AUTOMATIC, 13 GSM ONLU, 38 LTE ONLY, 51 GSM AND LTE

CMD_SET_MODE_NB     = "AT+CNMP=38"
CMD_SET_MODE_NB_2   = "AT+CMNB=2"

CMD_SET_MODE_GPRS   = "AT+CNMP=13"
CMD_SET_MODE_GRPS_2 = "AT+CMNB=3" # 1 CAT-M , 2 NB-IOT, 3 BOTH

CMD_MSG_ERROR      = "AT+CMEE"   # =1 errors messages more definition, 0 error messages simples




#GPS MODES


CMD_PWR_GPS = "AT+CFNSPWR" # =0 OFF ,=1 ON
CMD_GET_INFO_GPS = "AT+CGNSINF"
CMD_SET_PORT_GPS = "AT+CGNSPORT"   # 3 NMEA PORT, 4 NONE



""""
Secuencia de pasos para iniciar una coneccion http






"AT+CNMP=38"
"AT+CMNB=2"



attachtService
-----------------
AT+CGATT=1

AT+CSTT = MODE


AT+CIICR

AT+CIFSR
------------------

HTTP_INIT
---------------
"AT+SAPBR=3,1,"APN","CTNB"   # TO CHANGE CTNB for CMNET


AT+SAPBR=1,1

AT+SAPBR=2,1






-------------
"""


""""
Error	Description
CME ERROR: 0	Phone failure
CME ERROR: 1	No connection to phone
CME ERROR: 2	Phone adapter link reserved
CME ERROR: 3	Operation not allowed
CME ERROR: 4	Operation not supported
CME ERROR: 5	PH_SIM PIN required
CME ERROR: 6	PH_FSIM PIN required
CME ERROR: 7	PH_FSIM PUK required
CME ERROR: 10	SIM not inserted
CME ERROR: 11	SIM PIN required
CME ERROR: 12	SIM PUK required
CME ERROR: 13	SIM failure
CME ERROR: 14	SIM busy
CME ERROR: 15	SIM wrong
CME ERROR: 16	Incorrect password
CME ERROR: 17	SIM PIN2 required
CME ERROR: 18	SIM PUK2 required
CME ERROR: 20	Memory full
CME ERROR: 21	Invalid index
CME ERROR: 22	Not found
CME ERROR: 23	Memory failure
CME ERROR: 24	Text string too long
CME ERROR: 25	Invalid characters in text string
CME ERROR: 26	Dial string too long
CME ERROR: 27	Invalid characters in dial string
CME ERROR: 30	No network service
CME ERROR: 31	Network timeout
CME ERROR: 32	Network not allowed, emergency calls only
CME ERROR: 40	Network personalization PIN required
CME ERROR: 41	Network personalization PUK required
CME ERROR: 42	Network subset personalization PIN required
CME ERROR: 43	Network subset personalization PUK required
CME ERROR: 44	Service provider personalization PIN required
CME ERROR: 45	Service provider personalization PUK required
CME ERROR: 46	Corporate personalization PIN required
CME ERROR: 47	Corporate personalization PUK required
CME ERROR: 48	PH-SIM PUK required
CME ERROR: 100	Unknown error
CME ERROR: 103	Illegal MS
CME ERROR: 106	Illegal ME
CME ERROR: 107	GPRS services not allowed
CME ERROR: 111	PLMN not allowed
CME ERROR: 112	Location area not allowed
CME ERROR: 113	Roaming not allowed in this location area
CME ERROR: 126	Operation temporary not allowed
CME ERROR: 132	Service operation not supported
CME ERROR: 133	Requested service option not subscribed
CME ERROR: 134	Service option temporary out of order
CME ERROR: 148	Unspecified GPRS error
CME ERROR: 149	PDP authentication failure
CME ERROR: 150	Invalid mobile class
CME ERROR: 256	Operation temporarily not allowed
CME ERROR: 257	Call barred
CME ERROR: 258	Phone is busy
CME ERROR: 259	User abort
CME ERROR: 260	Invalid dial string
CME ERROR: 261	SS not executed
CME ERROR: 262	SIM Blocked
CME ERROR: 263	Invalid block
CME ERROR: 772	SIM powered down
"""