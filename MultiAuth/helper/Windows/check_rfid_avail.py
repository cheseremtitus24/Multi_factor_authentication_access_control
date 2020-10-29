from serial.tools import list_ports


def is_available():
    try:
        cdc = next(list_ports.grep("CH340"))
        if (cdc):
            print("Device was found ")
            return  True
    except:
        print("Device was not found")
        return False


# is_available()
