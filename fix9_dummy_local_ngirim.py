

from __future__ import print_function 
import time, sys
import cv2
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
import mysql.connector
import datetime as dt
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
import ast
import insert
import MySQLdb
from datetime import timedelta, datetime



ketinggian_air = 0
last_kalibrasi = 0
response2 = os.system("sudo -S pigpiod") #menjalankan pigpiod

tinggi_sensor = 800

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
status = 0
flag_status = 0
last_flag_status = 0
imei = "088298203828"
lastupdate_jam = ""
url = "https://posduga.sysable.io/api/sendjsondata"
url1 = "https://posduga.sysable.io/api/api-device-by-imei/088298203828"
url2 = "https://posduga.sysable.io/api/sendjsondata-multiple"
jadwal_pengiriman = ""
current_time = ""
date = ""
waktu_pengiriman = ""
status_response = 0


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


last_ketinggian_air = 0
ketinggian_air_fix = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)


def check_ping():
    hostname = "192.168.1.64"
    response = os.system("ping -c 1 " + hostname) #cek cctv
    # and then check the response...
    print("check ping : " + str(response))
    if response == 0 or response == 512 :
        pingstatus = "Kamera Dapat Tersambung"
    else:
        pingstatus = "Kamera error"

    return response

def check_url(hostname):
    response = os.system("ping -c 1 " + hostname) #cek_koneksi_internet
    print("response url :" + str(response))
    if response == 0 or response == 512:
        pingstatus = "Terkoneksi Ke Internet"
        #print("Terkoneksi ke Internet")
    else:
        pingstatus = "Internet Error"
        #print("Trying to Route to Dns Server")
        
        #time.sleep(10)
    
        response = os.system("ping -c 1 " + hostname)
        #print(response)
    return response

def compress_img(nama_file): #compress image
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
          
          if ((int(self._hp/58) != 0) and (int(self._hp/58)<tinggi_sensor)): #filter jika data sensor = 0 atau lebih tinggi dari ketinggian sensor
              ketinggian_air = int(tinggi_sensor - self._hp/58)
          else:
              ketinggian_air = 10000 #jika nilai sensor = 0 atau sensor > ketinggian air maka nilai default 10000

            
   def cancel(self):
      self._cb.cancel()
      
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file: #Untuk memproses data CCTV
        binaryData = file.read()
    return binaryData

def kirim_data(data,img, waktu, tanggal):
    global jadwal_pengiriman, status_response
    if (check_ping() == 0):
        img = "data:image/png;base64," + str(img) 
    else :
        img = " " 
    #data=json.dumps
    waktu = "" + str(waktu) 
    tanggal = "" + str(tanggal)
    print(waktu, tanggal)
    data_tmp = data
    data_fix = {"foto_cam":img,"ketinggian_air":data,"imei":imei, "waktu":waktu, "tanggal":tanggal }
    #print("tes" ,data_fix)
    try:
        r = requests.post(url, data=json.dumps(data_fix), headers=headers)
            
        print(r)
        data = r.__dict__['_content'] #pengambilan data jadwal selanjutnya
        print(data)
        data = json.loads(data)
        jadwal_pengiriman = str(data['next_schedule_sentdata'])
        print(jadwal_pengiriman)
        #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)] #pengambilan data next_schedulu di dict jadwal pengiriman
        status = str(data['status']) 
        print(data) 
        print("Jadwal Pengiriman Selanjutnya", jadwal_pengiriman) 
        r.close()
        if (status == "500"):
            status_response = 1
            #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)]
            print("Response 500")
            #kirim_data_full() #jika data kekirim, looping kirim data

        else :
            status_response = 0
            with open('/var/tmp/testing.log', 'a') as fp:
                img = "data:image/png;base64," #simpan data payload
                data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                print(data, 'done', file=fp) #simpan response pengiriman 
                print(data_fix, 'done', file=fp)
                #time.sleep(2)
        return jadwal_pengiriman

    except requests.exceptions.ConnectionError:
        print(r)
        #get_data_durasi()
    
    
