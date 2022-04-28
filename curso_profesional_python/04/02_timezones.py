from datetime import datetime
import pytz

# Fomat by time zone with pytz lib

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print('Bogota date: ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)
print('Caracas date: ', caracas_date.strftime('%d/%m/%Y, %H:%M:%S'))

cordoba_timezone = pytz.timezone('America/Cordoba')
cordoba_date = datetime.now(cordoba_timezone)
print('cordoba date: ', cordoba_date.strftime('%d/%m/%Y, %H:%M:%S'))
