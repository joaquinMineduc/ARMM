import pandas as pd
import numpy as np
from static_data import *
from helper_functions import *

# Aplicar multiproceso para mejorar rendimiento : PENDIENTE 
def create_dataframe(location, sheet, header):
    if (sheet and header) is None: 
        df = pd.read_excel(location, header = 0) # Si hoja y header no están definidos
       
    if sheet is None and header is not None: 
        df = pd.read_excel(location, header = header)# Si sólo se tiene header
    else:
        df = pd.read_excel(location, sheet, header = header)# Si se encuentran todos los argumentos
    return df


# Eliminar columnas innecesarias
def drop_unless_columns(df, start, end, columns):
    list_index = list(df.columns)
    if (start and end) is None and columns is None:
        for index in drop_index:
            df.drop(list_index[index], axis = 1, inplace = True)
    if (start and end) is None and columns is not None:
        if isinstance(columns, list):
            for index in columns:
                df.drop(list_index[index], axis = 1, inplace = True)
        else:
            df.drop(list_index[columns], axis = 1, inplace = True)
    if (start and end) is not None and columns is  None:
        for index in range(start, end):
            df.drop(list_index[index], axis = 1, inplace = True)
    return df


# Eliminar filas innecesarias
def drop_unless_rows(df, start, end, rows):
    if (start and end) is None:
        if isinstance(rows, list):
            for index in rows:
                df.drop(index = index, axis = 0, inplace = True)
        else:
            df.drop(index = rows, axis = 0, inplace = True)
    else:
        for index in range(start, end):
            df.drop(index = index, axis = 0, inplace = True)
    return df



# Crea una copia de un dataframe para la manipulacion de datos
def create_an_copy(df, columns):
    if isinstance(columns, list):
        df_copy = df[columns].copy() # Se copian todas las columnas
    else:
        df_copy = df[columns].copy() # Se copia  sólo 1 columna del df original
    return df_copy


# Funcion que clasifica las regiones según su id de SECREDUC
def classify_reg(df):
    list_regiones = []
    df_reg = create_an_copy(df, 'Regiones')
    for reg in df_reg:
        region = classificator_by_reg(reg, '_')
        list_regiones.append(region)
    df.loc[:, 'Regiones'] = list_regiones
    return df


# Cambiar formatos de las columns con procentajes
def format_eval_columns(df):
    columns = list(df.columns)
    for col in columns:
        if col != 'Regiones':
            df[col] = df[col].apply(
            lambda x: np.floor(x*10)/10).apply(lambda x: int(x)).apply(
            lambda x: str(x) + "%")
            
            
# Funcion que crea una particion de un DF
def partioner(df, start, end):
    return df.iloc[start:end]