def kirim_data_local_server(data_fix):
    
    try:
        r = requests.post(url2, data=json.dumps(data_fix), headers=headers)
        data = r.__dict__['_content'] #pengambilan data jadwal selanjutnya
        data = json.loads(data)
        status = str(data['status']) 
        print(status) 
        r.close()
        print("Response Kirim data Lokal : ", r)



    except requests.exceptions.ConnectionError:
        print("Gagal mengirimkan Data lokal ke server")
    
    with open('/var/tmp/testing.log', 'a') as fp:
        print('Kirim ulang data local', file=fp) #simpan response pengiriman 
        print(data, 'done', file=fp) #simpan response pengiriman 
        #time.sleep(2)
    
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
        #jadwal_pengiriman = data['last_update'] #Pengambilan jadwal berikutnya ketika booting script
        print("jadwal_pengiriman",jadwal_pengiriman)
        cek_siaga_init()
        kirim_data_full()
    except requests.exceptions.ConnectionError:
        
        print(r)

def ubah_data_local(x) :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    curs.execute("update data set status = 0 where id = %s",(x))
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute("")
    db.commit()
    print("ubah data", db)


def cek_data_local() :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute("SELECT * FROM data where status = 1")
    db.commit()
    print(db)
    data_dict = {}
    print("ubah data", db)
    temp_data_local = curs.fetchall()

    for x in temp_data_local:
        data_fix = {"foto_cam":x[2],"ketinggian_air":x[1],"imei":imei, "waktu":x[3], "tanggal":x[4] }
        kirim_data_local_server(data_fix)
        ubah_data_local(x(0))
    

def ambil_data_local_terakhir() :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute("SELECT * FROM data ORDER BY id DESC LIMIT 0, 1")
    db.commit()
    print(db)
    data_dict = {}
    print("Ambil Data Terakhir", db)
    temp_data_local = curs.fetchone()
    return temp_data_local[6]

def kirim_data_full():
   
    global  current_time, date, status, waktu_pengiriman
    print("Ketinggian_air_fix",ketinggian_air_fix)
    print("flag_status", flag_status)
    status = 0
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    crt_time = dt.datetime.now()
    date = dt.datetime.now().date()
    if flag_status == 0 :
       tmp_current_time = crt_time + timedelta(hours = 6) 
       waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))

    hostname = "posduga.sysable.io"
    

    print("Booting Camera and Modem 4G")
    if (check_ping() == 0):
        #time.sleep(2)
        cam = Client('http://192.168.1.64', 'admin', 't4ng3r4ng')
        print("starting picture capture")
        vid = cam.Streaming.channels[102].picture(method ='get', type = 'opaque_data')
        bytes = b''
        #path = "r'C:\Users\Myname\Dropbox\Foldes\image-' + date_string + '.png'"
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
    
    
    #path = '/home/pi/img_cctv/%s' , (current_time)
    
    #insert.kirim_data_local(ketinggian_air_fix, path)
    
    hostname = "posduga.sysable.io"
    print("cek url db local", check_url(hostname))
    
    if(check_url(hostname) == 512  ):
      if(check_ping()) == 0 :
          buffer_img = compress_img('img.png')
          #print("waktu :" + converter_json(current_time))

          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          #print("Response :" + response)
      else :
          buffer_img = " "
          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          print(response)
      #print("Full response" , response.__dict__)
      jadwal_pengiriman = response
      status1 = 0
    
    elif(check_url(hostname) == 0) :
        if(check_ping()) == 0 :
            buffer_img = compress_img('img.png')
            #print("waktu :" + converter_json(current_time))
          #print("Response :" + response)
        else :
          buffer_img = " "
        status1  = 1
        if flag_status == 0 :
            jadwal_pengiriman = waktu_pengiriman
        
        else :
            jadwal_pengiriman = waktu_pengiriman
        '''with open('/var/tmp/error.log', 'a') as fp:
            current_time = time.strftime("%H:%M:%S", t)
            date = datetime.datetime.now().date()
            print(date,current_time,"No Internet", file=fp)
        time.sleep(10)
        kirim_data_full()
        '''
    
    insert.kirim_data_local(date,current_time , ketinggian_air_fix, buffer_img,status1,waktu_pengiriman)

    if(check_url(hostname) == 0 or check_url(hostname) == 512):
        cek_data_local()

