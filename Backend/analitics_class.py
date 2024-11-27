import pandas as pd
import numpy as np
import math as mat



def create_dataFrame(location):
    df = pd.read_excel(location, header = 1)
    return df

def create_an_copy(df, columns, columns_2 = None):
    df_copy = df[columns].copy()
    df_copy2 = df[columns_2].copy()
    df_copy = pd.concat([df_copy, df_copy2], axis = 1)
    return df_copy


def clasificator_by_ponderation(df):
    # Este código crea una clasificación entre indicadores ponderados y normales.
    df['tag_ponderado'] = df.apply(lambda row: 'SI' if pd.isna
                            (row['Instrumento']) else 'NO', axis = 1)
    return df
    

def split_column(df, columns, columns_2):
    list_code = []
    list_indicadores = []
    df_filtrated = create_an_copy(df, columns, columns_2)
    print(df_filtrated)
    for col in df_filtrated:
        col[df_filtrated]
        
        
        
        #code = parts[0]
        #nom_indicador = parts[1]
        #code = code.replace('[','')
        #list_code.append(code)
        #list_indicadores.append(nom_indicador)