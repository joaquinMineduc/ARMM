import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from panel_functions import *
from inserts_functions import *


columns = ['G','K','M','O']
columns_graps = ['B','C','D','E']


# Se modifica el panel del informe, la primera página que contiene los gráficos.
route = modify_file('APP/Backend/Input/Reports/formato.xlsx', 
                   '01-PANEL',df_principal_panel, columns, 9, 12)

# Se agrega la fecha al documento
modify_file(route, '01-PANEL', date_document, 'M', 5, 5)

# Grafico PMG
modify_file(route, 'data_panel',df_grap_PMG, columns_graps, 4, 6)

# Grafico H
modify_file(route, 'data_panel',df_grap_H, columns_graps, 8, 11)

# Grafico CDC NC
modify_file(route, 'data_panel',df_grap_CDC, columns_graps, 13, 20)

# Grafico Regiones CDC
modify_file(route, 'data_panel',df_grap_reg, columns_graps, 25, 40)




#modify_file(route, 'Ev Proveedores', df_regional, columns_reg, 11, 26)