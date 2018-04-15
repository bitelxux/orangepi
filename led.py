#!/usr/bin/env python
"""Basic blinking led example.
 
"""
 
import os
import sys
 
if not os.getegid() == 0:
    sys.exit('Script must be run as root')
 
 
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
 
__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"
 
led = port.PA12
led1 = port.PA11
led2 = port.PA6
 
gpio.init()
gpio.setcfg(led, gpio.OUTPUT)
gpio.setcfg(led1, gpio.OUTPUT)
gpio.setcfg(led2, gpio.OUTPUT)
 
try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(led, 1)
        sleep(0.5)
        gpio.output(led, 0)
        sleep(0.5)
 
except KeyboardInterrupt:
    print ("Goodbye.")
