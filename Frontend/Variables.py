import os, sys
from pathlib import Path

# Añade la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

#-----------Configuración de directorio base ---------------------#

proyecto_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proyecto_path)


# Ruta absoluta del archivo actual
ruta_actual = Path(__file__).resolve()

# Subir 3 niveles hasta llegar a APP/
ruta_base = ruta_actual.parents[1]  # 0 = mi_archivo.py, 1 = format_reports, 2 = Input, 3 = Backend


#---------------- Variables de utilidad --------------------------#

# -------------- Colores en Exadecimal ----------------------#

# Color gob_blue
Exgob_blue = "#1569b2"

# color gob_red
Exgob_Red = "#eb3947"

# color gob_hover_red
Exgob_hover_red = "#CB0E19"

 # color gob_disabled_red
Exgob_disabled_red = "#DABEC0"

# color gob_hover_red
Exgob_disabled_blue = "#95B2CB"

 # Color Letras gob_gray
Exgob_Gray = "#8E8B8B"

# Matiz gob_gray
Exgob_GrayLigth = "#EEEEEE"

# Color gob_white
Exgob_white = "#FFFFFF"

# color gob_black
Exgob_black = "#000000"

# Color azul_oscuro
Exazul_oscuro = "0E2841"

# Subrayado de titulos file XLSX
Exa_subrayado = "64BEE6"
# ---------------- Colores Formato RGB -----------------------------#

# color gob_blue RGB
Rgob_blue = (21,105,178,255)

# Color gob_red RGB
Rgob_Red = (235,57,71,255)

# Color letras gob_gray RGB
Rgob_Gray = (137,137,137,52)

# Color gob_white RGB
Rgob_white = (0,0,0,0)

# ------------------- Variables de directorios de salida  --------------- #
dir_in = (Path(ruta_base)/ 'Backend/Input/format_reports/').resolve()
dir_output = (Path(ruta_base)/ 'Backend/output/').resolve()
Path_charts_PTR = (Path(dir_output)/ 'graphics/PTR/').resolve()
Path_charts_NC = (Path(dir_output)/ 'graphics/NC/').resolve()
Path_last_report = (Path(dir_output)/ 'informe_final.xlsx').resolve()
path_report_format = (Path(dir_in)/'formato.xlsx').resolve()
path_last_anexo = (Path(dir_output)/'anexo_final.xlsx').resolve()
dir_output_PDFs = (Path(dir_output)/'report_parts/').resolve()
format_anexo = (Path(dir_in)/'format_anexo.xlsx').resolve()
