import json
from avion import avion
from vuelos import vuelos

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
                            for d in a.lista_trip[1:]:
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




