import socket
import json
from tcp_latency import measure_latency

debug = False

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

def updateData(dataStorage, dataToStore, mode="w"):
    '''
    Update the data that is being stored
    Input data and where to store it
    Do NOT change mode unless you know what the implications of that is.
    TL;DR, if mode is not w, this stuff will probably break.
    '''
    if dataToStore is None or isinstance(dataToStore, dict) is False:
        raise ValueError

    jsonData = json.dumps(dataToStore)
    try:
        with open(dataStorage, mode) as output:
            output.write(jsonData + "\n")
            return True
    except Exception as exp:
        print("Exception: " + str(exp))
        return False

def readData(dataStorage):
    try:
        with open(dataStorage, 'r') as f_input:
            for line in f_input:
                # data = json.load(f_input)
                dataDict = json.loads(line)
                global debug
                if debug:
                    i = 0
                    for (key, val) in dataDict.items():
                        i += 1
                        print(str(i) + " " + str(key) + " : avg: " + str(val.get('avg')) + " : dropped: " + str(val.get('dropped')))
                return dataDict
            return False
    except Exception as exp:
        print("Exception: " + str(exp))
        return False

def checkHost(checkType, host=None, port=80, attempts=10, timeout=4):
    checkType = str(checkType).lower()
    if (checkType == "icmp"):
        raise NotImplementedError
    elif (checkType == "tcp_up"):
        raise NotImplementedError
    elif (checkType == "latency"):
        pass
        if (host is not None):
            latency_pre = measure_latency(host=host, port=port, runs=attempts, timeout=timeout)
        else:
            raise ValueError
        sum = 0
        valid = 0
        dropped = 0
        for time in latency_pre:
            try:
                sum += time
                valid += 1
            except Exception as exp:
                global debug
                if debug:
                    print("Exception: "+ str(exp))
                dropped += 1
                #return False
        average = sum/valid
        return {"avg": float(str("%.2f" % average)), "dropped": dropped}

def checkHosts(parameterDictionary=None):
    """
    Check a dictionary of hosts with their own parameters
    parameterDictionary: a dictionary containing at least one host definition
    """
    resultDict = {}
    if parameterDictionary is None or isinstance(parameterDictionary, dict) is False:
        raise ValueError
    for name in parameterDictionary:
        global debug
        if debug:
            print(name + " ; " + parameterDictionary.get(name).get('checkType') + " ; " + parameterDictionary.get(name).get('host') + " ; " + str(parameterDictionary.get(name).get('port')) + " ; " + str(parameterDictionary.get(name).get('attempts')) + " ; " + str(parameterDictionary.get(name).get('timeout')) + " ;\n")
        try:
            tempDict = {name: checkHost(checkType=parameterDictionary.get(name).get('checkType'), host=parameterDictionary.get(name).get('host'), port=parameterDictionary.get(name).get('port'), attempts=parameterDictionary.get(name).get('attempts'), timeout=parameterDictionary.get(name).get('timeout'))}
        except Exception as exp:
            print("Exception: " + str(exp))
        if debug:
            print(tempDict)
        resultDict.update(tempDict)
    return resultDict

hostsDict = {
    "Cloudflare DNS": {
        "checkType": "latency",
        "host": "1.1.1.1",
        "port": 53,
        "attempts": 4,
        "timeout": 4
    },
    "ISI": {
        "checkType": "latency",
        "host": "integratedsolutions.net",
        "port": 80,
        "attempts": 4,
        "timeout": 4
    },
    "Tokyo": {
        "checkType": "latency",
        "host": "ty1.mirror.newmediaexpress.com",
        "port": 80,
        "attempts": 4,
        "timeout": 4
    },
    "MIT": {
        "checkType": "latency",
        "host": "mirrors.mit.edu",
        "port": 80,
        "attempts": 4,
        "timeout": 4
    },
    "Google DNS": {
        "checkType": "latency",
        "host": "8.8.8.8",
        "port": 53,
        "attempts": 4,
        "timeout": 4
    }
}

testing = False
if testing:
    import time, sys
    while True:
        try:
            updateData('network_log.json', checkHosts(hostsDict))
            print(readData('network_log.json'))
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as exp:
            print(str(exp))
