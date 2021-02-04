import socket
import json

def tcpCheck(ip, port, timeout):
    '''
    See if host is up
    Returns true or false
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def updateData(dataStorage, dataToStore):
    '''
    Update the data that is being stored
    Input data and where to store it
    '''
    data = {}
    jsonData = json.dumps(data)
    try:
        with open('network_log.json', 'a') as output:
            output.write(jsonData + "\n")
            return True
    except Exception as exp:
        print("Exception: " + str(exp))
        return False

def readData():
    pass

def checkHost(checkType):
    checkType = str(checkType).lower()
    if (checkType == "icmp"):
        pass
    elif (checkType == "tcp"):
        pass
