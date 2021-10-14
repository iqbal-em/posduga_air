#!/usr/bin/env python

import datetime
import MySQLdb
import time


def kirim_data_local(tanggal, waktu, ketinggian_air, img, status, next_jadwal,imei) :
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor() 
    #kirim data lokal

    #
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
       
    date = datetime.datetime.now().date()
    temp_waktu = str(date) +  str(current_time)
    img = "data:image/png;base64," + str(img)
    
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute ("""INSERT INTO data(ketinggian_air,data_cam,waktu,tanggal,status,next_jadwal,imei)
            values(%s, %s,%s,%s,%s,%s,&s)""",(ketinggian_air, img, waktu, tanggal, status, next_jadwal,imei))

    db.commit()
    print ("kirim data local",db)
