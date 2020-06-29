class Persona:
    def __init__(self):
        self.codigo = []
        self.nombre=[]
        self.apellido=[]
        self.telefono=[]
        self.carnet=[]

class Conductor(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.tipo_licencia=[]
        self.vehiculo=[]
        self.habilitado = []
        self.estado=[]
        self.cod = 0

class Usuario:
    def __init__(self):
        self.email=[]
        self.password=[]

class TipoVehiculo:
    def __init__(self):
        self.tipo_vehiculo=[]


class Vehiculo(TipoVehiculo):
    def __init__(self):
        TipoVehiculo.__init__(self)
        self.placa=[]
        self.cilindrada=[]      

class Marca:
    def __init__(self):
        self.marca=[]
        self.procedencia=[]

class Delivery(Conductor,Usuario,Vehiculo, Marca):
    def __init__(self):
        Conductor.__init__(self)
        Usuario.__init__(self)
        Vehiculo.__init__(self)
        Marca.__init__(self)
    
    def menu(self):
        print("""
            MENU REGISTRO DE CONDUCTORES
            1.- REGISTRAR
            2.- MOSTRAR REGISTRO
            3.- MOSTRAR HABILITADOS
            4.- MOSTRAR NO HABILITADOS
            5.- MODIFICAR DATOS DE CONDUCTOR
            6.- SALIR
        """)
        eleccion = int(input("Seleccione una opcion: \n"))
        if eleccion == 1:
            print(self.registrar())
            print(self.menu())
        elif eleccion==2:
            print(self.listar())
            print(self.menu())
        elif eleccion==3:
            print(self.listar())
            print(self.menu())
        elif eleccion==4:
            print(self.habilitados())
            print(self.menu())
        elif eleccion==5:
            print(self.editar())
            print(self.menu())
        elif eleccion == 6:
            print("Gracias por utilizar el sistema")
        else:
            print("Seleccione una opcion valida")
            self.menu()

    def registrar(self):
        nombre = input("Digite su nombre: \n")
        apellido = input("Digite el apellido: \n")
        telefono = int(input("Digite el telefono: \n"))
        carnet = int(input("Digite su carnet: \n"))
        tipo_licencia = input("Digite su tipo de licencia AUTO/MOTOCLICLETA: \n")
        Vehiculo = input("Digite su tipo de vehiculo: \n")
        email = input("Digite su correo electronico: \n")
        password =input("Digite una contraseña: \n")
        tipo_vehiculo =input("Seleccione su tipo de vehiculo:  \n ")
        placa =input("Digite su numero de placa de circulacion \n")
        cilindrada=input("Digite su cilindrada de su vehiculo: \n")
        marca=input("Digite la marca de su vehiculo: \n")
        procedencia=input("Digite su procedencia de su vehiculo: \n")
        codigo = self.code()
        print(self.guardar(nombre, apellido, telefono, carnet, tipo_licencia, Vehiculo, 
        email,password,tipo_vehiculo,placa,cilindrada,marca, procedencia, codigo))
        agregarOtro=input("Desea agregar mas registros? s/n \n")
        if agregarOtro == 's' or agregarOtro =='S':
            self.registrar()
        return 'Se registro correctamente.!'


    def guardar(self,codigo,nombre, apellido,telefono,carnet,tipo_licencia,vehiculo,
        email,password,tipo_vehiculo,placa,cilindrada,marca, procedencia):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        self.tipo_licencia.append(tipo_licencia)
        self.vehiculo.append(vehiculo)
        self.email.append(email)
        self.password.append(password)
        self.tipo_vehiculo.append(tipo_vehiculo)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
        self.marca.append(marca)
        self.procedencia.append(procedencia)
        self.habilitado.append(1)
        self.estado.append(1)
        return '{} registrado exitosamente.!!'.format(nombre)

    def listar(self):
        if self.nombre:
            for i in range(len(self.nombre)):
                self.detalle(i)
        else:
            print("TODAVIA NO SE REGISTRARON DATOS.!!")
        pass



    def detalle(self, posicion):
        if (self.estado[posicion] == 1):
            print("CODIGO: {}".format(self.codigo[posicion]))
            if (self.habilitado[posicion] == 1):
                print("habilitado: si")
            elif (self.habilitado[posicion] == 0):
                print("habilitado: No")
            print("NOMBRE: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
            print("TELEFONO: {}".format(self.telefono[posicion]))
            print("CARNET: {}".format(self.carnet[posicion]))
            print("TIPO DE LICENCIA: {}".format(self.tipo_licencia[posicion]))
            print("VEHICULO: {}".format(self.vehiculo[posicion]))
            print("EMAIL: {}".format(self.email[posicion]))
            print("PASSWORD: {}".format(self.password[posicion]))
            print("TIPO DE VEHICULO: {}".format(self.tipo_vehiculo[posicion]))
            print("PLACA: {}".format(self.placa[posicion]))
            print("CILINDRADA: {}".format(self.cilindrada[posicion]))
            print("MARCA: {}".format(self.marca[posicion]))
            print("PROCEDENCIA: {}".format(self.procedencia[posicion]))
            print("-------------------------------")
            pass


    def modificar(self):
        self.listar()
        print("-------------------------------")
        editar = input("Digite el codigo a modificar: \n")
        posicion = self.codigo.index(editar)
        self.detalle(posicion)
        return posicion

    def editar(self):
        posicion = self.modificar()
        dato = input("Desea modificar el tipo de licencia?: s/n \n")
        datoActual = self.tipo_licencia[posicion]
        tipo_licencia = self.confirmarEditarStr(dato,datoActual)
        
        dato = input("Desea modificar el vehiculo?: s/n \n")
        datoActual = self.vehiculo[posicion]
        vehiculo = self.confirmarEditarStr(dato,datoActual)

        dato = input("Desea modificar el tipo de vehiculo?:s/n \n")
        datoActual = self.tipo_vehiculo[posicion]
        tipo_vehiculo = self.confirmarEditarStr(dato,datoActual)

        dato = input("Desea modificar nueva placa?:s/n\n")
        datoActual = self.placa[posicion]
        placa = self.confirmarEditarStr(dato,datoActual)

        dato = input("Desea modificar nueva cilindrada?:s/n \n")
        datoActual = self.cilindrada[posicion]
        cilindrada = self.confirmarEditarStr(dato,datoActual)

        dato = input("Desea modificar nueva marca?:s/n \n")
        datoActual = self.marca[posicion]
        marca = self.confirmarEditarStr(dato,datoActual)

        dato = input("Desea modificar nueva procedencia?:s/n \n")
        datoActual = self.procedencia[posicion]
        procedencia = self.confirmarEditarStr(dato,datoActual) 
        self.habilitados()       
        self.guardarModificacion(posicion,tipo_licencia,vehiculo,tipo_vehiculo,placa,cilindrada,marca,procedencia)
        self.otros()

    def confirmarEditarStr(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = input("Ingrese el nuevo dato: \n")
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu")
            self.menu()

    def confirmarEditarInt(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = int(input("Ingrese el nuevo dato: \n"))
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu modificar")
            self.menu()

    def guardarModificacion(self,posicion,tipo_licencia,vehiculo,tipo_vehiculo,placa,cilindrada,marca,procedencia):
        self.tipo_licencia[posicion] = tipo_licencia
        self.vehiculo[posicion] = vehiculo
        self.tipo_vehiculo[posicion] = tipo_vehiculo
        self.placa[posicion] = placa
        self.cilindrada[posicion] = cilindrada
        self.marca[posicion] = marca
        self.procedencia[posicion] = procedencia
        return "** Actualizado correctamente.!!! **"

    def otros(self):
        otro = input("Desea modificar otro dato ? s/n \n")
        if (otro == "s" or otro == "S"):
            self.editar()
        if (otro == "n" or otro == "N"):
            print("**DATOS GUARDADOS CORRECTAMENTE*******")
            return self.menu()

    def code(self):
        if (self.cod >= 10):
            self.cod = self.cod + 1
            codigo = "0" + str(self.cod)
            return codigo
        elif (self.cod < 10):
            self.cod = self.cod + 1
            codigo = "00" + str(self.cod)
            return codigo

    def habilitados(self):
        if self.nombre:
            self.listar()
            print("-------------------------------")
            pregunta = input("¿Desea deshabilitar un condigo? \n")
            posicion = self.codigo.index(pregunta)
            print(self.cambioHabilitado(posicion))
            otro = input("Desea deshabilitar otro codigo? s/n \n")
            if (otro == "s" or otro == "S"):
                self.habilitados()
            elif (otro == "n" or otro == "N"):
                self.menu()
        else:
            return "**** La lista del menú se encuentra vacia *** "

    def cambioHabilitado(self, posicion):
        self.habilitado[posicion] = 0
        return "Deshabilitado exitosamente"

delivery = Delivery()
delivery.guardar("1", "Paul", "Banegas", "75568447","9008444","A","Auto","PaulBanegas@gmail.com","*******","Auto","4950mmm","1200cc","Honda","japon")
delivery.guardar("2", "Diego", "Mendez", "75568447","9008444","M","Moto","DiegoMendez@gmail.com","*******","Motocicleta","4950tfn","150cc","Honda","japon")
delivery.guardar("3", "Marco", "Dominguez", "75568447","9008444","M","Moto","MarcoDominguez@gmail.com","*******","Motocicleta","4950ppp","200cc","Honda","japon")
delivery.menu()
