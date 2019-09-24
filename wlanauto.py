import network
import time
import socket

ap_ssid = ""
ap_password = ""
ap_authmode = 3  # WPA2

wlan_ap = network.WLAN(network.AP_IF)
wlan_sta = network.WLAN(network.STA_IF)

def get_connection(ssid,password):
    """return a working WLAN(STA_IF) instance or None"""
    # First check if there already is any connection:
    if wlan_sta.isconnected():
        return wlan_sta

    connected = False
    try:
        # ESP connecting to WiFi takes time, wait a bit and try again:
        time.sleep(3)
        if wlan_sta.isconnected():
            return wlan_sta

        # Search WiFis in range
        wlan_sta.active(True)
        connected = do_connect(ssid,password)

    except OSError as e:
        print("exception", str(e))

    # start web server for connection manager:
    # if not connected:
    #     connected = start()

    return wlan_sta if connected else None

def do_connect(ssid, password):
    print(ssid)
    wlan_sta.active(True)
    if wlan_sta.isconnected():
        return wlan_sta.isconnected()
    print('Trying to connect to %s...' % ssid)
    wlan_sta.connect(ssid, password)
    for retry in range(100):
        connected = wlan_sta.isconnected()
        if connected:
            break
        time.sleep(0.2)
        print('.', end='')
    if connected:
        print('\nConnected. Network config: ', wlan_sta.ifconfig())
    else:
        print('\nFailed. Not Connected to: ' + ssid)
    return connected


def ap(switch):
    wlan_ap = network.WLAN(network.AP_IF)
    if switch:
        wlan_ap.config(essid=ap_ssid, password=ap_password)
        wlan_ap.active(True)
        return wlan_ap
    else:
        wlan_ap.active(False)
        return wlan_ap

def wlannearby(wlan_sta):
    networks = wlan_sta.scan()
    wlans = []
    AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
    for ssid, bssid, channel, rssi, authmode, hidden in sorted(networks, key=lambda x: x[3], reverse=True):
        wlan = {}
        ssid = ssid.decode('utf-8')
        wlan["ssid"] = ssid
        wlan["channel"] = channel
        wlan["rssi"] = rssi
        wlans.append(wlan)
        print("ssid: %s chan: %d rssi: %d " % (ssid, channel, rssi))
    return wlans


def forward():

    port=10000
    listenSocket=None
    
    port2=5000
    ip2='192.168.100.10'
    
    
    try:
        #   ip=wlan.ifconfig()[0]
        
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((ip2,port2))
        
        listenSocket = socket.socket()
        listenSocket.bind((ip2,port))
        listenSocket.listen(1)
        listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print ('tcp waiting...')
    
        while True:
            print("accepting.....")
            conn,addr = listenSocket.accept()
            print(addr,"connected")
        
            while True:
                data = conn.recv(1024)
                if(len(data) == 0):
                    print("close socket")
                    conn.close()
                    break
                print(data)
                ret = s.send(data)
    except:
        if(listenSocket):
            listenSocket.close()
