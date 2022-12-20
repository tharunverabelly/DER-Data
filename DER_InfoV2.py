from time import time
from datetime import datetime
import random
import string


class DER:
    
    def __init__(self,id,ap,src_IP,wlan,salt_data,product_name,platform,sysdate,pcb,hw_vr,sw_vr1,sw_vr2,time_stmp):
        
        self.id = id
        self.ap = ap
        self.src_IP = src_IP
        self.wlan = wlan
        self.salt_data = salt_data
        self.product_name = product_name
        self.platform = platform
        self.sysdate = sysdate
        self.pcb = pcb
        self.hw_vr = hw_vr
        self.sw_vr1 = sw_vr1
        self.sw_vr2 = sw_vr2
        self.time_stmp = time_stmp
    
    def __str__(self):
        return "ID: {}\nConnectedviaAP: {}\nremoteAddr: {}\nwlanAvailabale: {}\nsalt: {}\nproduct_Name: {}\nplatform: {}\nsystemDate: {}\nPCBname: {}\nhw_version: {}\nswVersion: {}\nnewSwversion:{}\nTimeStamp: {}".format(self.id,self.ap,self.src_IP,self.wlan,self.salt_data,self.product_name,self.platform,self.sysdate,self.pcb,self.hw_vr,self.sw_vr1,self.sw_vr2,self.time_stmp)


# obj = DER(1,1,1,1,1,1,1,1,1,1,1,1,1)

# print(obj)