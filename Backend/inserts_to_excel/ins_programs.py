import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal_functions import *
from Backend.inserts_to_excel.inserts_functions import modify_file
from programs_functions import df_exante, df_graph, df_monitoring, df_programs
from Frontend.Variables import dir_output, path_report

date_document = get_date()

columns_monitoring = ['E','H']
columns_programs = ['B','C']
columns_exante = ['K','M','O']
columns_graph = ['A','B','C','D']

def insert_data_programs():
    modify_file(dir_output + path_report, 'programas sociales', df_monitoring, columns_monitoring, 15, 20)
    modify_file(dir_output + path_report, 'programas sociales', df_programs, columns_programs, 16, 21)
    modify_file(dir_output + path_report, 'programas sociales', df_exante, columns_exante, 6, 23)
    modify_file(dir_output + path_report, 'programas sociales', date_document, 'G', 2, 2)
    modify_file(dir_output + path_report, 'datos_graficos', df_graph, columns_graph, 3, 15)
    
    
   


