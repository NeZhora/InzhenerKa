import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]



try:
    print("Input 0-255 number:")
    num = input()
    if num != 'q':
        GPIO.output(dac, dec2bin(int(num)))
        print("v~~ ", 3.3*(int(num)/255), " volts")
        time.sleep(1000)
        print("done")
    else:
        print("Stopped")
except:
    if (not num.isdigit()) and (num != 'q'):
        print("Input number, not a letter!")    
    if (int(num) > 255 or int(num) < 0) and num.isdigit():
        print("Wrong value!")
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

