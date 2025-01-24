import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from eval_functions import df_eval_NC, df_regional
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import dir_output, path_report


colums_nc = ['C','D','E','F','G']
columns_reg = ['I','J','K','L','M']

def insert_data_prov():
    
    modify_file(dir_output + path_report, 'Ev Proveedores',df_eval_NC, colums_nc, 11, 29)
    modify_file(dir_output + path_report, 'Ev Proveedores', df_regional, columns_reg, 11, 26)


