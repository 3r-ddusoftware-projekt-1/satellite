from machine import I2C, Pin
from display import Display
import sys

def main():
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    display = Display(i2c)

    try:
        display.write("Ld BMP..")
        from datasources.bmp import BMP
        bmp = BMP(i2c)
        data = bmp.poll()
        display.write(data[0]["value"])
    except Exception as e:
        display.write(e)
        sys.print_exception(e)

main()
