import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisis_datos import df
from inserts_functions import *


colums = ['G','K','M','O']


# Se modifica el panel del informe, la primera página que contiene los gráficos.
route = modify_file('APP/Backend/Input/formato.xlsx', 
                   '01-PANEL',df, colums, 9, 12)

#modify_file(route, 'Ev Proveedores', df_regional, columns_reg, 11, 26)