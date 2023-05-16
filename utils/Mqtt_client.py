import random
import paho.mqtt.client as mqtt
import mqtt_init 
clients_status = {}

class Mqtt_client():
    
    def __init__(self,on_message = None,subscribe = False):
        r = random.randrange(1,100000)
        self.clientname = "IOT_client-Id-"+str(r)
        clients_status[self.clientname] = False
        self.on_message = on_message  
        self.subscribe = subscribe
        
    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            print("connected OK")
            clients_status[self.clientname] = True
            if self.on_connected_action:
                self.on_connected_action()
            if self.subscribe:
                self.client.subscribe(mqtt_init.topic)

        else:
            print("Bad connection Returned code=",rc)
            
    def on_disconnect(self, client, userdata, flags, rc=0):
        clients_status[self.clientname] = False
        print("DisConnected result code "+str(rc))
            
    def on_message(self, client, userdata, msg):
        print("on_message_chen")

    def connect_to(self):
        # Init paho mqtt client class        
        self.client = mqtt.Client(self.clientname, clean_session=True) # create new client instance        
        self.client.on_connect=self.on_connect  #bind call back function
        self.client.on_disconnect=self.on_disconnect
        self.client.on_message= self.on_message
        self.client.username_pw_set(mqtt_init.username,mqtt_init.password)        
        print("Connecting to broker ",mqtt_init.broker_ip)        
        self.client.connect(mqtt_init.broker_ip,mqtt_init.port)     #connect to broker
    
    def disconnect_from(self):
        self.client.disconnect()                   
    
    def start_listening(self):        
        self.client.loop_start()        
    
    def stop_listening(self):        
        self.client.loop_stop()    
    
  
    def publish_to(self, topic, message):
        if clients_status[self.clientname]:
            self.client.publish(topic,message)        
  