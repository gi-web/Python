from gpiozero import LED
from time import sleep

led=LED(4) #4번 핀에 연결

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
