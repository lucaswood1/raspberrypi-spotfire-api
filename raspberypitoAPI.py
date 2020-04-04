import time
from multiprocessing import Pool
import os
import datetime
import requests
import csv
from pprint import pprint
import argparse
from functions import get_well_identifier, post_new_well, post_live_production, get_well_identifier
import sys
import Adafruit_DHT
 
 
while True:
PETRO_URL = 'https://<YOUR PETRO.AI SERVER>/api/'
freq_seconds = 3
wellId = 'COFFEE 001'
endpoint = 'RealTimeProduction'
 
pwi = '5ce813c9f384f2057c983601'
 
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
 
# Un-comment the line below to convert the temperature to Fahrenheit.
temperature = temperature * 9/5.0 + 32
 
if temperature is not None:
    casingtemp = temperature
else:
    casingtemp = 0
    sys.exit(1)
 
try:
    post_live_production(endpoint, pwi, 0, casingtemp, 0, 0, 0, 0, 0, 0, PETRO_URL)
except:
    pass
    print((wellId + " Tag sent to " + PETRO_URL + endpoint + " at "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    time.sleep(freq_seconds)