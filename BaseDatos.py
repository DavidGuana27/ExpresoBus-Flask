import pymysql

def mysqlConnect():
    conexion = pymysql.Connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'expresobus')
    return conexion

