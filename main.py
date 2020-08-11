import sqlite3 as sql
import argparse
import datetime
import time


parser = argparse.ArgumentParser(description='Select an app choice')
parser.add_argument('choice', default=1, type=int, help="App number")
parser.add_argument('FIO', nargs='?', default=None, type=str, help="Name")
parser.add_argument('birthday', nargs='?', default=None, type=lambda d: datetime.datetime.strptime(d, '%d.%m.%Y'), help="Birthday")
parser.add_argument('sex', nargs='?', default=None, type=str, help="Sex")
args = parser.parse_args()

choice = args.choice
con = sql.connect('test.db')
with con:
    cur = con.cursor()

    if choice == 1:
        cur.execute("CREATE TABLE IF NOT EXISTS `test` (`FIO` STRING, `birthday` DATE, `sex` STRING)")
    elif choice == 2:
        fio = args.FIO
        birthday = args.birthday
        sex = args.sex
        cur.execute(f"INSERT INTO `test` VALUES ('{fio}', '{birthday}', '{sex}')")
    elif choice == 3:
        cur.execute("SELECT DISTINCT FIO, birthday, sex FROM `test`")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif choice == 4:
        pass
    elif choice == 5:
        timing = time.time()
        cur.execute("SELECT FIO, sex FROM `test` WHERE FIO LIKE 'F%' AND sex='M'")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print(time.time() - timing)
    elif choice == 5:
        pass
    else:
        pass

    con.commit()
    cur.close()
