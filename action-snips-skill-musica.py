#!/usr/bin/env python3
import subprocess
import sys

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def poner_musica():
    subprocess.run(['echo "connect XX:XX:XX:XX:XX:XX" | sudo bluetoothctl'],shell=True)
    subprocess.Popen(["mpg321 -a bluealsa:HCI=hci0,DEV=XX:XX:XX:XX:XX:XX,PROFILE=a2dp '/media/networkdrive/Musica/playlist.txt'"],shell=True)
    sys.exit(0)

def quitar_musica():
    subprocess.run(['killall mpg321'],shell=True)
    subprocess.run(['echo "disconnect XX:XX:XX:XX:XX:XX" | sudo bluetoothctl'],shell=True)


def intent_received(hermes, intent_message):
    sentence = ""
        
    if intent_message.intent.intent_name == 'jaimevegas:PonMusica':
        poner_musica()
    elif intent_message.intent.intent_name == 'jaimevegas:ParaMusica':
        quitar_musica()
                       
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
