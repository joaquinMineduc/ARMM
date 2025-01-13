import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ins_adp import route
from inserts_functions import *
from risk_functions import *


DATE_REPORT = get_date()


columns = ['B','C','D']

matriz_columns = ['G','I','L','O','R','T','V','X']
risk_columns = ['L','O','Q','S','T','V','W','Y']
columns_graph = ['C','D','E']

modify_file(route, 'Gestión de riesgos', DATE_REPORT,'B', 4, 4)

modify_file(route, 'Gestión de riesgos', df_risk_tools, columns, 8, 15)

modify_file(route, 'Gestión de riesgos', df_monitoring, columns, 19, 23)

modify_file(route, 'Gestión de riesgos', df_matriz, matriz_columns, 14, 22)

modify_file(route, 'Gestión de riesgos', df_risk, risk_columns, 29, 37)

modify_file(route, 'data_riesgos', df_grap, columns_graph, 15, 39)