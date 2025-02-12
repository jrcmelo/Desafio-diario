'''
Crie uma função que receba uma string representando um horário no formato hh:mm:ss e converta-o para o total de segundos. 
Certifique-se de validar a entrada para evitar erros de formato.
'''

import datetime

time = input(datetime.time)

date_time = datetime.datetime.strptime(time, "%H:%M:%S")
a_timedelta = date_time - datetime.datetime(1900, 1, 1)
seconds = a_timedelta.total_seconds()

print(seconds)