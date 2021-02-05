import socket
import json
from tcp_latency import measure_latency

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

def checkHost(checkType, host=None, port=80, attempts=10, timeout=4):
    checkType = str(checkType).lower()
    if (checkType == "icmp"):
        raise NotImplementedError
    elif (checkType == "tcp_up"):
        pass
    elif (checkType == "latency"):
        pass
        if (host is not None):
            latency_pre = measure_latency(host=host, port=port, runs=attempts, timeout=timeout)
        else:
            raise ValueError
        sum = 0
        for time in latency_pre:
            sum += time
        average = sum/len(latency_pre)
        print("%.2f" % average)

checkHost("latency", "1.1.1.1")