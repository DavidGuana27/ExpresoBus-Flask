from BaseDatos import mysqlConnect
#*------------- LISTAR VIAJES
def consultarViaje():
    conexion = mysqlConnect()
    boletos = []
    with conexion.cursor() as cursor:
        sql = "SELECT o.numero, o.fecha, o.silla, o.placa, o.tarifa, o.ciudad AS origen, d.ciudad AS destino FROM (SELECT v.numero, c.tipo AS ciudad, v.fecha, v.silla, v.placa, v.tarifa FROM viaje AS v INNER JOIN ciudad AS c ON v.id_ciudad_origen = c.id) o INNER JOIN (SELECT v.numero, c.tipo AS ciudad FROM viaje AS v INNER JOIN ciudad AS c ON v.id_ciudad_destino = c.id) d ON o.numero = d.numero"
        cursor.execute(sql)
        boletos = cursor.fetchall()
        conexion.close()
    return boletos

#*-------------- AGREGAR VIAJE
def agregarViaje(numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO `viaje` (`numero`, `fecha`, `silla`, `placa`, `tarifa`, `id_ciudad_origen`, `id_ciudad_destino` ) VALUES(%s, %s, %s, %s, %s, %s, %s)',
        (numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino))
        conexion.commit()
        conexion.close()

#?--------------- CONSULTAR VIAJE POR NUMERO
def consultarViajeNum(numero):
    conexion = mysqlConnect()
    viaje = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM viaje WHERE numero = %s"
        cursor.execute(sql, (numero))
        viaje = cursor.fetchone()
        conexion.close()
    return viaje

#?--------------- CONSULTAR CIUDAD POR ID
def consultarCiudadId():
    conexion = mysqlConnect()
    ciudad = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM ciudad"
        cursor.execute(sql)
        ciudad = cursor.fetchall()
        conexion.close()
    return ciudad

#*---------------- ACTUALIZAR VIAJE
def actualizarViaje(numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('UPDATE viaje SET numero = %s, fecha = %s, silla = %s, placa = %s, tarifa = %s, id_ciudad_origen = %s, id_ciudad_destino = %s WHERE numero = %s',
            (numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino, numero))
        conexion.commit()
        conexion.close()

#*---------------- ELIMINAR VIAJE
def eliminarViaje(numero):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('DELETE FROM viaje WHERE numero = %s', (numero))
        conexion.commit()
        conexion.close()