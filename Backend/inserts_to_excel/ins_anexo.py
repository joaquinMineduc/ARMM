import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisis_datos import df_informe, df_risk
from Backend.inserts_to_excel.inserts_functions import modify_anexo, apply_borders
from Frontend.Variables import dir_in, dir_output, path_anexo, path_anexo, format_anexo
from principal_functions import get_date

year_report = get_date(format2=True, text="Año")

print(year_report)
columns = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

def insert_data_anexo():
    modify_anexo(dir_in + format_anexo, 'anexo_final', df_informe, columns, 5, 127)
    modify_anexo(dir_output + path_anexo, 'anexo_final', year_report, 'F', 3, 3)
    modify_anexo(dir_output + path_anexo, 'anexo_risk', df_risk, columns, 5, 127)
    modify_anexo(dir_output + path_anexo, 'anexo_risk', year_report, 'F', 3, 3)
    apply_borders(dir_output + path_anexo, 'anexo_final')
    apply_borders(dir_output + path_anexo, 'anexo_risk')