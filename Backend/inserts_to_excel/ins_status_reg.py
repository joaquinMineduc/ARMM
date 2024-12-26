import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_reg import df_status_REG
from ins_status_NC import route
from inserts_functions import *

columns = ['B','C','D','E']

modify_file(route, 'data_status_reg',df_status_REG, columns, 4, 67)


