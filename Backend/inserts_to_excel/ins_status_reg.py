import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_reg import df_status_REG, date_document
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import dir_output, path_report

columns = ['B','C','D','E']

def insert_data_reg():
    
    modify_file(dir_output + path_report , 'data_status_reg', df_status_REG, columns, 4, 67)
    modify_file(dir_output + path_report, '03-  ESTADO REGIONES', date_document, 'B', 3, 3)
