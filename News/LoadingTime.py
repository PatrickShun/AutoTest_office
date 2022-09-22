from time import sleep

def LongLoadingTime():
    sleep(10)


def shotaLoadingTime():
    sleep(1)
    print(ivalue)


def MyValue():
    global ivalue
    global idict
    ivalue = "hahaha"
    idict = {}


def _set(name,value):
    try:
        idict[name] = value
        return True
    except:
        return False



