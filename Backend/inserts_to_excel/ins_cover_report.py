import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal_functions import get_date
from inserts_functions import modify_file

DATE_REPORT = get_date()
YEAR_REPORT = DATE_REPORT[-4:]


# Este código modifica la primer pagina del informe, la portada.
route = modify_file('APP/Backend/Input/Reports/formato.xlsx','Portada', YEAR_REPORT, 'G', 11, 11)

modify_file(route,'Portada', DATE_REPORT, 'F', 12, 12)