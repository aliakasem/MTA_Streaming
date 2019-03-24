import pylab as pl
import os
import json
import pprint
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    import sys 
pl.rc('font', size=15)

api_key=sys.argv[1]
bus_line=sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (api_key, bus_line)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
var1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
var1
index = 0 
for k in var1:  
    k=k['MonitoredVehicleJourney']
    print ('Bus',index,'is at latitude:', k['VehicleLocation'],['Latitude'],'Longitude',k['VehicleLocation']['Longitude'])
    index+=1