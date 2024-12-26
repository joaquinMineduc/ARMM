import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from status_NC import df_status_NC
from ins_panel import route
from inserts_functions import *


columns = ['I','j']

# Grafico PMG
modify_file(route, 'data_status_NC', df_status_NC, columns, 3, 50)