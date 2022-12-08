WIFI_SSID, WIFI_PW = "SAWLAN", "AW7H29gy"
SERVER_URL = "http://10.42.0.1:5000"

from machine import I2C, Pin
from display import Display
import sys
import time

def main():
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    display = Display(i2c)

    unsent_datapoints = []

    try:
        display.write("Ld BMP..")
        from datasources.bmp import BMP
        display.write("Ld WLA..")
        from net.wlan import wlan_connect, wlan_status_lookup
        wlan = wlan_connect(WIFI_SSID, WIFI_PW)
        while not wlan.isconnected():
            #display.write("Ld WLA.." + wlan.status())
            pass
        display.write("Ld API..")
        from net.api import send_datapoints
        bmp = BMP(i2c)

        while True:
            data = bmp.poll()
            display.write(data[0]["value"])
            unsent_datapoints += data
            time.sleep_ms(100)
            send_datapoints([data], SERVER_URL)
    except Exception as e:
        sys.print_exception(e)
        display.write(e)

main()
