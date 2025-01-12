import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ins_risk import route
from inserts_functions import *
from programs_functions import df_exante, df_graph, df_monitoring, df_programs

columns_monitoring = ['E','F']
columns_programs = ['B','C','D','E','F']
columns_exante = ['I','K','M']
columns_graph = ['A','B','C','D']

modify_file(route, 'programas sociales', df_monitoring, columns_monitoring, 13, 18)

modify_file(route, 'programas sociales', df_programs, columns_programs, 21, 26)

modify_file(route, 'programas sociales', df_exante, columns_exante, 6, 18)

modify_file(route, 'datos_graficos', df_graph, columns_graph, 3, 14)