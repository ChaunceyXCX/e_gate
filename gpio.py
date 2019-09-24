from machine import Pin,Timer
import time
import machine


button_key = 0
led_key = 2
open_gate_key = 14
stop_key = 12
close_gate_key = 13
led = Pin(led_key,Pin.OUT,0)
open_pin = Pin(open_gate_key,Pin.OUT,0)
stop_pin = Pin(stop_key,Pin.OUT,1)
close_pin = Pin(close_gate_key,Pin.OUT,0)


def on():
    global led
    led.value(0)
    global stop_pin
    stop_pin.value(1)

def blink(times):
    global led
    if (times==0):
        while 1:
           led.value(not led.value()) 
    for step in range(times):
        led.value(not led.value())
        time.sleep(0.05)
    led.value(0)


def open_gate():
    pin = Pin(open_gate_key,Pin.OUT)
    pin.value(1)
    time.sleep(0.05)
    pin.value(0)
    blink(3)
    print("gpio ok")

def stop():
    global stop_pin
    stop_pin.value(0)
    time.sleep(0.1)
    stop_pin.value(1)
    blink(3)
    print("gpio ok")

def close_gate():
    pin = Pin(close_gate_key,Pin.OUT)
    pin.value(1)
    time.sleep(0.05)
    pin.value(0)
    blink(3)
    print("gpio ok")






