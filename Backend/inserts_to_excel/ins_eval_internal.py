import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from eval_functions import df_eval_NC, df_regional
from ins_status_reg import route
from inserts_functions import *




colums_nc = ['C','D','E','F','G']
columns_reg = ['I','J','K','L','M']


modify_file(route, 'Ev Proveedores',df_eval_NC, colums_nc, 11, 29)

modify_file(route, 'Ev Proveedores', df_regional, columns_reg, 11, 26)


