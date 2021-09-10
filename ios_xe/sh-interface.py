from ncclient import manager
import sys
import xml.dom.minidom

HOST = "10.10.20.48"
PORT = 830
USER = "developer"
PASS = "C1sco12345"

#import xml file
INCLUDE = 'sh_interfaces.xml'
def get_configures_interfaces(xml_filter):
    with manager.connect(host=HOST, port=PORT,
                        username=USER, password=PASS, hostkey_verify=False,
                        device_params={'name': 'default'},
                        allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read() )) 

def main():

interfaces = get_configures_interfaces(INCLUDE)
print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())

if __name__ == '__main__':
    sys.exit(main())