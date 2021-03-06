

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
siaga2 = 100
siaga3 = 70

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
dict = {}
status1 = 1


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
    global jadwal_pengiriman, status_response, status1
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
    crt_time = dt.datetime.now()
    #print("tes" ,data_fix)
    try:
        r = requests.post(url, data=json.dumps(data_fix), headers=headers)
            
        print(r)
        data = r.__dict__['_content'] #pengambilan data jadwal selanjutnya
        print(data)
        if str(r)[0:16] == "<Response [504]>" :
            status1 = 1
            with open('/var/tmp/testing.log', 'a') as fp:
                print(waktu, '504 Gateway Timeout', data, file=fp) #simpan response pengiriman 
            
                    #time.sleep(2)
        elif data : 
            data = json.loads(data)
       
            #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)] #pengambilan data next_schedulu di dict jadwal pengiriman
            status = str(data['status']) 
            print(data) 
            print("Jadwal Pengiriman Selanjutnya", jadwal_pengiriman) 
            r.close()
            if (status == "200"):
                status_response = 0
                status1 = 0
                #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)]
                #print("Response 500")
                #kirim_data_full() #jika data kekirim, looping kirim data
                with open('/var/tmp/testing.log', 'a') as fp:
                    img = "data:image/png;base64," #simpan data payload
                    data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                    print(waktu, 'Data Tersimpan', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)

            else :
                status_data = str(data['status_data'])
                if (status_data == "200"):
                    status1 = 0
                    with open('/var/tmp/testing.log', 'a') as fp:
                        img = "data:image/png;base64," #simpan data payload
                        data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                        print(waktu, 'Data Terkirim Tapi tidak tersimpan di Web', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
                else : 
                    status1 = 1
                    with open('/var/tmp/testing.log', 'a') as fp:
                        img = "data:image/png;base64," #simpan data payload
                        data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                        print(waktu, 'Data Tidak Terkirim dikarenakan status_data tidak 200', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
                status_response = 1
        
                
                #time.sleep(2)
        else :
            status1 = 1
            with open('/var/tmp/testing.log', 'a') as fp:
                img = "data:image/png;base64," #simpan data payload
                data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                print(waktu, 'Data Terkirim Tapi Response status data tidak ada', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
        return jadwal_pengiriman

    except requests.exceptions.ConnectionError:
        print(r)
        r.close()
        #get_data_durasi()
    
    except requests.exceptions.ReadTimeout:
        status1 = 1
        r.close()
        with open('/var/tmp/testing.log', 'a') as fp:
            img = "data:image/png;base64," #simpan data payload
            data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
            print(waktu,'Timeout', file=fp)
    
    except requests.exceptions.HTTPError as err:
        with open('/var/tmp/testing.log', 'a') as fp:
            print(crt_time,'Response error', file=fp)
            r.close()


def get_data_durasi():
    global siaga1, siaga2, siaga3, siaga4, lvl_siaga1, lvl_siaga2, lvl_siaga3, lvl_siaga4, jadwal_pengiriman,tinggi_sensor
    try : 
        r =  requests.get(url=url1)
        data = r.json()
        tinggi_sensor = int(data['data'][0]['ketinggian_sensor'])
        print(tinggi_sensor)

        '''
        siaga1 = data['data'][0]['siaga']['min_siaga_1']
        siaga2 = data['data'][0]['siaga']['min_siaga_2']
        siaga3 = data['data'][0]['siaga']['min_siaga_3']
        lvl_siaga1 = (data['data'][0]['siaga']['durasi_siaga_1'])*1000 
        lvl_siaga2 = (data['data'][0]['siaga']['durasi_siaga_2'])*1000
        lvl_siaga3 = (data['data'][0]['siaga']['durasi_siaga_3'])*1000
        lvl_siaga4 = (data['data'][0]['siaga']['durasi_siaga_4'])*1000
        siaga3 = data['data'][0]['siaga']['min_siaga_3']
        '''
        #jadwal_pengiriman = data['last_update'] #Pengambilan jadwal berikutnya ketika booting script
        #print("jadwal_pengiriman",jadwal_pengiriman)
        #cek_siaga_init()
        #kirim_data_full()
    except requests.exceptions.ConnectionError:
        
        print(r)

def kirim_data_local_server(data_fix):
    global status1
    try:
        r = requests.post(url2, data=json.dumps(data_fix), headers=headers)
        data = r.__dict__['_content'] #pengambilan data jadwal selanjutnya
        crt_time = dt.datetime.now()
        #print(data)
        if str(r)[0:16] == "<Response [504]>" :
            status1 = 0
            with open('/var/tmp/testing.log', 'a') as fp:
                print(crt_time, '504 Gateway Timeout', data, file=fp) #simpan response pengiriman 
            
                    #time.sleep(2)
        elif data : 
            data = json.loads(data)
       
            #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)] #pengambilan data next_schedulu di dict jadwal pengiriman
            status = str(data['status']) 
            print(data) 
            print("Jadwal Pengiriman Selanjutnya", jadwal_pengiriman) 
            
            
            if (status == "200"):
                status_response = 0
                status1 = 1
                #jadwal_pengiriman = jadwal_pengiriman[11:len(jadwal_pengiriman)]
                #print("Response 500")
                #kirim_data_full() #jika data kekirim, looping kirim data
                with open('/var/tmp/testing.log', 'a') as fp:
                    img = "data:image/png;base64," #simpan data payload
                    #data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                    print(crt_time, 'Data Lama Tersimpan', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)

            else :
                status_data = str(data['status_data'])
                if (status_data == "200"):
                    status1 = 0
                    with open('/var/tmp/testing.log', 'a') as fp:
                        img = "data:image/png;base64," #simpan data payload
                        #data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                        print(crt_time, 'Data Lama Terkirim Tapi tidak tersimpan di Web', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
                else : 
                    status1 = 1
                    with open('/var/tmp/testing.log', 'a') as fp:
                        img = "data:image/png;base64," #simpan data payload
                        #data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                        print(crt_time, 'Data Lama Tidak Terkirim dikarenakan status_data tidak 200', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
                status_response = 1
        
                
                #time.sleep(2)
        else :
            status1 = 1
            with open('/var/tmp/testing.log', 'a') as fp:
                img = "data:image/png;base64," #simpan data payload
                #data_fix = {"foto_cam":img,"ketinggian_air":data_tmp,"imei":imei, "waktu":waktu, "tanggal":tanggal }
                print(crt_time, 'Data Lama Terkirim Tapi Response status data tidak ada', data, file=fp) #simpan response pengiriman 
                    #time.sleep(2)
        r.close()
        return jadwal_pengiriman




    except requests.exceptions.ConnectionError:
        print("Gagal mengirimkan Data lokal ke server")
        r.close()
    
    except requests.exceptions.ReadTimeout:
        status1 = 1
        r.close()
        with open('/var/tmp/testing.log', 'a') as fp:
            print(crt_time,'Timeout', file=fp)
    
    except requests.exceptions.HTTPError as err:
        with open('/var/tmp/testing.log', 'a') as fp:
            print(crt_time,'Response error', file=fp)
            r.close()
    
    
    

def get_jadwal_pengiriman(device_id,status_siaga,count) :

    db = MySQLdb.connect("localhost", "root", "", "posduga_air")
    curs=db.cursor()

    query = """select * from jadwal_devices where device_id = %s and level = %s"""
    tmp_data = (device_id,status_siaga,)
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute (query,tmp_data)
    
    for x in temp_data_local:
        data_fix = {"foto_cam":x(2),"ketinggian_air":x(1),"imei":imei, "waktu":x(3), "tanggal":x(4) }
        kirim_data_local_server(data_fix)
        ubah_data_local(x(0))

    db.commit()
    print ("Data committed")
    temp_data_local = curs.fetchall()

    #temp_datalocal = temp_data_local[count][3]
    #minpos = delta.index(min(delta))
    
    return temp_data_local

def ubah_data_local(x) :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    tmp = (x,)
    sql = """update data set status = 0 where id = %s"""
    curs.execute(sql,tmp)
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    db.commit()
    print("ubah data", db)

def update_data_db_local(x1):
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    query = """SELECT id FROM data ORDER BY id DESC LIMIT 1"""
    curs.execute(query)
    db.commit()
    data_dict = {}
    temp_data_local = curs.fetchone()
    x = (x1,int(temp_data_local[0]))
    query = """UPDATE data SET status =%s where id = %s"""
    curs.execute(query,x)
    db.commit()
    
    print(temp_data_local[0])

#update_data_db_local(0)


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
        #print(data_fix)
        kirim_data_local_server(data_fix)
        ubah_data_local(x[0])

def ambil_data_local_terakhir() :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute("SELECT * FROM data ORDER BY id DESC LIMIT 0, 1")
    db.commit()
    #print(db)
    data_dict = {}
    #print("Ambil Data Terakhir", db)
    temp_data_local = curs.fetchone()
    #return temp_data_local[6]
    #print(temp_data_local[4])
    tmp = temp_data_local[4] + " " + temp_data_local[3]
    tmp_jadwal_pengiriman = datetime.strptime(tmp, '%Y-%m-%d %H:%M:%S')
    return tmp_jadwal_pengiriman

def ambil_data_jadwal(id1) :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    #kirim data lokal
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    x = (id1,)
    query = """SELECT level,waktu_pengiriman FROM jadwal_devices where device_id = %s order by level,waktu_pengiriman"""
    curs.execute(query,x)
    db.commit()
    print(db)
    data_dict = {}
    #print("ubah data", db)
    temp_data_local = curs.fetchall()
    #print(temp_data_local)
    date = dt.datetime.now().date()
    t = "00:00:00"
    tmp_string_realtime = str(date) + " " + t
    tmp_default_time = datetime.strptime(tmp_string_realtime, '%Y-%m-%d %H:%M:%S')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_hour = time.strftime("%H", t)
    current_minute = time.strftime("%M",t)
    tmplist_jadwal_pengiriman = []
    dict = {}
    key  = 1
    tmp_id = 1
    
    for x in temp_data_local:
        tmp_time = x[1] 
        #print(tmp_time)

        if (tmp_id == x[0]):
            tmp_jadwal_pengiriman = tmp_default_time + timedelta(seconds = tmp_time.total_seconds())
            #tmp_jadwal_pengiriman = datetime.strptime(tmp_jadwal_pengiriman, '%Y-%m-%d %H:%M:%S')
            #print(tmp_hour)
            tmplist_jadwal_pengiriman.append(tmp_jadwal_pengiriman)
        
        else :

            #tmplist_jadwal_pengiriman.append(tmp_default_time)
            dict[key] = tmplist_jadwal_pengiriman
            tmplist_jadwal_pengiriman = []
            tmp_jadwal_pengiriman = tmp_default_time + timedelta(seconds = tmp_time.total_seconds())
            tmplist_jadwal_pengiriman.append(tmp_jadwal_pengiriman)
            
        
            key = key + 1
            tmp_id = tmp_id + 1
        #print(tmp_jadwal_pengiriman.strftime("%H:%M:%S"))
    #print(dict)
    dict[key] = tmplist_jadwal_pengiriman
    return dict
    #return dict

    


def kirim_data_full():
   
    global  current_time, date, status, waktu_pengiriman, status1
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
    if(check_url(hostname) == 0 or check_url(hostname) == 512):
      if(check_ping()) == 0 :
          buffer_img = compress_img('img.png')
          #print("waktu :" + converter_json(current_time))
          insert.kirim_data_local(date,current_time , ketinggian_air_fix, buffer_img,status1,waktu_pengiriman,imei)
          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          update_data_db_local(status1)
          #print("Response :" + response)
      else :
          buffer_img = " "
          insert.kirim_data_local(date,current_time , ketinggian_air_fix, buffer_img,status1,waktu_pengiriman,imei)
          response = kirim_data(ketinggian_air_fix,buffer_img,current_time, date)
          update_data_db_local(status1)
          print(response)
      #print("Full response" , response.__dict__)
      #jadwal_pengiriman = response
    else :
        if(check_ping()) == 0 :
            buffer_img = compress_img('img.png')
            #print("waktu :" + converter_json(current_time))
          #print("Response :" + response)
        else :
          buffer_img = " "
        status1  = 1
        insert.kirim_data_local(date,current_time , ketinggian_air_fix, buffer_img,status1,waktu_pengiriman,imei)
        '''with open('/var/tmp/error.log', 'a') as fp:
            current_time = time.strftime("%H:%M:%S", t)
            date = datetime.datetime.now().date()
            print(date,current_time,"No Internet", file=fp)
        time.sleep(10)
        kirim_data_full()
        '''
    
   
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

def pengecekan_jadwal(dict,flag):
    
    date = dt.datetime.now().date()
    t = "00:00:00"
    crt_time = dt.datetime.now()
    tmp_string_realtime = str(date) + " " + t
    tmp_default_time = datetime.strptime(tmp_string_realtime, '%Y-%m-%d %H:%M:%S')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_hour = time.strftime("%H", t)
    current_minute = time.strftime("%M",t)
    col = 0
    #print(dict[flag])
    for x in dict[flag]:
        tmp_time = x
        tmp_time = tmp_time - tmp_default_time
        tmp_jadwal_pengiriman = tmp_default_time + timedelta(seconds = tmp_time.total_seconds())
        delta = crt_time - x
        if (delta < timedelta(minutes=1,seconds = 30)):
            return col
    
            break
        elif (int(tmp_jadwal_pengiriman.hour) > int(current_hour)):
                if(int(tmp_jadwal_pengiriman.minute) > int(current_minute)):
                   
                    return col
                    break
                else:  
                    
                    return col
                    break
        
        col = col + 1

def update_dict(dict):
    tmplist_jadwal_pengiriman = []
    for col in range(1,5):
        for x in dict[col] :
            x += timedelta(days=1)
            tmplist_jadwal_pengiriman.append(x)
        
        dict[col] = tmplist_jadwal_pengiriman
        tmplist_jadwal_pengiriman = []
    return dict

        
        
    

def main():
   cek_data_local()

if __name__ == '__main__':
   main()


   
