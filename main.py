WIFI_SSID, WIFI_PW = "SAWLAN", "AW7H29gy"
SERVER_URL = "http://10.42.0.1:5000"

from machine import I2C, Pin
from display import Display
import sys
import time

def main():
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    display = Display(i2c)

def wlan_status_lookup(status):
    status_lookup_table = {
        network.STAT_IDLE: "STAT_IDLE",
        network.STAT_CONNECTING: "STAT_CONNECTING",
        network.STAT_WRONG_PASSWORD: "STAT_WRONG_PASSWORD",
        network.STAT_NO_AP_FOUND: "STAT_NO_AP_FOUND",
        network.STAT_CONNECT_FAIL: "STAT_CONNECT_FAIL",
        network.STAT_GOT_IP: "STAT_GOT_IP"
    }
    return status_lookup_table[status]

    unsent_datapoints = []

    try:
        display.write("Ld BMP..")
        from datasources.bmp import BMP
        display.write("Ld WLA..")
        from net.wlan import wlan_connect, wlan_status_lookup
        wlan = wlan_connect(WIFI_SSID, WIFI_PW)
        while not wlan.isconnected():
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
