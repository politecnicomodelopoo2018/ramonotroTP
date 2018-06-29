import json
from avion import avion
from vuelos import vuelos
from datetime import datetime
from pasajero import pasajero
from tripulante import tripulante
class sistema(object):
    diccionario = {'listado_pasajeros': []}


    la_biblia = {
                 'ej 1':[],
                 'ej 2':[],
                 'ej 3':[],
                 'ej 4':[],
                 'ej 5':[],
                 'ej 6':[],
                 'ej 7':[]
                }

    def __init__(self):
        self.lista_vuelos=[]
        self.lista_aviones=[]



    def agregar_vuelos(self,v):
        self.lista_vuelos.append(v)

    def ej1(self):
        for a in self.lista_vuelos:
            self.la_biblia['ej 1'].append(a.lista_pasajeros())

    def ej2(self):
        for a in self.lista_vuelos:
            self.la_biblia['ej 2'].append(a.ej_2())

    def ej3(self):
        for a in self.lista_vuelos:
            self.la_biblia['ej 3'].append(a.ej3())

    def ej4(self):

        for a in self.lista_vuelos:
            self.la_biblia['ej 4'].append(a.ej4())


    def ej5(self):

        for a in self.lista_vuelos:
            for b in self.lista_vuelos[1:]:
                if a != b:
                    if a.fecha == b.fecha:
                        for c in a.lista_trip:
                            for d in b.lista_trip:
                                if c.dni == d.dni:

                                    tripulant = {'nombre': c.nombre,
                                                 'apellido': c.apellido,
                                                 'fecha_nac': c.fecha_nac,
                                                 'dni': c.dni}

                                    self.la_biblia['ej 5'].append(tripulant)

        return tripulant



    def ej6(self):
        for a in self.lista_vuelos:
            self.la_biblia['ej 6'].append(a.ej6())

    def ej7(self):
        for a in self.lista_vuelos:
            self.la_biblia['ej 7'].append(a.ej7())

    def cargar(self):
        self.cargar_aviones()
        self.cargar_vuelo()
        self.cargar_personitas()
    def cargar_aviones(self):
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)

            for a in aux2['Aviones']:
                unavion = avion(a['codigoUnico'],a['cantidadDePasajerosMaxima'],a['cantidadDeTripulaciónNecesaria'])

                self.lista_aviones.append(unavion)

    def cargar_vuelo(self):
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)

            for a in aux2['Vuelos']:

                    for c in self.lista_aviones:
                        if c.modelo == a['avion']:
                            unvuelo=vuelos(c,datetime.strptime(a['fecha'], '%Y-%m-%d').date(),a['hora'],a['origen'],a['destino'])
                            unvuelo.lista_pas=a['pasajeros']
                            unvuelo.lista_trip=a['tripulacion']

                            self.lista_vuelos.append(unvuelo)


    def cargar_personitas(self):
        self.pasajeros = []
        self.tripulantes = []
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)
            for a in aux2['Personas']:
                if a['tipo'] == 'Pasajero':
                    if 'solicitudesEspeciales' in a:
                        UnPasaj = pasajero(a['nombre'], a['apellido'],
                                            datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'],
                                            a['vip'], a['solicitudesEspeciales'])
                        self.pasajeros.append(UnPasaj)
                    else:
                        UnPasaj = pasajero(a['nombre'], a['apellido'],
                                            datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'],
                                            a['vip'],
                                            'Ninguna')
                        self.pasajeros.append(UnPasaj)

                else:

                    if 'idiomas' in a:
                        UnTripu = tripulante(a['nombre'], a['apellido'],
                                              datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'])
                        UnTripu.modelos_avion = a['avionesHabilitados']
                        UnTripu.idiomas = a['idiomas']
                        self.tripulantes.append(UnTripu)
                    else:
                        UnTripu = tripulante(a['nombre'], a['apellido'],
                                              datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'])
                        UnTripu.modelos_avion = a['avionesHabilitados']
                        UnTripu.idiomas = ''


                        self.tripulantes.append(UnTripu)


        self.cargar_meter_personas(self.pasajeros, self.tripulantes)

    def cargar_meter_personas(self, pasaj, tripu):
        for a in self.lista_vuelos:
            lista=[]
            for b in a.lista_pas:
                for c in pasaj:
                    if b == c.dni:
                        lista.append(c)

            a.lista_pas=lista

        for a in self.lista_vuelos:
            lista=[]
            for b in a.lista_trip:
                for c in tripu:
                    if b == c.dni:
                        lista.append(c)

            a.lista_trip=lista





