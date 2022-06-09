from BaseDatos import mysqlConnect
#*------------- LISTAR PERSONA
def consultarPersona():
    conexion = mysqlConnect()
    personas = []
    with conexion.cursor() as cursor:
        sql = "SELECT identificacion, nombre, apellido, email, telefono, tp.tipo AS id_tipo_per, td.tipo AS id_tipo_doc FROM persona AS p, tipo_documento AS td, tipo_persona AS tp WHERE p.id_tipo_per = tp.id AND p.id_tipo_doc = td.id"
        cursor.execute(sql)
        personas = cursor.fetchall()
        conexion.close()
    return personas
#*--------------- CONSULTAR TIPO PERSONA POR ID
def consultarPersonaTipoPer():
    conexion = mysqlConnect()
    personas = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM tipo_persona"
        cursor.execute(sql)
        personas = cursor.fetchall()
        conexion.close()
    return personas
#*--------------- CONSULTAR TIPO DOCUMENTO POR ID
def consultarPersonaTipoDoc():
    conexion = mysqlConnect()
    personas = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM tipo_documento"
        cursor.execute(sql)
        personas = cursor.fetchall()
        conexion.close()
    return personas

#*-------------- AGREGAR PERSONA
def agregarPersona(tipo_doc, identificacion, txtNombre, txtApellido, txtEmail, txtTelefono, tipo_per):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO persona (identificacion, nombre, apellido, email, telefono, id_tipo_per, id_tipo_doc) VALUES(%s, %s, %s, %s, %s, %s, %s)',
        (identificacion, txtNombre, txtApellido, txtEmail, txtTelefono, tipo_per, tipo_doc))
        conexion.commit()
        conexion.close()

#?--------------- CONSULTAR PERSONA POR IDENTIFICACION
def consultarPersonaId(identificacion):
    conexion = mysqlConnect()
    persona = None
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM persona WHERE identificacion = %s"
        cursor.execute(sql, (identificacion))
        persona = cursor.fetchone()
        conexion.close()
    return persona

#?--------------- CONSULTAR TIPO PERSONA POR ID
def consultarPersonaTipoPer():
    conexion = mysqlConnect()
    personas = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM tipo_persona"
        cursor.execute(sql)
        personas = cursor.fetchall()
        conexion.close()
    return personas

#?--------------- CONSULTAR TIPO DOCUMENTO POR ID
def consultarPersonaTipoDoc():
    conexion = mysqlConnect()
    personas = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM tipo_documento"
        cursor.execute(sql)
        personas = cursor.fetchall()
        conexion.close()
    return personas

#*---------------- ACTUALIZAR PERSONA
def actualizarPersona( tipo_doc, txtNombre, txtApellido, txtEmail, txtTelefono, tipo_pers, identificacion):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('UPDATE persona SET nombre = %s, apellido = %s, email = %s, telefono = %s, id_tipo_per = %s, id_tipo_doc = %s WHERE identificacion = %s',(txtNombre, txtApellido, txtEmail, txtTelefono, tipo_pers, tipo_doc, identificacion))
        conexion.commit()
        conexion.close()

#*---------------- ELIMINAR PERSONA
def eliminarPersona(identificacion):
    conexion = mysqlConnect()
    with conexion.cursor() as cursor:
        cursor.execute('DELETE FROM persona WHERE identificacion = %s', (identificacion))
        conexion.commit()
        conexion.close()