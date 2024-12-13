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


# Funcion que agrupa datos según una columna 
def union_by_column(df, column):
    df = df.groupby(by=[column]).mean()
    df.reset_index(inplace = True)
    df = df[order_columns_NC]
    df.columns = df_NC_columns
    return df

#Funcion para crear consultas query
def create_query(df, arg):
    df = df.query(f"`Lugar de medición` == 'GABSUB' and Variable.str.startswith('{arg}')").reset_index(drop=True)
    return df 


def modify_eval_values(df):
    df['Oportunidad'] = df['Oportunidad'].apply(
        lambda op: 100 if op == 'Si' else 0 if op == 'No' else 'Sin informar')
    df['Consistencia'] = df['Consistencia'].apply(
        lambda op: 100 if op == 'Si' else 0 if op == 'No' else 'Sin informar')
    df['Completitud'] = df['Completitud'].apply(
        lambda op: 100 if op == 'Si' else 0 if op == 'No' else 'Sin informar')
    return df

# recibe como argumento dataframe y arg = nuevo valor del lugar de medición
def create_means(df, arg):
    columns = df.columns
    for col in columns:
        if isinstance(df[col].dtype, int):
            df.loc[:, 'promedio'] = df.iloc[:,1:].mean(axis = 1)
            df = union_by_column(df, 'Lugar de medición')
        else:
            df.drop_duplicates(inplace = True)
            df.loc[:,'promedio'] = 'Sin informar'
        df.loc[:,'Lugar de medición'] = arg
    df.reset_index(inplace=True, drop = True)
    return df

def format_divition(df):
    list_divition = []
    for dv in df['División']:
        if dv == 'RECFIN':
            list_divition.append('Recursos Financieros')
        elif dv == 'SUBV':
            list_divition.append('Subvenciones')
        elif dv == 'AYUMIN':
            list_divition.append('Ayuda Mineduc')
        elif dv == 'INNOV':
            list_divition.append('Innovación')
        elif dv == 'SEJEC_TP':
            list_divition.append('TP')
        elif dv in ['AUDITORIA','ESTUDIOS']:
            list_divition.append(str(dv).lower().capitalize())
        else:
            list_divition.append(dv)
    df['División'] = list_divition
    return df


def format_percentage(value):
    if isinstance(value, float):
        value = np.floor(value*10)/10
        value = int(value)
    value = str(value) + "%"
    return value



def format(df):
  for col in df:
    if col != 'División':
        list_val = []
        for row in df[col]:
            if isinstance(row, float) or isinstance(row, int):
                row = format_percentage(row)
                list_val.append(row)
            else:
                list_val.append(row)
        df[col] = list_val