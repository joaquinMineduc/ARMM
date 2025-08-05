import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_reg import create_df_reg, date_document
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import Path_last_report

columns = ['B','C','D','E']

def insert_data_reg():
    df_status_REG = create_df_reg()
    modify_file(Path_last_report , 'data_status_reg', df_status_REG, columns, 4, 83)
    modify_file(Path_last_report, '03-  ESTADO REGIONES', date_document, 'A', 2, 2)
