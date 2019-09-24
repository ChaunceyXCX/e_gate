import picoweb
import gpio
import network
import ujson
import wlanauto

app = picoweb.WebApp("SafeGate")
@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    htmFile = open('./static/gate.html','r')
    for line in htmFile:
        yield from resp.awrite(b""+line)
    # yield from resp.awrite()

@app.route("/wlancfg")
def wlan_cfg(req, resp):
    yield from picoweb.start_response(resp)
    htmFile = open('./static/wlancfg.html','r')
    for line in htmFile:
        yield from resp.awrite(b""+line)

@app.route("/wlanscan")
def wlan_scan(req, resp):
    yield from picoweb.start_response(resp, content_type = "application/json")
    wlan_sta = network.WLAN(network.STA_IF)
    wlans = wlanauto.wlannearby(wlan_sta)
    wlans = ujson.dumps(wlans)
    yield from resp.awrite(wlans)

@app.route("/wlanconnect")
def wlan_connect(req, resp):
    yield from picoweb.start_response(resp, content_type = "application/json")
    query_str = req.qs
    print(query_str)
    param = qs_parse(query_str)
    print(param['ssid'])
    try:
         wlan = wlanauto.get_connection(param['ssid'],param['password'])
    except OSError as e:
        print("exception", str(e))
    resp_json = {}
    resp_json['isConnected'] = 1
    resp_json = ujson.dumps(resp_json)
    yield from resp.awrite(resp_json)

def qs_parse(qs):
    parameters = {}
    ampersandSplit = qs.split("&")
    for element in ampersandSplit:
        equalSplit = element.split("=")
        parameters[equalSplit[0]] = equalSplit[1]
    return parameters

@app.route("/opengate")
def open_gate(req, resp):
    gpio.open_gate()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("open")

@app.route("/stop")
def stop(req, resp):
    gpio.stop()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("stop")

@app.route("/closegate")
def close_gate(req, resp):
    gpio.close_gate()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("close")