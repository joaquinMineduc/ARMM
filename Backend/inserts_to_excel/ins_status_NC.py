import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_NC import df_status_NC, date_document
from Backend.inserts_to_excel.inserts_functions import *
from Frontend.Variables import dir_output, path_report

columns = ['A','D','E','F','G']

def insert_status_NC():
    modify_file(dir_output + path_report, 'data_status_NC', df_status_NC, columns, 3)
    modify_file(dir_output + path_report, '02-ESTADO NC', date_document, 'T', 2, 2)
    insert_format_estructure()
    

def insert_format_estructure():
    end_row = 3 + len(df_status_NC) -1 #Se realiza el calculo del total de filas a completar
    # apply_format_status_risk(dir_output + path_report, 'data_status_NC', f'G3:G{end_row}')
    formula = '=IF($F3="bajo",0,IF($F3="medio",2,IF($F3="alto",3,4)))'
    apply_format_formula(dir_output + path_report, 'data_status_NC', formula, 'C', 3, end_row)


