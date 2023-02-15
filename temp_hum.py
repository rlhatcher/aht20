import AHT20
import time
import paho.mqtt.client as mqtt

broker_address = "pifarmer.local"

client = mqtt.Client("Farmer")
client.connect(broker_address)

# Initialize an AHT20

aht20 = AHT20.AHT20()

while 1:

    # Fill a string with date, humidity and temperature
    client.publish("printRoom/humidity/RH%",
                   "{:10.2f}".format(aht20.get_humidity()))
    client.publish("printRoom/temp/celsius",
                   "{:10.2f}".format(aht20.get_temperature()))

    # Wait
    time.sleep(10)