def cek_siaga_init():
     global waktu_pengiriman,flag_status
     t = time.localtime()
     current_time = time.strftime("%H:%M:%S", t)
     crt_time = dt.datetime.now()
     date = dt.datetime.now().date()

     if(int(ketinggian_air_fix) > siaga1): #pengecekan status berdasarkan ketinggian
         flag_status = 1
         set_millis = lvl_siaga1
         status =  "siaga1"
         tmp_current_time = crt_time + timedelta(minutes = 30)
         waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
     elif(int(ketinggian_air_fix) > siaga2):
         flag_status = 2
         set_millis = lvl_siaga2
         status =  "siaga2"
         tmp_current_time = crt_time + timedelta(hours = 1)
         waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
            
     elif(int(ketinggian_air_fix) > siaga3):
         flag_status = 3
         set_millis = lvl_siaga3
         status =  "siaga3"
         tmp_current_time = crt_time + timedelta(hours = 3)
         waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
         
     else:
         flag_status = 4
         set_millis = lvl_siaga4
         status =  "siaga4"
         print("Status : ", status)
         print("flag_status: ", flag_status)
         tmp_current_time = crt_time + timedelta(hours = 6)
         waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
    

def main():
   global set_millis,status, ketinggian_air, ketinggian_air_fix, last_ketinggian_air, tinggi_sensor, flag_status, last_flag_status, last_kalibrasi, current_time, date, waktu_pengiriman
   pwm_millis = round(int(time.time() * 1000))
   print("Initiate Kalibrasi Sensor ......")
   flag_kirim = 0
   flag_data_kirim = 0
   pi = pigpio.pi()
   time.sleep(5)
   for i in range(10):
       p1 = PWM_read(pi, 12 )
       time.sleep(1)
       if (i == 0):
           last_kalibrasi = ketinggian_air #kalibrasi ketika nilai sensor tidak stabil
           last_ketinggian_air = ketinggian_air
           ketinggian_air_fix =ketinggian_air
       if ((ketinggian_air < last_kalibrasi) and (last_kalibrasi != 0)): #mencari nilai paling kecil dari 10 data kalibrasi
           last_ketinggian_air = ketinggian_air #last ketinggian air digunakan untuk variabel filter
           last_kalibrasi = ketinggian_air 
           ketinggian_air_fix = ketinggian_air #ketinggian air fix digunakan sebagai variabel fix sensor
       print(ketinggian_air)  
   print("Hasil Kalibrasi Ketinggian sensor", ketinggian_air_fix)
   
   if (check_url(url1) == 0 or check_url(url1) == 512) :
       print("Update Data")
       get_data_durasi() #cek jadwal pengiriman ketika booting

   while True :
       current_millis = round(int(time.time() * 1000))
       t = time.localtime()
       current_time = time.strftime("%H:%M:%S", t)
       crt_time = dt.datetime.now()
       date = dt.datetime.now().date()
       


       if (current_millis - pwm_millis) > 10000 : #setiap 10 detik baca data sensor untuk melakukan filtering
          print(jadwal_pengiriman)
          p1 = PWM_read(pi, 12)
          time.sleep(1)
          print("Current Time : " + current_time)

          #print("Real Ketinggian_air :", int(ketinggian_air))
          #filter noise sensor

          if(abs(ketinggian_air - last_ketinggian_air)>40 and last_ketinggian_air != 0 and ketinggian_air != 0):
              ketinggian_air_fix = last_ketinggian_air #filter jika ada data noise yang beda lebih dari 40 dari last_ketinggian_air
              print("filter noise") #Jika iya. maka akan dilakukan filter menggunakan data sebelumnya
          else :
              ketinggian_air_fix = ketinggian_air #update biasa ketinggian air
              last_ketinggian_air = ketinggian_air #update last_ketinggian_air untuk filter selanjutnya
          pwm_millis = current_millis
             
          print("Ketinggian_air :", ketinggian_air_fix)
          #print("Last_ketinggian:",int(last_ketinggian_air))

          p1.cancel()
          
          if(int(ketinggian_air_fix) > siaga1): #pengecekan status berdasarkan ketinggian
              flag_status = 1
              set_millis = lvl_siaga1
              status =  "siaga1"
              tmp_current_time = crt_time + timedelta(minutes = 30)
              waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))

          elif(int(ketinggian_air_fix) > siaga2):
              flag_status = 2
              set_millis = lvl_siaga2
              status =  "siaga2"
              tmp_current_time = crt_time + timedelta(hours = 1)
              waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
            
          elif(int(ketinggian_air_fix) > siaga3):
              flag_status = 3
              set_millis = lvl_siaga3
              status =  "siaga3"
              tmp_current_time = crt_time + timedelta(hours = 3)
              waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
          else:
              flag_status = 4
              set_millis = lvl_siaga4
              status =  "siaga4"
              print("Status : ", status)
              print("flag_status: ", flag_status)
              tmp_current_time = crt_time + timedelta(hours = 6)
              waktu_pengiriman = str(format(tmp_current_time, '%H:%M:%S'))
    
          if (flag_status != last_flag_status and last_ketinggian_air != 0 and last_flag_status !=0 and flag_status < last_flag_status):
              inc = inc + 1 
              if (inc > 4):
                  with open('/var/tmp/testing.log', 'a') as fp:
                      print("Status :",flag_status, ' Status Changed', file=fp)
                      #time.sleep(1)
                      print("perubahan status")
                      kirim_data_full()
                      last_flag_status = flag_status    
              

              
          else :
              inc = 0 
              last_flag_status = flag_status  

          with open('/var/tmp/data_sensor.log', 'a') as fp:
              print(ketinggian_air_fix, last_ketinggian_air, ketinggian_air, current_time, date,flag_status, 'done', file=fp) #simpan data sensor
              time.sleep(1)
        #Cek apakah ada update jadwal pengiriman
        #Jika tidak ada maka ambil dari status siaga
       
       date1 = datetime.now().date()
       #print("date1", date1)
       if (status_response == 0):
           tmp_jadwal_pengiriman = str(date1) + " " + jadwal_pengiriman
           tmp_jadwal_pengiriman = datetime.strptime(tmp_jadwal_pengiriman, '%Y-%m-%d %H:%M:%S')
       else :
           tmp_jadwal_pengiriman = datetime.strptime(jadwal_pengiriman, '%Y-%m-%d %H:%M:%S')
       #print("tmp_string" , tmp_jadwal_pengiriman)
       tmp_string_realtime = str(date1) + " " + str(current_time)
       tmp_real_time = datetime.strptime(tmp_string_realtime, '%Y-%m-%d %H:%M:%S')
       #print("tmp_real_time" , tmp_real_time)
       tmp_currt_time = datetime.now()
       if (tmp_real_time > tmp_jadwal_pengiriman):
           elapsed = tmp_real_time - tmp_jadwal_pengiriman
           flag_data_kirim = 1
           #print("elapsed :",elapsed)
       else :
           elapsed = timedelta(minutes=5)
           
       #print("elapsed :",elapsed)
       if (str(current_time) == jadwal_pengiriman or (elapsed < timedelta(minutes=3) and flag_data_kirim == 1 )):
           print("elapsed :",elapsed)
           flag_data_kirim = 0
           if (flag_kirim == 0):
               flag_kirim = 1
               #waktu_pengiriman = jadwal_pengiriman
               kirim_data_full()
               
           else :
               print("data sudah dkirim pada jadwal pengiriman :", jadwal_pengiriman )
       else :
           flag_kirim = 0
         


if __name__ == '__main__':
   main()


   
