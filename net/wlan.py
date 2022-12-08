import network
import time
import display

def wlan_connect(ssid, pw):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, pw)
    return station
