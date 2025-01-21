import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ins_eval_internal import route
from inserts_functions import *
from adp_functions import *


DATE_REPORT = get_date(format = True)


date_columns = ['B']
date_acum_columns = ['I']
services_columns = ['B','C','E','F','G','H','I','J']
comment_columns = ['D','E']


modify_file(route, 'Convenios ADP', df_adp_data, services_columns, 6, 12)

modify_file(route, 'Convenios ADP', df_adp_comments, comment_columns, 16, 22)

modify_file(route, 'Convenios ADP', DATE_REPORT, 'H', 2, 2)

modify_file(route, 'Convenios ADP', date_subtitle, 'B', 3, 3)

