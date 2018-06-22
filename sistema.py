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


