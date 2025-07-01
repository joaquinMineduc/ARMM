import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import dir_output, path_report
from adp_functions import *


date_columns = ['B']
date_acum_columns = ['I']
services_columns = ['B','C','E','F','G','H','I','J']
comment_columns = ['D','E']


def insert_data_adp():
    
    modify_file(dir_output + path_report, 'Convenios ADP', df_adp_data, services_columns, 6, 12)
    modify_file(dir_output + path_report, 'Convenios ADP', df_adp_comments, comment_columns, 16, 22)
    modify_file(dir_output + path_report, 'Convenios ADP', date_document, 'I', 2, 2)
    modify_file(dir_output + path_report, 'Convenios ADP', date_subtitle, 'B', 3, 3)
    
    modify_file(dir_output + path_report, 'Convenios ADP_II', df_adp_data_II, services_columns, 6, 7)
    modify_file(dir_output + path_report, 'Convenios ADP_II', df_adp_comments_II, comment_columns, 13, 14)
    modify_file(dir_output + path_report, 'Convenios ADP_II', date_document, 'I', 2, 2)
    modify_file(dir_output + path_report, 'Convenios ADP_II', date_subtitle, 'B', 3, 3)
    

