# Streaming real-time bus data from MTA through the MTA Bus Time interface

There are two scripts:

## 1. A python script to retrieve and report information about active vehicle for a bus line.

`python show_bus_locations_amk742.py <MTA_KEY> <BUS_LINE>`

For example <BUS_LINE> could be B52:

`python show_bus_locations_amk742.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52`

The above command fetches data from the MTA website through the SIRI API using the provided key and return information on all available vehicles for the bus line <BUS_LINE> (e.g. B52).

__The program
outputs the following to the console:__ 
- the bus name, 
- the number of vehicles
- their current position

### SAMPLE OUTPUT:
```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```

## 2. A python script that displays information on the next stop location of all buses of a given line.

```
python get_bus_info_amk742.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv
```

__it outputs to a CSV file named \<BUS_LINE>.csv__:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```
