from gpiozero import LED
from time import sleep
from gpiozero import LED, Button
from signal import pause

green = LED(17)
red = LED(27)
button = Button(2)

button.when_pressed = red.off
button.when_released = red.on


