import pandas as pd
import numpy as np
import math as mat
from datetime import datetime
import locale
from static_data import *


# Configuración del idioma del entorno local, se cambia de EN a ES
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


def create_an_copy(df, columns):
    if isinstance(columns, list):
        df_copy = df[columns].copy()
    else:
        df_copy = df[columns].copy()
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
    df_filtrated = create_an_copy(df, columns)
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
    df_filtrated = create_an_copy(df, columns)
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
def add_classificator_type(df, columns):
    list_type = []
    df_filtrated = create_an_copy(df, columns)
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
    if CR in [f'R{num2}.EDUC - REG:{num}',f'R{num2}.GAB - REG:{num}',
              f'R{num2}.SUBV - REG:{num}',f'SECREDUC_{num} - REG:{num}']:
        return f"SECREDUC {num2}"
    else:
        return "format error"
    
 
       
def add_classificator_CR2(df, columns):
    lista_CR2 = []
    df_filtrated = create_an_copy(df, columns)
    shape = pd.DataFrame(df_filtrated).shape[1]
    if shape == 1:
        for x in df_filtrated:
            x = x.upper()
            if x in ['AUDITORIA - REG:99','ESTUDIOS - REG:99','GABMIN']:
                lista_CR2.append("Gabinete Ministerio")
            elif x in ['AYUMIN - REG:99','AYUMIN','GABSUB - REG:99',
                    'GABSUB','INNOV - REG:99','INNOV','SEJEC_TP']:
                lista_CR2.append("Gabinete Subsecretaría")
            elif x in ['CNT - REG:99','CNT','RECFIN - REG:99','SUBV - REG:99','URAE', 'DIPLAP', 'DPCG']:
                lista_CR2.append("División de Planificación y Presupuesto")
            elif x in ['C.AYC - REG:99','C.AYC','C.CONV', 'C.NORM - REG:99','C.NORM',
                       'C.PROC','C.SYJ - REG:99','JURID']:
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



# Funcion que permite clasificar CR por regiones
def classificator_by_reg(CR, arg):
    num_cr = CR.split(arg)
    num_cr = int(num_cr[1])
    for index, region in enumerate(regiones, start = 1):
        if index == num_cr:
            return region


        
# Agregar una nueva columna al DF con los Centros de responsabilidad en segundo nivel      
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
            list_CR.append(classificator_by_reg(CR, ' '))
    df.loc[:,'CR'] = list_CR
    return df



# Funcion que permite concatenar columnas, a través de un argumento intermedio
def concat_column_by_args(df, columns, arg, new_column):
    # Verificar si 'arg' es un delimitador o algo similar
    if arg:  # Si 'arg' tiene algún valor, asumimos que es un delimitador
        delimiter = arg
    else:
        delimiter = ''  # Si no, concatenamos sin delimitador
    
    # Inicializamos una lista para almacenar los valores concatenados
    concatenated_values = []
    
    # Iteramos sobre las filas del DataFrame
    for _, row in df.iterrows():
        # Concatenamos las columnas de la fila especificada en 'columns' con el delimitador
        concatenated_value = delimiter.join(str(row[col]) for col in columns)
        concatenated_values.append(concatenated_value)
    
    # Asignamos la lista de valores concatenados como la nueva columna
    df.loc[:,new_column] = concatenated_values
    return df



# Crea la columna nivel. Permite hacer la distinción entre indicadores de nivel central y las regiones
def add_level(df, column):
    list_level = []
    df_CR = create_an_copy(df, column)
    for CR in df_CR:
        if CR in ['UCE','DEG','DAG','JURIDICA','DIPLAP','GABINETE','CPEIP']:
            list_level.append("NC")
        else:
            list_level.append("Regiones")
    df.loc[:,'Nivel'] = list_level
    return df



# Agrega la columna como riesgo en binario
def add_risk_as_binary(df, column):
    list_type_risk = []
    count_low = []
    count_medium = []
    count_high = []
    df_risk = create_an_copy(df, column)
    for risk in df_risk:
        if risk == 'Bajo':
            list_type_risk.append(1)
            count_low.append(1)
            count_medium.append(0)
            count_high.append(0)
        elif risk == "Medio":
            list_type_risk.append(2)
            count_low.append(0)
            count_medium.append(1)
            count_high.append(0)
        elif risk == "Alto":
            list_type_risk.append(3)
            count_low.append(0)
            count_medium.append(0)
            count_high.append(1)
        else:
            list_type_risk.append("Sin dato")
            count_low.append(0)
            count_medium.append(0)
            count_high.append(0)
    df.loc[:, 'Tipo Riesgo'] = list_type_risk
    df.loc[:, 'Cantidad Riesgo Bajo'] = count_low
    df.loc[:, 'Cantidad Riesgo Medio'] = count_medium
    df.loc[:, 'Cantidad Riesgo Alto'] = count_high
    return df


# Refactorizar 
def rename_columns(df):
    df.rename(columns={"Observación": "Análisis Resultado periodo", 
                    "Riesgo": "Análisis DPCG","Nivel Riesgo": "Riesgo (Alto - Medio- Bajo) periodo",
                    "Fórmula de Cálculo": "Forma de Cálculo", "Meta del período": "Meta periodo", 
                    "% Avance": "Resultado periodo",
                    "% Cumplimiento efectivo meta anual": "Cumplimiento respecto a meta"},
                    inplace=True)
    return df


