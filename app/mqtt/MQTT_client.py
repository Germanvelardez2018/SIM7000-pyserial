
from MQTT_object import MQTT_object   #abstract class




class MQTT_client (MQTT_object):

    def __init__(self,server,port=8083,topic="none"):
        super._server_ = server
        super._port_ = port
        super._topic = topic
        


    def set_server(self, server):
        #validation statement
        if type(server) == str:
            return super().set_server(server)
    
    def set_topic(self, topic):
        if type(topic) == str:
            return super().set_topic(topic)


    def get_server(self):
        return super().get_server()

    def get_topic(self):
        return super().get_topic()