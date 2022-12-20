from time import time
from datetime import datetime
import random
import string


class DER_Adv:

    def get_ID(self):
        return random.randint(1000,9999)

    def get_ap(self):
        return False

    def get_src_IP(self):
            rm_addr = "192.168.11."
            # port = random.randint(0,99)
            addr = random.randint(0, 255)
            ip = rm_addr + str(addr)
            return ip

    def get_wlan_status(self):
        return True

    def get_salt(self):
        characters = string.ascii_lowercase + string.digits
        salt = ""
        for i in range(8):
            salt += "".join(random.choice(characters))
        return salt

    def get_salt_data(self):
        return {"admin": self.get_salt(), "service": self.get_salt(), "user": ""}

    def get_product_name(self):
        return "Fronius Data Manager"

    def get_platform(self):
        return "arm-wilma"

    def get_time(self):
        today = datetime.now()
        # print("Current date and time is", today)
        d_t = datetime.isoformat(today)
        # print("Date & Time:", date_as_string)
        return d_t

    def get_PCB_name(self):
        return "WILMA20"

    def get_hw_vr(self):
        return "2.4E"

    def get_sw_vr(self):
        update = random.randint(1, 9)
        sw = "3.23." + str(update) + "-" + str(random.randint(0, 9))
        update += 1
        sw2 = "3.23." + str(update) + "-" + str(random.randint(0, 9))
        return sw, sw2

    def isWlanCapable(self):
        return True