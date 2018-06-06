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
        self.list_trip=[]

    def lista_pasajeros(self):
        vuelo = {'listado_pasajeros': []}




