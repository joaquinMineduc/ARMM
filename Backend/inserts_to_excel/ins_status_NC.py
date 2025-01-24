import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_NC import df_status_NC, date_document
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import dir_output, path_report

columns = ['I','j']

def insert_status_NC():
    modify_file(dir_output + path_report, 'data_status_NC', df_status_NC, columns, 3, 50)
    modify_file(dir_output + path_report, '02-ESTADO NC', date_document, 'T', 2, 2)


