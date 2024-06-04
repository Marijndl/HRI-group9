import nao_nocv_2_1 as nao
from naoqi import ALProxy
import time
import keyboard

robot_ip = "192.168.0.116"
port = 9559  # Robot port number
base_dir = "/home/nao/group_09/"

dialog_p = ALProxy('ALDialog', robot_ip, port)
memory_p = ALProxy('ALMemory', robot_ip, port)

def DeactivateTopic(topic, module_name='MyModule'):
    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe(module_name)

topics = ['PracticalQuestion', 'Painting', 'vanGogh', 'PSV']

for topic in topics:
    try:
        DeactivateTopic(topic)
        print("Succesfully deactivated: " + str(topic))
    except:
        print("Unsuccesfully deactivated: " + str(topic))
        pass