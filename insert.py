#!/usr/bin/env python

import datetime
import MySQLdb
import time


db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_lokal")
curs=db.cursor()

# note that I'm using triplle quotes for formatting purposes
# you can use one set of double quotes if you put the whole string on one line
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
       
date = datetime.datetime.now().date()
waktu = current_time + str(date)
curs.execute ("""INSERT INTO data
            values(130, '/home/pi/img.png', waktu)""")

db.commit()
print ("Data committed")
