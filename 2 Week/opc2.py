NumeroSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
Dias = NumeroSegundos // 86400
Horas = (NumeroSegundos % 86400) // 3600
Minutos = ((NumeroSegundos % 86400) % 3600) // 60
Segundos =  ((NumeroSegundos % 86400) % 3600) % 60
print(Dias, "dias,", Horas, "horas,", Minutos, "minutos e", Segundos, "segundos.")