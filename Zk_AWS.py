# import zymkey
import boto3
import hashlib
import binascii
import pycurl
from OpenSSL import SSL


class ZK():

    topic = "zymkey"
    Root_Cert="/home/swan/test/AWS_CA.pem"
    Device_Cert ="/home/swan/test/zymkey.crt"
    AWS_ENDPOINT ="https://ax0vcs1zijata-ats.iot.us-east-1.amazonaws.com"+":8443/topics/"+topic+"?qos=1"


    def Publish(self, post_field):
        
        c = pycurl.Curl()

        #Setting Curl to use zymkey_ssl engine
        c.setopt(c.SSLENGINE, "zymkey_ssl")
        # c.setopt(c.SSLENGINE_DEFAULT, 1)
        c.setopt(c.SSLVERSION, c.SSLVERSION_TLSv1_2)
        
        #Settings certificates for HTTPS connection
        # c.setopt(c.SSLENGINE, "zymkey_ssl")
        # c.setopt(c.SSLCERTTYPE, "PEM")
        c.setopt(c.SSLCERT, self.Device_Cert)
        c.setopt(c.CAINFO, self.Root_Cert)
        
        #setting endpoint and HTTPS type, here it is a POST
        c.setopt(c.URL, self.AWS_ENDPOINT)
        c.setopt(c.POSTFIELDS, post_field)
        
        #Telling Curl to do client and host authentication
        c.setopt(c.SSL_VERIFYPEER, 1)
        c.setopt(c.SSL_VERIFYHOST, 2)
        
        #Turn on Verbose output and set key as placeholder, not actually a real file.
        c.setopt(c.VERBOSE, 1)
        c.setopt(c.SSLKEYTYPE, "ENG")	
        c.setopt(c.SSLKEY, "nonzymkey.key")
        
        c.perform()
        c.close()