from datetime import date

hoy = date(1997, 2, 26)
otra_fecha = date(2000, 6, 2)

delta = otra_fecha - hoy

print(delta.days / 365 )