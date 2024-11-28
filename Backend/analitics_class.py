import pandas as pd
import numpy as np
import math as mat
from datetime import datetime
import locale
from datos_estaticos import *


# Configura el idioma a español
try:
    # Esto funciona en la mayoría de los sistemas operativos
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para Windows


def get_this_year():
    year = datetime.now().year
    return year

def create_dataFrame(location):
    df = pd.read_excel(location, header = 1)
    return df


def create_an_copy(df, columns, columns_2 = None):
    df_copy = df[columns].copy()
    if columns_2 is not None:
        df_copy2 = df[columns_2].copy()
        df_copy = pd.concat([df_copy, df_copy2], axis = 1)
    return df_copy


def add_clasificator_ponderation(df):
    # Este código crea una clasificación entre indicadores ponderados y normales.
    df['tag_ponderado'] = df.apply(lambda row: 'SI' if pd.isna
                            (row['Instrumento']) else 'NO', axis = 1)
    return df


# Esta f(x) divide la columnas indicador en, codigo indicador y su nombre.
def add_split_indicador(df, columns, columns_2 = None):
    list_x = []
    list_y = []
    df_filtrated = create_an_copy(df, columns, columns_2)
    shape = pd.DataFrame(df_filtrated).shape[1]
    if shape == 1:
        for x in df_filtrated:
            parts = x.split(']')
            x = parts[0]
            y = parts[1]
            x = x.replace('[','')
            list_x.append(x)
            list_y.append(y)
    df.loc[:,'Cod_Sigemet'] = list_x
    df.loc[:,'Nombre del Indicador'] = list_y
    return df


# Esta funcion divide las columnas de meta periodo en mes, año y orden del período
def add_split_meta_periodo(df, columns, columns_2 = None):
    list_period = []
    list_order_period = []
    list_year = []
    df_filtrated = create_an_copy(df, columns, columns_2)
    shape = pd.DataFrame(df_filtrated).shape[1]
    if shape == 1:
        for x in df_filtrated:
            parts = x.split('-')
            Anio = parts[0]
            periodo = parts[1]
            list_order_period.append(int(periodo))
            periodo = format_periodo(int(periodo))
            list_period.append(periodo)
            list_year.append(Anio)
        df.loc[:,'Mes Periodo'] = list_period
        df.loc[:,'Año Periodo'] = list_year
        df.loc[:,'Ordenperiodo'] = list_order_period
    return df


# Entrega el periodo en formato String
def format_periodo(periodo):
    date = datetime(2024, periodo, 1)
    mes = date.strftime("%B")
    return mes


# Este código 
def add_classificator_type(df, columns, columns_2 = None):
    list_type = []
    df_filtrated = create_an_copy(df, columns, columns_2)
    shape = pd.DataFrame(df_filtrated).shape[1]
    if shape == 1:
        for t in df_filtrated:
            match t:
                case "Convenio de Desempeño Colectivo":
                    list_type.append("CDC")
                case "PMG":
                    list_type.append(t)
                case "Formulario H":
                    list_type.append("H")
                case "Transversal":
                    list_type.append("PMG")
                case _:
                    list_type.append("")
        df.loc[:,'Tipo'] = list_type
    return df


def classificator_CR_REG(CR):
    CR = str(CR).upper()
    num = CR.split(":")
    num = int(num[1])
    num2 = num if num >= 10 else f'0{num}'
    if CR in [f'R{num2}.EDUC - REG:{num}',f'R{num2}.GAB - REG:{num}',f'R{num2}.SUBV - REG:{num}',f'SECREDUC_{num} - REG:{num}']:
        return f"SECREDUC {num2}"
    else:
        return "format error"
    
       
def add_classificator_CR2(df, columns, columns_2 = None):
    lista_CR2 = []
    df_filtrated = create_an_copy(df, columns, columns_2)
    shape = pd.DataFrame(df_filtrated).shape[1]
    if shape == 1:
        for x in df_filtrated:
            x = x.upper()
            if x in ['AUDITORIA - REG:99','ESTUDIOS - REG:99','GABMIN']:
                lista_CR2.append("Gabinete Ministerio")
            elif x in ['AYUMIN - REG:99','AYUMIN','GABSUB - REG:99','GABSUB','INNOV - REG:99','INNOV','SEJEC_TP']:
                lista_CR2.append("Gabinete Subsecretaría")
            elif x in ['CNT - REG:99','CNT','RECFIN - REG:99','SUBV - REG:99','URAE', 'DIPLAP', 'DPCG']:
                lista_CR2.append("División de Planificación y Presupuesto")
            elif x in ['C.AYC - REG:99','C.AYC','C.CONV', 'C.NORM - REG:99','C.NORM','C.PROC','C.SYJ - REG:99', 'JURID']:
                lista_CR2.append("División Jurídica")
            elif x in ['FCONT','FID','LDP','CPEIP']:
                lista_CR2.append("CPEIP")
            elif x in ['COMPRAS','GC - REG:99','GDP - REG:99','DAG', 'BIE - REG:99']:
                lista_CR2.append("DAG")
            elif x in ['SEP','EPJA - REG:99','EPJA', 'DEG']:
                lista_CR2.append("DEG")
            elif x in ['CRA - REG:99','CURRIC - REG:99','TE - REG:99', 'UCE - REG:99', 'UCE']:
                lista_CR2.append("UCE")
            else:
                lista_CR2.append(classificator_CR_REG(x))
    df.loc[:,'CR.2'] = lista_CR2
    return df


def add_new_column(df, add_columns):
    for column in add_columns:
        df.loc[:,column] = ""
    return df


def get_order_cr(CR, df_cr2):
    df_cr2 = df_cr2.drop_duplicates()
    df_cr2.index = indexs
    df_cr2.sort_index(inplace = True)
    for index, cr in enumerate(df_cr2, start = 1):
        if CR == cr:
            return index
        
        
def add_order_CR(df, column):
    list_order_CR = []
    df_cr2 = create_an_copy(df, column)
    for cr in df_cr2:
        list_order_CR.append(get_order_cr(cr, df_cr2))
    df.loc[:,'ORDENCR'] = list_order_CR
    return df


def classificator_by_CR(CR):
    num_cr = CR.split(" ")
    num_cr = int(num_cr[1])
    for index, region in enumerate(regiones, start = 1):
        if index == num_cr:
            return region
        
        
def add_cr(df, column):
    list_CR = []
    df_cr2 = create_an_copy(df, column)
    for CR in df_cr2:
        if CR in ['Gabinete Subsecretaría','Gabinete Ministerio']:
            list_CR.append("GABINETE")
        elif CR in ['División de Planificación y Presupuesto']:
            list_CR.append("DIPLAP")
        elif CR in ['División Jurídica']:
            list_CR.append("JURIDICA")
        elif CR in ['CPEIP','DAG','DEG','UCE']:
            list_CR.append(CR)
        else:
            list_CR.append(classificator_by_CR(CR))
    df.loc[:,'CR'] = list_CR