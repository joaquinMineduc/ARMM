import os, sys


#-----------Configuración de directorio base ---------------------#

proyecto_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proyecto_path)

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
dir_in = "APP/Backend/Input"
dir_output = "APP/Backend/output"