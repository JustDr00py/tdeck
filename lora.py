from sx1262 import SX1262
from machine import Pin
from time import sleep
import machine
# Constants
machine.freq(80000000)

# LoRa initialization
sx = SX1262(spi_bus=2, clk=40, mosi=41, miso=38, cs=9, irq=45, rst=17, gpio=13)

sx.begin(freq=915, bw=250, sf=7, cr=5, syncWord=0x12,
         power=21, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

payload = input('LoRa: ')
sx.send(payload.encode('utf-8'))




