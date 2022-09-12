from dataclasses import dataclass
from os import curdir
import pymysql
db=pymysql.connect(user='root',password='',host='localhost',database='shop')
def addrow(sql):
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
def allrow(sql):
    cur=db.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data
def onerow(sql):
    cur=db.cursor()
    cur.execute(sql)
    data=cur.fetchone()
    return data
