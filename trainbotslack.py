import urllib2
import json
import time
import os
from prettytable import PrettyTable
import requests

#===========Initial Set Up===========#
#You need an API key so sign up to transportapi.com

url = "INSERT TRANSPORTAPI API KEY HERE"
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)


t = PrettyTable(['Time', 'Platform', 'Service'])

#===========Getting info off the API===========#
#     I got the info from here:
#     https://stackoverflow.com/questions/44169258/printing-json-elements

for info in data['departures']['all']:
    departure_time = info['aimed_departure_time']
    platform = info['platform']
    service = info['destination_name']

    t.add_row([departure_time,platform,service])

payload = {
        "text": t.get_string()
}
requests.post("INSERT SLACK WEBHOOK HERE", json=payload)
