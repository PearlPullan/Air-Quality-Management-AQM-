# Air-Quality-Management-AQM-
Using Raspberry Pi 3 (RPi3), PPD42NS Dust Sensor, SIM800L EvB and uploading the data on real-time database of Firebase


To upload the data collected by PPD42NS module to Firebase
Steps-
1. Download both to the root folder i.e. /home/pi
2. Open RPi3 terminal
       
       2.1 sudo pigpiod
       
       2.2 sudo python fblink.py
       
       
 FYI
 1. Install and configure pigpiod
     sudo apt-get update
     sudo apt-get install pigpio
     pigpiod -v
 2. Install firebase
     sudo pip install requests
     sudo pip install python-firebase
  sudo apt-get install python-pip 
  sudo pip install pyrebase

