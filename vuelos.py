from avion import avion

class vuelos(object):
    avion=None
    fecha=None
    hora=None
    origen=None
    destino=None

    def __init__(self,a,f,h,o,d):
        self.avion=a
        self.fecha=f
        self.hora=h
        self.origen=o
        self.destino=d
        self.lista_pas=[]
        self.lista_trip=[]
        self.lista_idiomas=[]

    def lista_pasajeros(self):
        d = { 'vuelo':[{'pasajeros':[]}]}

        for a in self.lista_pas:
            d['vuelo'['pasajeros']].append(a.dic_pasajero())

    def ej_2(self):

        menor = self.lista_pas[0]

        for a in self.lista_pas:
            if a.getfecha < menor.getfecha:
                menor = a

        pas_menor = {'Nombre': menor.nombre,
                     'Apellido': menor.apellido,
                     'Fecha_nac': menor.fecha_nac,
                     'Dni': menor.dni}

        return pas_menor

    def ej3(self):

        if len(self.lista_trip) < avion.cant_tripulantes_nec:

            vuelo_trip_nec = {'Avion': self.avion,
                              'Fecha': self.fecha,
                              'Hora': self.hora,
                              'Origen': self.origen,
                              'Destino': self.destino}

            return vuelo_trip_nec

    def ej4(self):

        for a in self.lista_trip:
            for b in a.modelos_avion:
                if b != self.avion.modelo:
                    vuelito = {'Avion': self.avion,
                               'Fecha': self.fecha,
                               'Hora': self.hora,
                               'Origen': self.origen,
                               'Destino': self.destino}

                    return vuelito

    def ej6(self):
        for a in self.lista_pas:
            if a.vip == 1 or a.necesidades != 'ninguna':

                pasajero = {'nombre': a.nombre,
                            'apellido': a.apellido,
                            'fecha_nac': a.fecha_nac,
                            'dni': a.dni,
                            'vip': a.vip,
                            'necesidades': a.necesidades}

                return pasajero

    def ej7(self):

        for a in self.lista_idiomas:
            for b in self.lista_idiomas[1:]:
                if a == b:
                    self.lista_idiomas.remove(b)

                    vuelito = {'Avion': self.avion,
                               'Fecha': self.fecha,
                               'Hora': self.hora,
                               'Origen': self.origen,
                               'Destino': self.destino}

                    return vuelito













