from avion import avion
from pasajero import pasajero

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
        d = {'vuelo':[{'pasajeros':[]}]}

        for a in self.lista_pas:
            d['vuelo'][0]['pasajeros'].append(a.dic_pasajero())

        return d

    def ej_2(self):

        menor = self.lista_pas[0]

        for a in self.lista_pas:
            if a.fecha_nac > menor.fecha_nac:
                menor = a

        pas_menor = {'Nombre': menor.nombre,
                     'Apellido': menor.apellido,
                     'Fecha_nac': menor.fecha_nac,
                     'Dni': menor.dni}

        return pas_menor

    def ej3(self):

        if len(self.lista_trip) < self.avion.cant_tripulantes_nec:

            vuelo_trip_nec = {'Avion': self.avion.modelo,
                              'Fecha': self.fecha,
                              'Hora': self.hora,
                              'Origen': self.origen,
                              'Destino': self.destino}

            return vuelo_trip_nec

    def ej4(self):

        for a in self.lista_trip:
            if self.avion.modelo not in a.modelos_avion:


                    vuelito = {'Avion': self.avion.modelo,
                               'Fecha': self.fecha,
                               'Hora': self.hora,
                               'Origen': self.origen,
                               'Destino': self.destino}

                    return vuelito

    def ej6(self):
        for a in self.lista_pas:
            if a.vip == 1 or a.necesidades != 'Ninguna':

                pasajero = {'nombre': a.nombre,
                            'apellido': a.apellido,
                            'fecha_nac': a.fecha_nac,
                            'dni': a.dni,
                            'vip': a.vip,
                            'necesidades': a.necesidades}

                return pasajero

    def ej7(self):

        for a in self.lista_trip:
            for b in a.idiomas:
                if b not in self.lista_idiomas:
                    self.lista_idiomas.append(b)

        vuelito = {'Avion': self.avion.modelo,
                   'Fecha': self.fecha,
                   'Hora': self.hora,
                   'Origen': self.origen,
                   'Destino': self.destino}


        return vuelito,self.lista_idiomas













