import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal_functions import get_date
from Backend.inserts_to_excel.inserts_functions import modify_file
from Frontend.Variables import Path_last_report, path_report_format
from Backend.principal_functions import get_month
from Backend.helper_functions import modify_status


def ins_data_to_report():
    month_validation = get_month()
    if month_validation in ['ABRIL','JULIO','OCTUBRE']:
        modify_status("Planes de tratamientos", status = True)
    DATE_REPORT = get_date()
    YEAR_REPORT = DATE_REPORT[-4:]
    # Este código modifica la primer pagina del informe, la portada.
    modify_file(path_report_format, 'Portada', YEAR_REPORT, 'G', 11, 11)
    modify_file(Path_last_report, 'Portada', DATE_REPORT, 'F', 12, 12)