import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status_reg import df_status_REG, date_document
from ins_status_NC import route
from inserts_functions import *

columns = ['B','C','D','E']

modify_file(route, 'data_status_reg', df_status_REG, columns, 4, 67)

modify_file(route, '03-  ESTADO REGIONES', date_document, 'B', 3, 3)
