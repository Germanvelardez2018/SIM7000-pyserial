"""
This is a mqtt client ready to use

"""
from abc import ABC, abstractclassmethod



class MQTT_object(ABC):

    _server_ = None     # link to broker mqtt
    _port_   = None     # port, if you need it
    _topic   = None     # topic channel when you work



    @abstractclassmethod
    def set_server(self,server):
        self.set_server = server
        


    @abstractclassmethod
    def set_topic(self,topic):
        self.topic = topic

    @abstractclassmethod
    def get_server(self):
        return self.server
        

    @abstractclassmethod
    def get_topic(self):
        return self.topic
        



    

