#penambahan fitur relay

    
import time, sys
import cv2
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
import mysql.connector
import datetime
import RPi.GPIO as GPIO
from hikvisionapi import Client
import numpy as np
import base64
from PIL import Image
import PIL
import requests
import json
import os
import time



ketinggian_air = 0
last_kalibrasi = 0
response2 = os.system("sudo -S pigpiod")

'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #pin Relay Modem
GPIO.output(4, GPIO.LOW)#kondisi mati

GPIO.setup(17, GPIO.OUT) #pin Relay Kamera
GPIO.output(17, GPIO.LOW)#kondisi mati
'''
tinggi_sensor = 752

#SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 3
#SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 2

siaga1 = 201
siaga2 = 150
siaga3 = 100
set_millis = 0
lvl_siaga1 = 1800000
lvl_siaga2 = 3600000
lvl_siaga3 = 10800000
lvl_siaga4 = 21600000
status = ""
flag_status = 0
last_flag_status = 0
imei = "088298203821"
lastupdate_jam = ""
url = "https://posduga.sysable.io/api/sendjsondata"
url1 = "https://posduga.sysable.io/api/api-device-by-imei/088298203821"
jadwal_pengiriman = ""
current_time = ""
date = ""


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


last_ketinggian_air = 0
ketinggian_air_fix = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

def converter_json(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def check_ping():
    hostname = "192.168.1.64"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    print("check ping : " + str(response))
    if response == 0 or response == 512 :
        pingstatus = "Kamera Dapat Tersambung"
    else:
        pingstatus = "Kamera error"

    return response

def check_url(hostname):
    response = os.system("ping -c 1 " + hostname)
    print("response url :" + str(response))
    if response == 0 or response == 512:
        pingstatus = "Terkoneksi Ke Internet"
        #print("Terkoneksi ke Internet")
    else:
        pingstatus = "Internet Error"
        #print("Trying to Route to Dns Server")
        
        time.sleep(10)
    
        response = os.system("ping -c 1 " + hostname)
        #print(response)
    return response

def compress_img(nama_file):
   file_name = 'image-4-compressed.jpg'
   im = Image.open(nama_file)
   im.save(file_name,optimize=True,quality=20)
   with open(file_name,"rb") as im:
       img_base64 =  base64.b64encode(im.read()).decode('utf-8')
       return img_base64


class PWM_read:
   def __init__(self, pi, gpio):
      self.pi = pi
      self.gpio = gpio

      self._high_tick = None
      self._p = None
      self._hp = None

      self._cb = pi.callback(gpio, pigpio.EITHER_EDGE, self._cbf)

   def _cbf(self, gpio, level, tick):
      global ketinggian_air, tinggi_sensor
   
      if level == 1:
         if self._high_tick is not None:
            self._p = pigpio.tickDiff(self._high_tick, tick)
         self._high_tick = tick
      elif level == 0:
         if self._high_tick is not None:
            self._hp = pigpio.tickDiff(self._high_tick, tick)
      if (self._p is not None) and (self._hp is not None):
          period = 1 / (1000000.0/self._p)
          
          if ((int(self._hp/58) != 0) and (int(self._hp/58)<tinggi_sensor)):
              ketinggian_air = int(tinggi_sensor - self._hp/58)
          else:
              ketinggian_air = 10000
         #print(self.tempdistance)
         #ketinggian_air = self._hp/58
         #print(ketinggian_air)
         #print("g={} f={:.1f} dc={:.3f} distance ={:.3f}".  
          #  format(gpio, 1000000.0/self._p, self._hp , self._hp/58))
            
   def cancel(self):
      self._cb.cancel()
      
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def kirim_data(data,img, waktu, tanggal):
    if (check_ping() == 0):
        img = "data:image/png;base64," + str(img)
    else :
        img = " "
    #data=json.dumps
    waktu = "" + str(waktu)
    tanggal = "" + str(tanggal)
    data_fix = {"foto_cam":img,"ketinggian_air":data,"imei":imei, "waktu":waktu, "tanggal":tanggal }
    try:
        r = requests.post(url, data=json.dumps(data_fix), headers=headers)
        
        
        data = r.__dict__['_content']
        print("Cek response", type(data))
        r.close()
    except requests.exceptions.ConnectionError:
        print(r)
        get_data_durasi()

def get_data_durasi():
    global siaga1, siaga2, siaga3, siaga4, lvl_siaga1, lvl_siaga2, lvl_siaga3, lvl_siaga4, jadwal_pengiriman
    try : 
        r =  requests.get(url=url1)
        data = r.json()
        siaga1 = data['data'][0]['siaga']['min_siaga_1']
        siaga2 = data['data'][0]['siaga']['min_siaga_2']
        siaga3 = data['data'][0]['siaga']['min_siaga_3']
        lvl_siaga1 = (data['data'][0]['siaga']['durasi_siaga_1'])*1000
        lvl_siaga2 = (data['data'][0]['siaga']['durasi_siaga_2'])*1000
        lvl_siaga3 = (data['data'][0]['siaga']['durasi_siaga_3'])*1000
        lvl_siaga4 = (data['data'][0]['siaga']['durasi_siaga_4'])*1000
        siaga3 = data['data'][0]['siaga']['min_siaga_3']
        lastupdate = data['last_update']
        jadwal_pengiriman = lastupdate[11:19]
        print("Jadwal Pengiriman :" + jadwal_pengiriman)
        #jadwal_pengiriman = (data['data'][0]['siaga']['updated_at'])
        #kirim_data_full()
    except requests.exceptions.ConnectionError:
        
        print(r)
    

def kirim_data_full():
    #GPIO.output(4, GPIO.HIGH)#Modem hidup 
    #GPIO.output(17, GPIO.HIGH)#Kamera Hidup
    global jadwal_pengiriman, current_time, date
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
       
    date = datetime.datetime.now().date()

    print("Booting Camera and Modem 4G")
    #time.sleep(120)
    #os.system('sudo route add 27.131.0.10 gw 192.168.100.1')
    if (check_ping() == 0):
        time.sleep(2)
        cam = Client('http://192.168.1.64', 'admin', 't4ng3r4ng')
        print("starting picture capture")
        vid = cam.Streaming.channels[102].picture(method ='get', type = 'opaque_data')
        bytes = b''
        with open('img.png', 'wb') as f:
            for chunk in vid.iter_content(chunk_size=1024):
                bytes += chunk
                a = bytes.find(b'\xff\xd8')
                b = bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes[a:b+2]
                    bytes = bytes[b+2:]
                    i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imwrite('img.png', i)
                    #cv2.imshow('i', i)
    else :
      print("CCTV NOT DETECTED")

    

    hostname = "posduga.sysable.io"
    if(check_url(hostname) == 0 or check_url(hostname) == 512):
      buffer_img = compress_img('img.png')
      if(check_ping()) == 0 :
          
          #print("waktu :" + converter_json(current_time))
          
          
          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          #print("Response :" + response)
      else :
          dump = " "
          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          print(response)
      #print("Full response" , response.__dict__)
    else :
        print("No Internet")
    jadwal_pengiriman = response

      

    #GPIO.output(4, GPIO.LOW)#Modem Mati 
    #GPIO.output(17, GPIO.LOW)#Kamera Mati   
    
def main():
   global set_millis,status, ketinggian_air, ketinggian_air_fix, last_ketinggian_air, tinggi_sensor, flag_status, last_flag_status, last_kalibrasi, current_time, date
   pwm_millis = round(int(time.time() * 1000))
   print("Initiate Kalibrasi Sensor ......")
   pi = pigpio.pi()
   for i in range(10):
       p1 = PWM_read(pi, 12)
       time.sleep(1)
       if (i == 0):
           last_kalibrasi = ketinggian_air
       if ((ketinggian_air < last_kalibrasi) and (last_kalibrasi != 0)):
           last_ketinggian_air = ketinggian_air
           last_kalibrasi = ketinggian_air
           
       print(ketinggian_air)
       #print(last_ketinggian_air)
       
   if (check_url(url1) == 0 or check_url(url1) == 512) :
       print("Update Data")
       get_data_durasi()

   while True :
       current_millis = round(int(time.time() * 1000))
       t = time.localtime()
       current_time = time.strftime("%H:%M:%S", t)
       
       date = datetime.datetime.now().date()

       if (current_millis - pwm_millis) > 10000 :
          p1 = PWM_read(pi, 12)
          time.sleep(1)
          print("Current Time : " + current_time)

          #print("Real Ketinggian_air :", int(ketinggian_air))
          #filter noise sensor
          if(abs(ketinggian_air - last_ketinggian_air)>50 and last_ketinggian_air != 0 and ketinggian_air != 0):
              ketinggian_air_fix = last_ketinggian_air
              print("filter noise")
          else :
              ketinggian_air_fix = ketinggian_air
              last_ketinggian_air = ketinggian_air
          pwm_millis = current_millis
             
          print("Ketinggian_air :", ketinggian_air_fix)
          #print("Last_ketinggian:",int(last_ketinggian_air))

          p1.cancel()
          
          if(int(ketinggian_air_fix) > siaga1):
              flag_status = 1
              set_millis = lvl_siaga1
              status =  "siaga1"
          elif(int(ketinggian_air_fix) > siaga2):
              flag_status = 2
              set_millis = lvl_siaga2
              status =  "siaga2"
          elif(int(ketinggian_air_fix) > siaga3):
              flag_status = 3
              set_millis = lvl_siaga3
              status =  "siaga3"
          else:
              flag_status = 4
              set_millis = lvl_siaga4
              status =  "siaga4"
              print("Durasi Pengiriman : " ,(set_millis/(1000*60)) ," menit")
              print("Status : ", status)
              print("flag_status: ", flag_status)
    
          if (flag_status != last_flag_status and last_ketinggian_air != 0 and last_flag_status !=0):
              camera_millis = current_millis
              print("perubahan status")
              #kirim_data_full()
              last_flag_status = flag_status    
              last_ketinggian_air = ketinggian_air_fix 
            
          kirim_data_full()
    
       if (current_time == lastupdate_jam):
           kirim_data_full()
   
         


if __name__ == '__main__':
   main()


   
