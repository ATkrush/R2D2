#Florian Azemi
#17.06.2022
#Abschlussprojekt, Hardware teil

from gpiozero import CPUTemperature
from gpiozero import LED
import time

ledred = LED(17) #port auf den T coppler
ledblue = LED(27)

while 1:
    cpu = CPUTemperature()
    print(cpu.temperature)
    time.sleep(1)

    if (cpu.temperature > 46.01):
        ledred.on()
        ledblue.off()

    if(cpu.temperature < 46):
        ledred.off()
        ledblue.on()


# leds mit Vorwiderstand anschliesen!