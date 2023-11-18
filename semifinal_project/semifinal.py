import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import serial
from influxdb import InfluxDBClient


THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'gLNt6D4GDSzrjC9c5r3Y'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

sensor_data = {'sensor_value': 0}
client2 = mqtt.Client()
#client3 = mqtt.Client()
# Set access token
client2.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client2.connect(THINGSBOARD_HOST, 1883, 60)
#client3.connect('mqtt://test.mosquitto.org')

#-----------------------------------------------

ser=serial.Serial(
port='/dev/ttyACM0',
baudrate=115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
file = open("testfile.txt","w")

client=InfluxDBClient(host='localhost',port=8086)

#client=InfluxDBClient(host='localhost',port=8086)
client.create_database('semi_final')
client.switch_database('semi_final')

client2.loop_start()
#client3.loop_start()
try:
    while ser.is_open:
        if ser.inWaiting()>0:
            read_serial=ser.readline()
            value = int(read_serial)
            
            file.write("%d \n"%value)
            
            sensor_data['sensor_value'] = int(read_serial)
	    
	    print(sensor_data['sensor_value'])
            
            client2.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
            
            #client3.publish('babusha',json.dumps(sensor_data),1)
            
            json_body=[
                {
                    "measurement":"semi_final_value",
                    "tags":{
                        "status":"reading"
                        },
                    "fields":{
                        "sensor value":int(read_serial)
                        }
                    }
                ]
            client.write_points(json_body)

except KeyboardInterrupt:
    pass

client2.loop_stop()
client2.disconnect()

ser.close()
file.close()