# Función que separa el denominador y numerador de la formula de calculo del indicador
def split_formula(df, column):
    list_numerator = []
    list_denominator = []
    df_formula = create_an_copy(df, column)
    for f in df_formula:
        formula = str(f).split("*")[0]
        formula = formula.replace("(","").replace(")","")
        formula = formula.split("/")
        if len(formula) == 2:
            numerador = formula[0]
            denominador = formula[1]
            list_numerator.append(numerador)
            list_denominator.append(denominador)
            numerador = numerador.split(" ")
        elif len(formula) == 1:
            numerador = formula[0].split(" ")
            list_denominator.append("no aplica")
            if len(numerador) == 6:
                numerador = numerador[5]
                list_numerator.append(numerador)
            elif len(numerador) == 2:
                numerador = numerador[1]
                list_numerator.append(numerador)
            else:
                numerador = numerador[0]
                list_numerator.append(numerador)

    df.loc[:,'numerador'] = list_numerator
    df.loc[:,'denominador'] = list_denominator
    return df


# Aplica filtro para filtrar todos los indicadores que son podnerados del df
def query_ponderation(df):
    df_informe = df.query("tag_ponderado == 'NO'")
    return df_informe

    
# Añade la columna ponderación al DF
def add_weighthing(df, column):
    list_weighthing = []
    df_weighthing = create_an_copy(df, column)
    for cod, CR in zip(df_weighthing['Cod_Sigemet'], df_weighthing['CR.2']):
        if cod in Group_5:
            list_weighthing.append("5,0%")
        elif cod in Group_10:
            list_weighthing.append("10,0%")
        elif cod in Group_13:
            list_weighthing.append("13,0%")
        elif cod in Group_14:
            list_weighthing.append("14,0%")
        elif cod in Group_15:
            list_weighthing.append("15,0%")
        elif cod in Group_16:
            list_weighthing.append("16,0%")
        elif cod in Group_17:
            list_weighthing.append("17,0%")
        elif cod in Group_18:
            list_weighthing.append("18,0%")
        elif cod in Group_23:
            list_weighthing.append("23,0%")
        elif cod in Group_27:
            list_weighthing.append("27,0%")
        elif cod in Group_30:
            list_weighthing.append("30,0%")
        elif cod in Group_33:
            list_weighthing.append("33,0%")
        elif cod in Group_34 and CR in ['SECREDUC 13','SECREDUC 16']:
            list_weighthing.append("34,0%")
        elif cod in Grupo_35:
            list_weighthing.append("35,0%")
        elif cod in Group_40:
            list_weighthing.append("40,0%")
        else:
            list_weighthing.append("25,0%")
    df.loc[:,'Ponderación'] = list_weighthing
    return df



def change_errors(df):
    filtered_df = df.query("Cod_Sigemet == 'I16_062'")
    df.loc[filtered_df.index, 'Tipo'] = "H"
    return df




# Se utiliza column_order desde datos estáticos
def order_df(df):
    df = df[column_orden]
    df = df.fillna("Sin dato")
    return df

  
# Refactorizar
def format_informe_mensual(df):
    df_informe = create_an_copy(df, columns_informe)
    df_informe.rename(columns={"Meta anual": "Meta","numerador": "Numerador",
                           "denominador": "Denominador",
                           "Riesgo (Alto - Medio- Bajo) periodo":"Nivel riesgo",
                           "Análisis DPCG":"Análisis"}, inplace= True)
    
    # se trunca a la decima el cumplimiento respecto a la meta
    df_informe.loc[:,"Cumplimiento respecto a meta"] = df_informe["Cumplimiento respecto a meta"].apply(
    lambda x: np.floor(x*10)/10)
    
    # cambio de tipo de datos, para ingresar miselaneo de tipos
    df_informe['Meta'] = df_informe['Meta'].astype("object") 
    df_informe['Resultado periodo'] = df_informe['Resultado periodo'].astype("object")
    return df_informe


def format_variable(df_informe):
    list_goal = []
    list_result = []
    for d, m, r, ind in zip(df_informe['Denominador'], df_informe['Meta'], 
        df_informe['Resultado periodo'], df_informe['Nombre del Indicador']):
        
        if d == "no aplica":
            list_goal.append(int(m))
            list_result.append(int(r))
        elif ind == ' Transformación Digital':
            list_goal.append(str("Solo medir"))
            list_result.append(int(r))
        else:
            list_goal.append(str(m).replace(".",",") + "%")
            r = mat.trunc(r*10)/10
            list_result.append(str(r).replace(".",",") + "%")
    df_informe.loc[:,"Meta"] = list_goal
    df_informe.loc[:,"Resultado periodo"] = list_result
    df_informe.loc[:,"Cumplimiento respecto a meta"] = df_informe["Cumplimiento respecto a meta"].apply(
    lambda x: str(x).replace(".",",")+ "%" )
    return df_informe


#Funcion entrega formato del periodo
def get_period_format():
    month = datetime.now().month
    date = datetime(2024, month -1, 1)
    mes = date.strftime("%B")
    return mes

    
# Funcion para crear el informe BI
def create_informe_BI(df):
    mes = get_period_format()
    df.to_excel(f"datosBI_{mes}.xlsx", index = False)


# Función crear informe mensual
def create_informe_mensual(df_informe):
    mes = get_period_format()
    df_informe.to_excel(f"informe_{mes}.xlsx", index = False)
    



