#!/usr/bin/python

import paho.mqtt.client as mqtt #import the client1
broker_address="localhost"
client = mqtt.Client("test") #create new instance
client.connect(broker_address,1883) #connect to broker
client.publish("test","OFF")#publish
