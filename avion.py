class avion(object):
    modelo=None
    cant_pasajeros=None
    cant_trpulantes_nec=None

    def __init__(self,m,cant_p,cant_t):
        self.modelo=m
        self.cant_pasajeros=cant_p
        self.cant_tripulantes_nec=cant_t

    def get_trip_nec(self):

        return self.cant_tripulantes_nec