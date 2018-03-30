#!/usr/bin/env python
import serial
import time
import sys

from tobin.hub import Tobin
from tobin.exceptions import DeviceNotFound, InvalidOperation

PORT = '/dev/ttyUSB0'
BAUDRATE = 57600

def main():
    global input

    rtu_connection = serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=8, parity='N', stopbits=1, xonxoff=0)
    tobin = Tobin(rtu_connection)
    print('Tobin connected')
    try: input = raw_input
    except NameError: pass

    tobin.start()
    try:
        print('Waiting for user input')
        while True:
            msg = input('Command to send:')
            if msg == 'close':
                tobin.stop()
                tobin.dump()
                sys.exit(0)
    except IOError:
        print('Running as daemon')

if __name__ == '__main__':
    main()