import paho.mqtt.client as mqtt
import time







TOPIC = "X1111"
BROKER= "test.mosquitto.org"
BROKER2="simointi.cloud.shiftr.io"
PORT = 1883
ID = "simointi"
PASS ="fdZY5b69OhOVsAns" 

_API_NAME_ = "mqtt client"

def on_connect(client,userdata,flags,rc):
    if rc == 0:

        print("[{}]connected to the broker".format(_API_NAME_))
        print("[{}] subcribe to the topic {}".format(_API_NAME_,TOPIC))
        client.subscribe("X1111")
    else:
        print("[{}]Error to connect".format(_API_NAME_))

def on_disconnected(client,userdata,rc):

    if rc !=0:
        print("[{}]disconnected to the broker".format(_API_NAME_))

def on_message(client,userdata,msg):
    print("[{}]you have a new message. {}".format(_API_NAME_,str(msg.payload)))



print("init sub")

client = mqtt.Client(client_id= "simo", clean_session=False)


print("conencted: {} port: {}".format(BROKER2,PORT))
client.on_connect = on_connect
client.on_message = on_message
#client.on_disconnect = on_disconnected


client.username_pw_set(ID,PASS)
client.connect(host=BROKER2,port=PORT,keepalive=60)
client.loop_forever()