from personaTP import persona

class tripulante(persona):

    def __init__(self,n,a,f,d):
        persona.__init__(n,a,f,d)
        self.modelos_avion=[]
        self.idiomas=[]

    def agregar_modelo(self,m):
        self.modelos_avion.append(m)

    def agregar_idioma(self,i):
        self.idiomas.append(i)



