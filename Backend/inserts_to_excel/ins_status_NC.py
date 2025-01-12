import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from status_NC import df_status_NC, date_document
from ins_panel import route
from inserts_functions import *


columns = ['I','j']

# Grafico PMG
modify_file(route, 'data_status_NC', df_status_NC, columns, 3, 50)
modify_file(route, '02-ESTADO NC', date_document, 'T', 2, 2)