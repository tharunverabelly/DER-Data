from AWS_MQTT import AWS_mqtt
from DER_InfoV2 import DER
from DER_Ad import DER_Adv
from Encryption_Decryption import Enc_Dec
from DER_Data import DER_data
from DER_DataGen import DER_datagen
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT
import json
import os
import time
import re


# DER_folder = "/home/swansadmin/Iteration1/DER Folder/"
# DER_path = os.listdir(DER_folder)

# Dictionary to store the DER Data as key and the data packets as values in a list called DER_Packets
DER_dict = {}

### Random Data Generation ###

#  Creating an object of the DER_Adv class to access the methods required to generate the dummy data
der_obj = DER_Adv()

id = der_obj.get_ID()
# print(id)
ap = der_obj.get_ap()
s_ip = der_obj.get_src_IP()
wlan = der_obj.get_wlan_status()
salt = der_obj.get_salt_data()
# print(salt)
product = der_obj.get_product_name()
platform = der_obj.get_platform()
sysdate = der_obj.get_time()
pcb = der_obj.get_PCB_name()
hw_vr = der_obj.get_hw_vr()
sw_vrs = der_obj.get_sw_vr()
sw_vr1 = sw_vrs[0]
sw_vr2 = sw_vrs[0]
# print(sw_vr1, sw_vr2)
timestmp = der_obj.get_time()

# Creating an object of the DER class to align the generated data
der_ad = DER(id,ap,s_ip,wlan,salt,product,platform,sysdate,pcb,hw_vr,sw_vr1,sw_vr2,timestmp)
# print(der_ad,"\n************************************\n")

# Adding the object as a key and the Data_Packets as values in the Dictionary
DER_dict[der_ad] = []

# Creating an object of the DER_Data_Gen class to generate the DER Data
data_obj = DER_datagen()
id = 0
mt_loc = data_obj.get_mt_loc()
mode = data_obj.get_mode()
P_Akku = data_obj.get_P_Akku()
P_Grid = data_obj.get_P_Grid()
P_Load = data_obj.get_P_Load()
P_PV = data_obj.get_P_PV()
rel_Aut = data_obj.get_rel_Autonomy()
rel_Sc = data_obj.get_rel_SelfConsumption()
day = 0
e_day = data_obj.e_per_day()
e_month = data_obj.e_per_month()
e_year = data_obj.e_per_year()
d_ip = data_obj.dest_IP()
s_port = data_obj.source_port()
d_port = data_obj.dest_port()
ttl = data_obj.get_ttl()


# Creating an object of the DER_data class to get the formatted DER_data
der_packet = DER_data(id,mt_loc,mode,P_Akku,P_Grid,P_Load,P_PV,rel_Aut,rel_Sc,day,e_day,e_month,e_year,s_ip,d_ip,s_port,d_port,ttl)

DER_dict[der_ad].append(der_packet)
# print(der_data.Data(1),"\n-------------------------------------\n",der_data.ip_ports(s_ip))

# print(DER_dict)

for key,val in DER_dict.items():
    
    data = key.__str__()
    for i in val:
        data += "\n\n"+ i.__str__()

    # print(data)
    

## Encryption and Decryption ###

# Creating an object of the Enc_Dec class to encrypt and decrypt the file

ed_obj = Enc_Dec()

key = ed_obj.SHA("ProjectSwans")
iv = ed_obj.get_iv()
enc_text = ed_obj.EncryptionEngine(key,iv,data)
print(enc_text)
# print(type(enc_text))

# dec_text = ed_obj.DecryptionEngine(key,iv,enc_text)
# print(dec_text)

# AWS IOT MQTT

pubsub = AWS_mqtt()
# sec = json.dumps
print("Connect")
pubsub.connect()
print("Subscribe")
pubsub.subscribe()
print("Publish")
pubsub.publish(bytearray(enc_text,"utf-16"))
print("Publish Done")
time.sleep(4)
pubsub.disconnect()

sub_data = pubsub.sublist[0]
print(sub_data)
# match = re.findall((r"(?<=b')(.*)(?=')"),sub_data)[0]
# print(match)

# import struct

# def rawbytes(s):
#     """Convert a string to raw bytes without encoding"""
#     outlist = []
#     for cp in s:
#         num = ord(cp)
#         if num < 255:
#             outlist.append(struct.pack('B', num))
#         elif num < 65535:
#             outlist.append(struct.pack('>H', num))
#         else:
#             b = (num & 0xFF0000) >> 16
#             H = num & 0xFFFF
#             outlist.append(struct.pack('>bH', b, H))
#     return b''.join(outlist)

# print(rawbytes(match))
# print(type(rawbytes(match)))
# ed_obj.DecryptionEngine(key,iv,sub_data.encode("utf-8"))
