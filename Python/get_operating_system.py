"""
This script retrieves a hardware information for an specific hardware object.
It is only necessary to specify the hostname from the server.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/article/object-filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer.API

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer username and api key
API_USERNAME = 'set me'
API_KEY = 'set me'
# Define the hostname from the hardware object
hostname = 'rcdeletme'

# Declare an object filter to get an specific hardware object
filterHardware = {
    'hardware': {
        'hostname': {
            'operation': hostname
        }
    }
}

# Creates a new connection to the API service.
client = SoftLayer.API.Client(username=API_USERNAME,api_key=API_KEY)

try:
    hardwareObjects = client['SoftLayer_Account'].getHardware(filter=filterHardware, mask='mask[operatingSystem[passwords]]')
    pp(hardwareObjects)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the hardware objects faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))
