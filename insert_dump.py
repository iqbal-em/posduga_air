#!/usr/bin/env python

import datetime
import MySQLdb
import time


def kirim_data_local() :
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
       
    date = datetime.datetime.now().date()
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor() 
    #kirim data lokal

    #
    ketinggian_air = 200
    tanggal =
    temp_waktu = str(date) +  str(current_time)
    img = "data:image/png;base64," 
    status = 0
    next_jadwal = 
    
    #tmp_img = 'home/pi/posduga_air/img/%s',temp_waktu
    curs.execute ("""INSERT INTO data(ketinggian_air,data_cam,waktu,tanggal,status,next_jadwal)
            values(%s, %s,%s,%s,%s,%s)""",(ketinggian_air, img, waktu, tanggal, status, next_jadwal))

    db.commit()
    print ("kirim data local",db)



kirim_data_local()