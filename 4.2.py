import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]

try:
    print("Input period:")
    t = int(input())
    while True:
        for val in range(255):
            GPIO.output(dac, dec2bin(val))
            time.sleep(t/255)
        for val in range(255, 0, -1):
            GPIO.output(dac, dec2bin(val))
            time.sleep(t/255)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()