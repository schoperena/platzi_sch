from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
