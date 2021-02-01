import configparser, sys
from pysnmp import hlapi
from quicksnmp import get

# Read config
try:
    config = configparser.ConfigParser()
    config.read_file(open(r'C:\Users\foo\Documents\GitHub\net-mon\config.ini'))
except Exception as exp:
    print(str(exp))
    sys.exit()

community = config.get('General', 'community')

print(get('10.0.0.1', ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData(community)))