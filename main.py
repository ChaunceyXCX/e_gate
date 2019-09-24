import wlanauto
import webserver
import gpio
import webrepl
# import webapp
ssid = ""
password = ""

wlan = wlanauto.get_connection(ssid,password)

if wlan is None:
    print("Could not initialize the network connection.")
    wlan = wlanauto.ap(True)
    gpio.blink(0)
else:
    gpio.on()


print("ESP OK")
ip = wlan.ifconfig()
print(ip)
print(ip[0])
wlanauto.ap(True)
webrepl.start()
# wlanauto.forward()


webserver.app.run(debug=-1, host=ip[0])
# webapp.app.run(debug=-1, host=ip[0])
