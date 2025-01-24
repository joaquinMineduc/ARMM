import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Backend.inserts_to_excel.inserts_functions import modify_file
from programs_functions import df_exante, df_graph, df_monitoring, df_programs
from Frontend.Variables import dir_output, path_report

columns_monitoring = ['E','H']
columns_programs = ['B','C']
columns_exante = ['K','M','O']
columns_graph = ['A','B','C','D']

def insert_data_programs():
        
    modify_file(dir_output + path_report, 'programas sociales', df_monitoring, columns_monitoring, 13, 18)
    modify_file(dir_output + path_report, 'programas sociales', df_programs, columns_programs, 22, 27)
    modify_file(dir_output + path_report, 'programas sociales', df_exante, columns_exante, 6, 27)
    modify_file(dir_output + path_report, 'datos_graficos', df_graph, columns_graph, 3, 14)


