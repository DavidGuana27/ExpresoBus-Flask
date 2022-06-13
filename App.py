from flask import Flask, redirect, render_template, request
import controladorPersona, controladorBoleto, controladorViaje

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/paga')
def paga():
    return render_template("paga.html")

# ? RUTAS CRUD PERSONAS
@app.route('/listaPersona')
def listaPersona():
    persona = controladorPersona.consultarPersona()
    return render_template("persona.html", personas = persona)

@app.route('/agregarPersona')
def agregaPersona():
    return render_template("crudPersona/agregar.html")

@app.route('/frmAgregarPersona', methods=['POST'])
def agregarPersona():
    if request.method == 'POST':
        tipo_doc = request.form['select_doc']
        identificacion = request.form['identificacion']
        txtNombre = request.form['nombre']
        txtApellido = request.form['apellido']
        txtEmail = request.form['email']
        txtTelefono = request.form['telefono']
        tipo_pers = request.form['select_per']
        
        controladorPersona.agregarPersona(tipo_doc, identificacion, txtNombre, txtApellido, txtEmail, txtTelefono, tipo_pers)
    return redirect("/listaPersona")

@app.route('/editarPersona/<int:identificacion>', methods=['GET', 'POST'])
def editarPersona(identificacion):
    if request.method == 'POST':
        tipo_doc = request.form['select_doc']
        txtNombre = request.form['nombre']
        txtApellido = request.form['apellido']
        txtEmail = request.form['email']
        txtTelefono = request.form['telefono']
        tipo_pers = request.form['select_per']

        controladorPersona.actualizarPersona(tipo_doc, txtNombre, txtApellido, txtEmail, txtTelefono, tipo_pers, identificacion)
        return redirect("/listaPersona")
    elif request.method == 'GET':
        tipo_persona = controladorPersona.consultarPersonaTipoPer()
        tipo_documento = controladorPersona.consultarPersonaTipoDoc()
        persona = controladorPersona.consultarPersonaId(identificacion)
        return render_template("crudPersona/editar.html", personas = persona, tipo_persona = tipo_persona, tipo_documento = tipo_documento)
        
@app.route('/eliminarPersona/<int:identificacion>')
def eliminarPersona(identificacion):
    controladorPersona.eliminarPersona(identificacion)
    return redirect('/listaPersona')

# ? RUTAS CRUD BOLETOS
@app.route('/listaBoleto')
def listaBoletos():
    boleto = controladorBoleto.consultarBoleto()
    return render_template("boleto.html", boletos = boleto)
@app.route('/agregarBoleto')

def agregaBoleto():
    pasajero = controladorBoleto.consultarPasajeroId()
    conductor = controladorBoleto.consultarConductorId()
    viaje = controladorBoleto.consultarViajeId()
    print(pasajero)
    return render_template("crudBoleto/agregar.html", pasajero = pasajero, conductor = conductor, viaje = viaje)

@app.route('/frmAgregarBoleto',  methods=['POST'])
def agregarBoleto():
    if request.method == 'POST':
        id = request.form['id']
        select_pasajero = request.form['select_pasajero']
        select_conductor = request.form['select_conductor']
        select_viaje = request.form['select_viaje']
        controladorBoleto.agregarBoleto(id, select_pasajero, select_conductor, select_viaje)
    return redirect("/listaBoleto")

@app.route('/eliminarBoleto/<int:id>')
def eliminarBoleto(id):
    controladorBoleto.eliminarBoleto(id)
    return redirect('/listaBoleto')

# ? RUTAS CRUD VIAJES
@app.route('/listaViaje')
def listaViaje():
    viaje = controladorViaje.consultarViaje()
    return render_template("viaje.html", viajes = viaje)

@app.route('/agregarViaje')
def agregaViaje():
    return render_template("crudViaje/agregar.html")

@app.route('/frmAgregarViaje', methods=['POST'])
def agregarViaje():
    if request.method == 'POST':
        numero = request.form['numero']
        fecha = request.form['fecha']
        silla = request.form['silla']
        placa = request.form['placa']
        tarifa = request.form['tarifa']
        select_ciudad_origen = request.form['select_ciudad_origen']
        select_ciudad_destino = request.form['select_ciudad_destino']
        controladorViaje.agregarViaje(numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino)
    return redirect("/listaViaje")

@app.route('/editarViaje/<int:numero>', methods=['GET', 'POST'])
def editarViaje(numero):
    if request.method == 'POST':
        numero = request.form['numero']
        fecha = request.form['fecha']
        silla = request.form['silla']
        placa = request.form['placa']
        tarifa = request.form['tarifa']
        select_ciudad_origen = request.form['select_ciudad_origen']
        select_ciudad_destino = request.form['select_ciudad_destino']
        
        controladorViaje.actualizarViaje(numero, fecha, silla, placa, tarifa, select_ciudad_origen, select_ciudad_destino)
        return redirect("/listaViaje")
    elif request.method == 'GET':
        ciudad = controladorViaje.consultarCiudadId()
        viaje = controladorViaje.consultarViajeNum(numero)
        return render_template("crudViaje/editar.html", viajes = viaje, ciudad = ciudad)

@app.route('/eliminarViaje/<int:numero>')
def eliminarViaje(numero):
    controladorViaje.eliminarViaje(numero)
    return redirect('/listaViaje')

if __name__ == '__main__':
    app.run(debug=True)