import MySQLdb

def delete_data_db_local_weekly():
    db = MySQLdb.connect("localhost", "admin", "t4ng3r4ng", "posduga_air")
    curs=db.cursor()
    query = """DELETE FROM data WHERE tanggal < ADDDATE(NOW(),-6)"""
    curs.execute(query)
    db.commit()
    tes = curs.fetchall()
    print(tes)

    

delete_data_db_local_weekly()