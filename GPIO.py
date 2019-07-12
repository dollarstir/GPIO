from gpiozero import LED
from time import sleep

led = LED(17)
led1 = LED(27)

while True:
    led.on()
    sleep(1)
    led1.on()
    sleep(0.1)
    led.off()
    sleep(0.9)
    led1.off()
    sleep(0.5)
    
    
