

class sistema(object):
    diccionario = {'listado_pasajeros': []}

    def __init__(self):
        self.lista_vuelos=[]


    def agregar_vuelos(self,v):
        self.lista_vuelos.append(v)

    def listado_pasajeros(self):
        dic={'pasajeros por vuelo': []}

        for a in self.lista_vuelos:
            a.Caca1