from datetime import datetime
import locale

# Configuración del idioma del entorno local, se cambia de EN a ES
try:
    # Esto funciona en la mayoría de los sistemas operativos
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para Windows


def get_year():
    month = datetime.now().month -1
    if month == 0:
        month = 12
        year = datetime.now().year -1
    date = datetime(year, month, 1).strftime("%Y-%B")
    return date


    
