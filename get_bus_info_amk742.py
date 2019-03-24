import os
import json
import pprint
import csv
import sys 
import pandas as pd 
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

api_key=sys.argv[1]
bus_line=sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (api_key, bus_line)
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
var1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
var1

index = 0 
#file = open('busline.csv', 'w+')
file = open(sys.argv[3], 'w')

#sys.argv[3]; 
for k in var1:  
    k=k['MonitoredVehicleJourney']
    s='Bus %s is at Latitude:%s and Longitude:%s' % (str(index), str(k['VehicleLocation']['Latitude']), str(k['VehicleLocation']['Longitude']))
    file.write(s+'\n')
    index+=1
    
file.close() #put at bottom

response =urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)
variable1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
variable1
index = 0
df_all=pd.DataFrame(columns=['latitude','Longitude','Busstop','Stopstatus'])
for k in variable1:
    k = k['MonitoredVehicleJourney']
    latitude = k['VehicleLocation']['Latitude']
    Longitude = k['VehicleLocation']['Longitude']
    if len(k['OnwardCalls']) < 1:
        Busstop='N/A'
        Stopstatus='N/A'
    else:
        Busstop = k['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Stopstatus= k['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    index+=1 
    df_all.loc[index] = [latitude,Longitude,Busstop,Stopstatus]
    #print (latitude,Longitude,Busstop,Stopstatus)
    
df_all.to_csv('bustime.csv')
