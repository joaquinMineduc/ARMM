import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisis_datos import df_informe, df_risk
from inserts_functions import modify_anexo, apply_borders


columns = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

route_anexo = modify_anexo("APP/Backend/Input/Reports/format_anexo.xlsx",'anexo_final', df_informe, columns, 5, 111)

modify_anexo(route_anexo, 'anexo_risk', df_risk, columns, 5, 111)

apply_borders(route_anexo, 'anexo_final')
apply_borders(route_anexo, 'anexo_risk')