import pandas as pd
from datetime import datetime
import numpy as np
from static_data import *
from helper_functions import *
import locale



# Configuración del idioma del entorno local, se cambia de EN a ES
try:
    # Esto funciona en la mayoría de los sistemas operativos
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para Windows
    

# Aplicar multiproceso para mejorar rendimiento : PENDIENTE 
def create_dataframe(location, sheet = None, header = None):
    if sheet is None and header is None: 
        df = pd.read_excel(location, header = 0) # Si hoja y header no están definidos

    if sheet is None and header is not None: 
        df = pd.read_excel(location, header = header)# Si sólo se tiene header
    else:
        df = pd.read_excel(location, sheet, header = header)# Si se encuentran todos los argumentos
    return df


# Eliminar columnas innecesarias
def drop_unless_columns(df, start, end, columns):
    list_index = list(df.columns)
    if start is None and end is None and columns is None: # si no se ingresa un inicio y termino y columna
        for index in drop_index: 
            df.drop(list_index[index], axis = 1, inplace = True) # elimina en base a una lsita predefinida
    if start is None and end is None and columns is not None:
        if isinstance(columns, list): # si la columna existe y el resto no, procede a eliminar
            for index in columns: # las columnas en base a la lsita creada
                df.drop(list_index[index], axis = 1, inplace = True)
        else:
            df.drop(list_index[columns], axis = 1, inplace = True)
    if start is not None and end is not None and columns is  None:
        for index in range(start, end): # elimina listas desde un rango y no desde una lista.
            df.drop(list_index[index], axis = 1, inplace = True)
    return df


# Eliminar filas innecesarias
def drop_unless_rows(df, start, end, rows):
    if start is None and end is None:
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
def create_an_copy(df, columns = None):
    if columns:
        if isinstance(columns, list):
            df_copy = df[columns].copy() # Se copian todas las columnas
        else:
            df_copy = df[columns].copy() # Se copia  sólo 1 columna del df original   
    else:
        df_copy = df.copy()
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
            lambda x: format_percentage(x))
            
            
# Funcion que crea una particion de un DF usando ILOC, esta f(x) recibe un rango para filtrar las columnas
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
def create_complex_query(df, arg):
    df = df.query(f"`Lugar de medición` == 'GABSUB' and Variable.str.startswith('{arg}')").reset_index(drop=True)
    return df


# una funcion que ejecuta una query simple
def create_simple_query(df, column, arg_compare, filter = None):
    if filter:
        if isinstance(arg_compare, int):
            df = df.query(f"`{column}` == {arg_compare}")[filter]
        else:
            df = df.query(f"`{column}` == '{arg_compare}'")[filter]
    else:
        if isinstance(arg_compare, int):
            df = df.query(f"`{column}` == {arg_compare}")
        else:
            df = df.query(f"`{column}` == '{arg_compare}'")
    return df


def build_query( columns, list_args, list_operator, list_logic):
    space = " "
    query_str = ""
    # Iterar sobre las columnas y los argumentos
    for index, (col, arg, op, log) in enumerate(zip(columns, list_args, list_operator, list_logic)):
        # Construir la condición
        query_str += f'`{col}`' + space + f'{log}' + space + f'"{arg}"'
        print(query_str)
        # Añadir el operador lógico solo si no es la última iteración
        if index  < len(columns) - 1:
          query_str += space + list_operator[index] + space
    return query_str


# Nuevo inspeccionar
def create_query(df, columns, list_args, list_operator, list_logic = None, columns_filter = None):
    str_query = build_query(columns, list_args, list_operator, list_logic)
    df = df.query(str_query)
    if columns_filter:
        df = df.query(str_query)[columns_filter]
    return df


def modify_eval_values(df):
    df['Oportunidad'] = df['Oportunidad'].apply(lambda op: 100 if op == 'Si' else 0)
    df['Consistencia'] = df['Consistencia'].apply(lambda op: 100 if op == 'Si' else 0)
    df['Completitud'] = df['Completitud'].apply(lambda op: 100 if op == 'Si' else 0)
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
        elif dv == 'GABSUB':
            list_divition.append('Gabinete Subsecretaría')
        elif dv == 'SEGI':
            list_divition.append("Seguridad de la Información")
        elif dv == 'GAB_DIPLAP':
            list_divition.append("Gabinete DIPLAP")
        else:
            list_divition.append(dv)
    df['División'] = list_divition
    return df


