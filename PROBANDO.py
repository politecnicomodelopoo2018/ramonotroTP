from sistema import sistema

S=sistema()
S.cargar()

for a in S.cargar_aviones():
    print(a.modelo)