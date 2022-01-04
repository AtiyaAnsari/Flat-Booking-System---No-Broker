import pymysql
from model import Home


connection = ''
cursor = ''


def connect():
    global connection, cursor
    connection = pymysql.connect(
        host="localhost", user="root", password="", db="DPN")
    cursor = connection.cursor()


def disconnect():
    global connection, cursor
    cursor.close()
    connection.close


def addHome(Home):
    global connection, cursor
    connect()
    query = 'insert into Home(name,email,number,tower,bhk,types)values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(query, (Home.name,Home.email,Home.number,Home.tower,Home.bhk,Home.types))
    connection.commit()
    disconnect()


def getAllHome():
    global connection, cursor
    connect()
    query = 'select * from Home'
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect()
    return data


def getHomeById(bid):
    global connection, cursor
    connect()
    query = 'select * from Home where id=%s'
    cursor.execute(query, (bid))
    data = cursor.fetchone()
    disconnect()
    return data


def delHomeById(bid):
    global connection, cursor
    connect()
    query = 'delete from Home where id=%s'
    cursor.execute(query, (bid))
    connection.commit()
    disconnect()


def updateHomeById(Home):
    global connection, cursor
    connect()
    query = 'update Home set name=%s,email=%s,number=%s,tower=%s,bhk=%s,types=%s where id=%s'
    cursor.execute(query, (Home.name,Home.email,Home.number,Home.tower,Home.bhk,Home.types,Home.bid))
    connection.commit()
    disconnect()
