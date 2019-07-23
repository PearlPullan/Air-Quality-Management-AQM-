# -*- coding: utf-8 -*-
import time
from firebase import firebase
import serial   

#firebase = firebase.FirebaseApplication('https://dataaqm.firebaseio.com/',None)
# Enable Serial Communication
port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

def disp():
    while True:
        rcv = port.read(10)
        print rcv
    


port.write('AT'+'\r\n')
disp()

port.write('AT+CGATT =1'+'\r\n') # to attach GPRS.
disp()

port.write('AT+SAPBR =3,1,”CONTYPE”,”GPRS”'+'\r\n')
# activate bearer profile.
disp()

port.write('AT+SAPBR =3,1,”APN”,"www"'+'\r\n')
disp()

port.write('AT+SAPBR=1,1'+'\r\n')
disp()

port.write('AT+SAPBR=2,1'+'\r\n')
disp()

port.write('AT+CIPGSMLOC=1,1'+'\r\n')# to get gsm location, time and date.
disp()
result = firebase.post('/node',
                             { 'Latitude' : '1' ,'Longitude':'2'})
print (result)


port.write('AT+CIPGSMLOC=2,1'+'\r\n')# to get gsm time and date
disp()

port.write('AT+SAPBR =0,1'+'\r\n')# to deactivate bearer profile.
disp()
