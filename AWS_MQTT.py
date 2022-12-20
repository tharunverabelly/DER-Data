import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT

class AWS_mqtt:

    # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE(js_file)
    ENDPOINT = "ax0vcs1zijata-ats.iot.us-west-2.amazonaws.com"
    CLIENT_ID = "Project Swans"
    PATH_TO_CERTIFICATE = "/home/swansadmin/HostFiles/Keys/certificate.pem.crt"
    PATH_TO_PRIVATE_KEY = "/home/swansadmin/HostFiles/Keys/private.pem.key"
    PATH_TO_AMAZON_ROOT_CA_1 = "/home/swansadmin/HostFiles/Keys/AmazonRootCA1.pem"
    TOPIC = "test/testing"
    sublist = []


    #Configuring the Endpoint and Credentials based on the Client ID and configuring the MQTT client
    myAWSIoTMQTTClient = AWSIoTMQTT.AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1,32,20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
    myAWSIoTMQTTClient.configureDrainingFrequency(2)
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)

    def connect(self):
        self.myAWSIoTMQTTClient.connect()

    def publish(self,data):
        self.myAWSIoTMQTTClient.publish(self.TOPIC,data,1)

    def subtest(self,samp,params,packet):
        # print("Topic:", packet.topic)
        # print("Payload:", (packet.payload))
        # print(packet.payload.decode("utf-8")) 
        data = packet.payload.decode("utf-8")
        self.sublist.append(data)
        # print(data)

    def subscribe(self):
        self.myAWSIoTMQTTClient.subscribe(self.TOPIC,1,self.subtest)

    def disconnect(self):
        self.myAWSIoTMQTTClient.disconnect()
