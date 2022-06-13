from BaseDatos import mysqlConnect
#*------------- LISTAR BOLETO
def consultarBoleto():
    conexion = mysqlConnect()
    boletos = []
    with conexion.cursor() as cursor:
        #TODO Consulta BD Expresobus
        sql = "SELECT a.id, a.pasajero, b.conductor, b.viaje, a.silla, a.placa, a.tarifa, a.origen, b.destino FROM (SELECT b.id, v.silla, v.placa, v.tarifa, c.tipo AS origen, CONCAT(p.nombre, ' ', p.apellido) AS pasajero FROM persona AS p INNER JOIN boleto AS b ON p.identificacion = b.ident_pasajero INNER JOIN viaje AS v ON b.num_viaje = v.numero INNER JOIN ciudad AS c ON v.id_ciudad_origen = c.id) a INNER JOIN (SELECT b.id, c.tipo AS destino, v.fecha AS viaje, CONCAT(p.nombre, ' ',p.apellido) AS conductor FROM persona AS p INNER JOIN boleto AS b ON p.identificacion = b.ident_conductor INNER JOIN viaje AS v ON b.num_viaje = v.numero INNER JOIN ciudad AS c ON v.id_ciudad_destino = c.id ) b ON a.id = b.id"
        sql2 = ""
        cursor.execute(sql)
        boletos = cursor.fetchall()
        conexion.close()
    return boletos

#*-------------- AGREGAR BOLETO
def agregarBoleto(id, select_pasajero, select_conductor, select_viaje):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO `boleto` (`id`, `ident_pasajero`, `ident_conductor`, `num_viaje`) VALUES(%s, %s, %s, %s)',
        (id, select_pasajero, select_conductor, select_viaje))
        conexion.commit()
        conexion.close()

#?--------------- CONSULTAR PASAJERO POR IDENTIFICACION
def consultarPasajeroId():
    conexion = mysqlConnect()
    pasajaro = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM persona WHERE id_tipo_per = 1"
        cursor.execute(sql)
        pasajaro = cursor.fetchall()
        print("prueba de conexion pasajero")
        conexion.close()
    return pasajaro

#?--------------- CONSULTAR CONDUCTOR POR IDENTIFICACION
def consultarConductorId():
    conexion = mysqlConnect()
    conductor = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM persona WHERE id_tipo_per = 2"
        cursor.execute(sql)
        conductor = cursor.fetchall()
        print("prueba de conexion conductor")
        conexion.close()
    return conductor

#?--------------- CONSULTAR VIAJE POR ID
def consultarViajeId():
    conexion = mysqlConnect()
    viaje = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM viaje"
        cursor.execute(sql)
        viaje = cursor.fetchall()
        print("prueba de conexion viaje")
        conexion.close()
    return viaje

#*--------------- CONSULTAR BOLETO POR ID
def consultarBoletoId(id):
    conexion = mysqlConnect()
    boleto = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM boleto WHERE id = %s"
        cursor.execute(sql, (id))
        boleto = cursor.fetchone()
        conexion.close()
    return boleto

# #*---------------- ACTUALIZAR BOLETO
# def actualizarPersona(identificacion,txtNombre, txtApellido, txtEmail, txtTelefono):
#     conexion = mysqlConnect()
#     with conexion.cursor() as cursor:
#         cursor.execute('UPDATE persona SET identificacion = %s, nombre = %s, apellido = %s, email = %s, telefono = %s WHERE identificacion = %s',
#             (identificacion, txtNombre, txtApellido, txtEmail, txtTelefono, identificacion))
#         conexion.commit()
#         conexion.close()

#*---------------- ELIMINAR BOLETO
def eliminarBoleto(id):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('DELETE FROM boleto WHERE id = %s', (id))
        conexion.commit()
        conexion.close()