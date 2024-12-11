import sys
import os

# Añadir el directorio raíz de Backend al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Ahora puedes importar el módulo
from data_analitics.eval_functions import df_eval_NC

# Usa df_eval_NC o realiza cualquier operación
print(df_eval_NC)