import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
tro = 13
rang = range(255, 0, -1)
volts = 0

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(tro, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]
    
def leds2bin(val):
    ll = [1]*((val//32))+[0]*((8-val//32))
    GPIO.output(leds, ll[0:8])

def adc():
    i = 255
    val = 0
    while i > 1:
        GPIO.output(dac, dec2bin(val+i)[0:8])
        time.sleep(0.002)
        if GPIO.input(comp) == GPIO.LOW:
            val += i
        i//=2
    return(val)

try:
    data = []
    secs = []
    start = time.time()
    GPIO.output(tro, GPIO.HIGH)
    while volts < 208: #выше не поднимается
        volts = adc()
        data.append(volts/256*3.3)
        secs.append(time.time()-start)
        leds2bin(volts)
        print(volts)
    GPIO.output(tro, GPIO.LOW)
    while volts > 190: #ниже не опускается
        volts = adc()
        data.append(volts/256*3.3)
        secs.append(time.time()-start)
        leds2bin(volts)
        print(volts)
    stop = time.time()
    
    print("total time:", stop-start)
    print("period: ", 1/len(data)*(stop-start))
    print("freq: ", len(data)/(stop-start), "measurments/sec")
    print("adc: ", 3.3/256)
    
    measured = [str(item) for item in data]
    with open("data.txt", "w") as out:
        out.write("\n".join(measured))
    with open("settings.txt", "w") as out:
        out.write("adc: 0.01289\n")
        out.write(str(stop-start))
         



finally:
    GPIO.output(dac, 0)
    GPIO.output(tro, 0)
    GPIO.cleanup()
    
    plt.plot(secs, data)
    plt.show()
    
