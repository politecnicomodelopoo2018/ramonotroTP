from personaTP import persona

class pasajero(persona):
    vip=None
    necesidades=None

    def __init__(self,n,a,f,d,v,nec):
        persona.__init__(self,n,a,f,d)
        self.vip=v
        self.necesidades=nec

    def dic_pasajero(self):
        pasajero = {'nombre': self.nombre,
                    'apellido': self.apellido,
                    'fecha de nac': self.fecha_nac,
                    'dni': self.dni,
                    'vip': self.vip,
                    'necesidades': self.necesidades
                    }
        return pasajero

    def getfecha(self):
        return self.fecha_nac