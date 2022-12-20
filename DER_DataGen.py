import random

class DER_datagen:

    def get_mt_loc(self):
        return "unknown"
    
    def get_mode(self):
        return "produce-only"

    def get_P_Akku(self):
        return "null"

    def get_P_Grid(self):
        return "null"

    def get_P_Load(self):
        return "null"

    def get_P_PV(self):
        return "null"

    def get_rel_Autonomy(self): 
        return "null"
    
    def get_rel_SelfConsumption(self):
        return "null"

    def e_per_day(self):
        en_day = random.randint(0, 99)
        return str("%.2f" % en_day)

    def e_per_month(self):
        en_total = random.randint(0, 999)
        return str("%.2f" % en_total)
    
    def e_per_year(self):
        en_year = random.randint(0, 99999)
        return str("%.2f" % en_year)
    
    def dest_IP(self):
        d_addr = "192.167.11."
        add = random.randint(0, 255)
        return d_addr + str(add)

    def source_port(self):
        return random.randint(0,65535)
    
    def dest_port(self):
        return random.randint(0,65535)

    def get_ttl(self):
        return 100
