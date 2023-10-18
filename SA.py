import Line
import config

ServerURL = config.ServerURL #For example: 'https://iottalk.tw'
MQTT_broker = config.MQTT_broker # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = config.MQTT_port
MQTT_encryption = config.MQTT_encryption
MQTT_User = config.MQTT_User
MQTT_PW = config.MQTT_PW

device_model = 'LineNotify'
ODF_list = ['Msg-O']
device_id = 'LineNotify_default_idX' #if None, device_id = MAC address
device_name = config.device_name
exec_interval = config.polling_cycle  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

    
def Msg_O(data:list):
    Line.notify(data[0])
   
