import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from panel_functions import *
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import path_report, dir_output


DATE_REPORT = get_date()

columns = ['G','K','M','O']
columns_graps = ['B','C','D','E']

def insert_data_panel():

    # Se agrega la fecha al documento
    modify_file(dir_output + path_report, '01-PANEL', DATE_REPORT, 'N', 5, 5)
    # Se modifica el panel del informe, la primera página que contiene los gráficos.
    modify_file(dir_output + path_report,'01-PANEL', df_principal_panel, columns, 10, 13)
    # Grafico PMG
    modify_file(dir_output + path_report, 'data_panel',df_grap_PMG, columns_graps, 4, 6)
    # Grafico H
    modify_file(dir_output + path_report, 'data_panel',df_grap_H, columns_graps, 8, 11)
    # Grafico CDC NC
    modify_file(dir_output + path_report, 'data_panel',df_grap_CDC, columns_graps, 13, 20)
    # Grafico Regiones CDC
    modify_file(dir_output + path_report, 'data_panel',df_grap_reg, columns_graps, 25, 40)

