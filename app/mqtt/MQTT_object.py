"""
This is a mqtt client ready to use

"""
from abc import ABC, abstractclassmethod
import paho.mqtt.client as mqtt


class MQTT_object(ABC):

    _server  = None     # link to broker mqtt
    _port    = None     # port, if you need it
    _topic   = None     # topic channel when you work
    _mqtt    = None


    
    def set_server(self,server):

        if type(server) == str:
            self.set_server = server
        


    
    def set_topic(self,topic):
        if type(topic) == str:
            self._topic = topic

    
    def set_port(self,port):
        if type(port) == int:
            self._port = port

    
    def get_server(self):
        return self._server
    
    
    def get_topic(self):
        return self._topic
    
    def get_port(self):
        return self._port
        




    

