#!flask/bin/python
import os
import sys
from flask import Flask

app = Flask(__name__)

if not os.getegid() == 0:
    sys.exit('Script must be run as root')
 
from pyA20.gpio import gpio
from pyA20.gpio import port
 
living_room = port.PA6
kitchen = port.PA12
 
gpio.init()
gpio.setcfg(kitchen, gpio.OUTPUT)
gpio.setcfg(living_room, gpio.OUTPUT)
 
@app.route('/kitchen/on')
def kitchen_on():
    gpio.output(kitchen, 1)
    return "Kitchen light is on\n"

@app.route('/kitchen/status')
def kitchen_status():
    result = gpio.input(kitchen)
    status = "on" if result else "off"
    return "Kitchen light is %s\n" % status

@app.route('/kitchen/off')
def kitchen_off():
    gpio.output(kitchen, 0)
    return "Kitchen light is off\n"

@app.route('/living_room/on')
def living_room_on():
    gpio.output(living_room, 1)
    return "Living room light is on\n"

@app.route('/living_room/status')
def living_room_status():
    result = gpio.input(living_room)
    status = "on" if result else "off"
    return "Living room light is %s\n" % status

@app.route('/living_room/off')
def living_room_off():
    gpio.output(living_room, 0)
    return "living room light is off\n"

@app.route('/all_lights/on')
def all_on():
    gpio.output(kitchen, 1)
    gpio.output(living_room, 1)
    return "All lights are on\n"

@app.route('/all_lights/status')
def all_lights_status():
    result = gpio.input(living_room)
    status_living_room = "on" if result else "off"
    result = gpio.input(kitchen)
    status_kitchen = "on" if result else "off"
    ret1_value = "Living room light is %s\n" % status_living_room
    ret2_value = "Kitchen light is %s\n" % status_kitchen
    return ret1_value + ret2_value

@app.route('/all_lights/off')
def all_off():
    gpio.output(kitchen, 0)
    gpio.output(living_room, 0)
    return "All lights are off\n"

if __name__ == '__main__':
        app.run(host="0.0.0.0", threaded=True, debug=True)

