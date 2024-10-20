import time
import serial
import matplotlib.pyplot as plt


if __name__ == "__main__":
    port = '/dev/ttyACM0'
    baud = 11520
    ser = serial.Serial(port, baud)
    # print(ser.readline())
    time.sleep(5)
    ser.flush()
    idx = 0
    check = []
    while idx < 5:
        b1 = ser.readline()
        check.append(b1)
        idx += 1
    ser.close()
    print(check)