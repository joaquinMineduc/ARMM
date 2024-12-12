import sys
import os
import xlwings as xw
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_analitics.eval_functions import df_eval_NC, df_regional
from inserts_functions import *




colums_nc = ['C','D','E','F','G']
columns_reg = ['I','J','K','L','M']


route = modify_file('APP/Backend/Input/formato.xlsx', 
                   'Ev Proveedores',df_eval_NC, colums_nc, 11, 29)

modify_file(route, 'Ev Proveedores',df_regional, columns_reg, 11, 26)


