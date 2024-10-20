import time
import serial
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html

import matplotlib.pyplot as plt
import datetime
"""
Example of serial monitor data with timestamp from Arduino
22:27:29.230 -> 80,958,745
22:27:29.263 -> 80,958,991
22:27:29.263 -> 80,958,991
22:27:29.296 -> 80,958,991
22:27:29.296 -> 80,958,991
22:27:29.329 -> 80,958,991
22:27:29.362 -> 80,958,991
22:27:29.362 -> 80,958,991
22:27:29.395 -> 80,958,991
22:27:29.395 -> 80,958,991
22:27:29.429 -> 80,958,991
22:27:29.462 -> 80,958,991
22:27:29.462 -> 80,958,991
22:27:29.495 -> 80,958,991
22:27:29.528 -> 80,958,991

https://github.com/WorldFamousElectronics/PulseSensorPlayground/blob/master/resources/PulseSensor%20Playground%20Tools.md

Based on pulse sensor documentation the library prints
BPM, IBI, PulseSensorRawSignal
BPM -> beats per minute
IBI -> interbeat interval


"""

if __name__ == "__main__":
    port = '/dev/ttyACM0'
    baud = 115200
    # port immediately opened on object creation
    ser = serial.Serial(port, baud)
    idx = 0
    # time.sleep(5)
    while idx < 10:
    #     # print(ser.readline())
        idx += 1
        ans = ser.readline()
    # ser.close()
    start_time = time.time()
    # ans = ser.readline()
    ser.close()
    print(ans)
    # print(ans)
    # print(type(ans))
    # print(len(ans))
    # print(f"This is the ans byte: {ans}")
    # for i in range(len(ans)):
    #     print(f"This is index: {i} and byte: {ans[i]}")

    bpm_idx = 0
    for i in range(len(ans)):
        if ans[i] == 44:
            bpm_idx = i
            break
    print(ans[:bpm_idx].decode('utf-8'))
    print((time.time()-start_time))
    print(ans)
    """
    output from ser.readline()
    b'65,994,491\r\n'
    the class is bytes
    length is 12

    The bytes at each index refer to the ascii values
    This is index: 0 and byte: 54
    This is index: 1 and byte: 53
    This is index: 2 and byte: 44
    This is index: 3 and byte: 57
    This is index: 4 and byte: 57
    This is index: 5 and byte: 52
    This is index: 6 and byte: 44
    This is index: 7 and byte: 52
    This is index: 8 and byte: 57
    This is index: 9 and byte: 49
    This is index: 10 and byte: 13
    This is index: 11 and byte: 10
    """

    
