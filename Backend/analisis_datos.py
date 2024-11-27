from analitics_class import *
import pandas as pd

# Creación del data frame
df = create_dataFrame('APP/Backend/Input/indicadores.xls')

# Se claisifcan indicadores ponderados
df = clasificator_by_ponderation(df)



split_column(df,'Indicador','Instrumento')







