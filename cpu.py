from gpiozero import CPUTemperature
from gpiozero import LED
import time

ledred= LED(17)
ledblue= LED(27)

while 1:
    cpu = CPUTemperature()
    print(cpu.temperature)
#    str1=repr(cpu)
    datei= open('temperaturen.txt','w')
    datei.write(str(cpu.temperature))
    datei.close()
    time.sleep(1)


    if (cpu.temperature > 46.01):
       ledred.on()
