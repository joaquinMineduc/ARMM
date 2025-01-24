import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal_functions import get_date
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import dir_output, path_report, dir_in, path_report_format


def ins_data_to_report():

    DATE_REPORT = get_date()
    YEAR_REPORT = DATE_REPORT[-4:]
    # Este código modifica la primer pagina del informe, la portada.
    modify_file(dir_in + path_report_format, 'Portada', YEAR_REPORT, 'G', 11, 11)
    modify_file(dir_output + path_report, 'Portada', DATE_REPORT, 'F', 12, 12)