import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisis_datos import df_informe
from inserts_functions import modify_anexo


columns = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

modify_anexo("Backend/Input/Reports/format_anexo.xlsx",'Sheet1', df_informe, columns, 5, 111)
