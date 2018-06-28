from sistema import sistema
from pasajero import pasajero
S=sistema()
S.cargar()


for a in S.lista_vuelos:
    print(a.avion.modelo)
    print('--')
    for b in a.lista_trip:
        print(b)
    print('--')