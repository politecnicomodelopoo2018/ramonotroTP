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

        if len(vuelos.lista_trip) < avion.cant_tripulantes_nec:

    vuelo_trip_men = {'Avion': avion,
                      'Fecha': fecha,
                      'Hora': hora,
                      'Origen': origen,
                      'Destino': destino}