def format_percentage(value):
    """
    Convierte un número a un porcentaje formateado como cadena.
    
    Si el valor es un float entre 0 y 1, se interpreta como una fracción y se multiplica por 100.
    Luego el valor se redondea al entero más cercano y se añade el símbolo '%'.

    Parámetros:
    ----------
    value : int o float
        Número a convertir a porcentaje. Puede ser una fracción (0 < value < 1) o un porcentaje directo.

    Retorna:
    --------
    str
        Cadena con el valor porcentual redondeado y el símbolo '%'.

    Ejemplos:
    ---------
    >>> format_percentage(0.457)
    '46%'
    >>> format_percentage(45.7)
    '46%'
    >>> format_percentage(100)
    '100%'
    """
    if isinstance(value, float) and 0 < value < 1:
        value = value*100
    value = round(value)
    return f"{value}%"


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
     
        
# Funcion para eliminar columnas como filas (funcion reutilizable)
def drop_columns_as_list(df, lista):
  for col in lista:
    df.drop(col, axis=1)
  return df


# FUncion para detectar si el dataframe no contiene filas especificas( ver si se puede reutilizar)
def detector_less_columns(df, arg_rows):
    columns = df['Tipo'].tolist()
    for arg in arg_rows:
        if arg not in columns:
            df.loc[len(df)] = [arg,0,0,0]
    return df



# Funcion complemento a f(x) rename_columns
def validation_type(arg):
    return isinstance(arg, str)
    

# funcion que agrupa por tipo  indicador
def group_by_columns(df, columns, arg = None):
    if arg:  
        if arg == 1:
            df = df.groupby(by=columns, as_index = False).sum()
        elif arg == 2:
            if isinstance(columns, list):
                df = df.groupby(by=columns, as_index = False).mean(numeric_only=True)
            else:
                df = df.groupby(by=[columns], as_index = False).mean(numeric_only=True)
    else:
        if isinstance(columns, list):
            df = df.groupby(by=columns, as_index = False).count()
        else:
            df = df.groupby(by=[columns], as_index = False).count()
    return df


# Modificación y optimización de la funcion rename (Reutilizable)
def rename_columns(df, origin_columns, new_name_columns):
    if (validation_type(origin_columns) and validation_type(new_name_columns)):
        df.rename(columns = {origin_columns:new_name_columns}, inplace = True)      
    else:
        for origin, new in zip(origin_columns, new_name_columns):
            df.rename(columns = {origin:new}, inplace = True)    
    return df


def create_group_risk(df, list_order_type, new_columns):
    df = group_by_columns(df, 'Tipo')
    df = detector_less_columns(df, list_order_type )
    df = rename_columns(df, 'Tipo Riesgo', new_columns)
    df = df.sort_values(by='Tipo')
    df = df.reset_index(drop=True)
    df = df[[f'{new_columns}']]
    return df 

   
def cut_cr(df):
    list_update_cr = []
    CR = df['CR.2'].tolist()
    for cr in CR:
        if cr == 'División Jurídica':
            list_update_cr.append('Jurídica')
        elif cr == 'División de Planificación y Presupuesto':
            list_update_cr.append('DIPLAP')
        elif cr == "Gabinete Subsecretaría":
            list_update_cr.append('Gab Subse')
        elif cr == "Gabinete Ministerio":
            list_update_cr.append('Gab Ministro')
        else:
            list_update_cr.append(cr)
    df['CR.2'] = list_update_cr
    return df


def last_bussines_day(month, year, holy_days = None):
    # Último día del mes
    last_day = pd.Timestamp(year, month, 1) + pd.offsets.MonthEnd(0)

    # Retrocede hasta el día hábil más cercano
    while last_day.weekday() >= 5 or (holy_days and last_day in holy_days):
        last_day -= pd.Timedelta(days=1)
    return last_day.day


def order_reg_by_columns(df, column):
    df = df.copy()
    df.sort_values(by = column, inplace = True)
    return df

# realizar validacion de año según cierre, si es enero debe tomar mes anterior y año anterior

def get_date(format=None, text=None, Format2=None):
    today = datetime.now()
    month = today.month - 1

    if month == 0:
        month = 12
        year = today.year - 1
    else:
        year = today.year

    # Convertimos el número del mes a nombre del mes en inglés
    month_name = datetime(year, month, 1).strftime("%B").upper()

    day = today.day

    if format:
        return f'Acum {month_name} - {year}'

    if text and format is None:
        last_day = last_bussines_day(month, year)
        return f'{text} {last_day} de {month_name}'

    if Format2 and text is not None:
        return f'{text} {year}'

    return f'{month_name} - {year}'

       
def clear_df(df):
    df.dropna(inplace = True)
    return df

# AGREGAR promedio para terminar
def build_df_eval_prov(df_div, df_sub_div = None):
    # ----- Se hace transformación del DF de división --
    df_div = group_by_columns(df_div, 'División', 2)
    if df_sub_div is not None:
        df_sub_div = group_by_columns(df_sub_div, 'Lugar de medición', 2)
        df_sub_div.columns = df_div.columns
        df_unificated = pd.concat([df_div, df_sub_div])
        return df_unificated
    return df_div

