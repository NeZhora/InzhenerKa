import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
tro = 13
rang = range(255, 0, -1)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(tro, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    for i in rang:
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.01)
        if GPIO.input(14) == GPIO.LOW :
            return(i)
            break
try:
    while True:
        vall = adc()
        time.sleep(1)
        print(vall/256*3.3)

finally:
    GPIO.output(dac, 0)
    GPIO.output(tro, 0)
    
    GPIO.cleanup()