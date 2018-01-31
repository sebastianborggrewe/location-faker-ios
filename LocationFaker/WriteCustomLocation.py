#!/usr/bin/python
latitude = raw_input("Latitude: ").replace(",",".")
longitude = raw_input("Longitude: ").replace(",",".")

f = open('CustomLocation.gpx', 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" creator="gpx-poi.com"><wpt lat="'+latitude+'" lon="'+longitude+'"><time>2016-11-16T12:55:06Z</time><name>Custom Location</name></wpt></gpx>')
f.close()
