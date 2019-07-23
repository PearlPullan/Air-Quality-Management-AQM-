#!/usr/bin/python3

from firebase import firebase
import time
import sensor
import pigpio
import datetime

#https://dataaqm.firebaseio.com/
firebase = firebase.FirebaseApplication('https://ppd42ns.firebaseio.com/',None)

pi=pigpio.pi()
s=sensor.sensor(pi,7)
ava=0;
while True:
      prev=ava;
      print('prev')
      print(str(prev))
      avaqi=0;
      avconc=0;
    # average reading after every 2 minutes
      #read after 30 seconds
      for i in range(0,4):
      	time.sleep(30) 
      	g, r, c = s.read()
      	aqi,conc= s.function(c)
      	a=int(aqi)
      	b=int(conc)
      	print(str(a))
      	if(aqi>150):
            now = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")
            r = firebase.post('/aqm',
                              { 'Alert' : 'Poor AQI ','timestamp' : str(now) })
            print(r)
            
      	avaqi=avaqi+a
      	avconc=avconc+b
      			
      ava=avaqi/4
      avc=avconc/4
      now = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")
      result = firebase.post('/aqm',
                             { 'PM25' : str(avc),'AQI':str(ava), 'timestamp' : str(now)})
      print(" Air quality measurements for PM 2.5 (2 minute avg) " + str(avc) + " ugm^3")
      print(" Current AQI (2 minute avg): " + str(ava))
      if(prev!=ava or prev!=ava+1 or prev!=ava+4 or prev!=ava+3 or prev!=ava +2 or prev!=ava-1 or prev!=ava-4  or prev!=ava-2 or prev!=ava-3 ):
          re = firebase.post('/aqm',
                              { 'Alert' : 'unusual reading ' ,'timestamp' : str(now)})
          print(re)
      
      time.sleep(5)
      print(result)
      #pi.stop() # Disconnect from Pi.

      #time.sleep(5)                       

