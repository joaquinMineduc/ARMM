from datetime import datetime

def get_year():
    today = datetime.today()
    month = today.month -1
    year = today.year
    if month == 0:
        year = year -1
    return year

YEAR = get_year()


regiones = [
    "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso",
    "O'Higgins", "Maule", "Biobío", "La Araucanía", "Los Lagos",
    "Aysén", "Magallanes", "Metropolitana", "Los Ríos",
    "Arica y Parinacota", "Ñuble"
]

cr_eval = ['CPEIP', 'DAG', 'DEG', 'DIPLAP', 'JURID', 'GABMIN', 'GABSUB', 'UCE']

df_NC_columns = ['División', 'Cumpl. Promedio', 'Oportunidad', 'Consistencia', 'Completitud']

order_columns_NC = ['Lugar de medición','Promedio','Oportunidad.1','Consistencia.1','Completitud.1']

order_partioner = ['Lugar de medición', 'Promedio', 'Oportunidad','Consistencia','Completitud']

# Se usa para crear el orden en la funcion order cr
indexs = [6,7,2,5,4,1,8,3,9,10,12,13,14,15,16,18,19,21,22,23,24,20,11,17,28]

drop_index = [0,1,2,3,5,6,7,8,10,12]

Group_10 = ['I21_011','I22_006','I21_012','I25_013']

Group_12 = ['I21_001']

Group_13 = ['I16_052','I24_004','I21_002']

Group_14 = ['I22_008']

Group_15 = ['I24_003','I23_007','I16_053','I24_011','I25_012']

Group_16 = ['I20_014','I16_054','I20_013','I25_005']

Group_17 = ['I20_011','I20_012','I16_043',
              'I19_012','I16_002','I19_026','I24_001','I24_002']

Group_20 = ['I23_015','I23_014','I16_056','I25_006','I16_066','I25_007'] # Todos los codigos de todas las regiones excepto 13 y 16

Group_25 = ['I16_062','I23_018','I25_010','I25_011','I20_005','I20_006',
            'I21_007','I25_004','I23_014','I16_056','I25_006','I25_007'] # Todos los codigos de regiones son de reg 13 y 16

Group_30 = ['I23_019','I25_001','I25_002','I24_009','I19_020']

Grupo_35 = ['I17_001','I23_004']

Group_40 = ['I25_003','I19_019']


column_orden = ['Cod_Sigemet','CR.2','Variable','Nivel','CR', 'CR inf','Tipo',
                'Nombre del Indicador','Forma de Cálculo','Ponderación',f'Numerador {YEAR}',
                f'Denominador {YEAR}','Meta anual','Mes Periodo','Año Periodo','numerador',
                'denominador','Meta periodo','Resultado periodo','Cumplimiento respecto a meta',
                'Variacion Periodo','Riesgo (Alto - Medio- Bajo) periodo','Tipo Riesgo',
                'Cantidad Riesgo Bajo','Cantidad Riesgo Medio', 'Cantidad Riesgo Alto',
                'Análisis Resultado periodo','Nombre medios de verificación', 'tag_ponderado',
                'Cumplimiento c/r a meta anual','Análisis DPCG', 'Ordenperiodo','ORDENCR']

columns_informe = ['CR','Tipo','Nombre del Indicador', 'Forma de Cálculo',
                 "Ponderación",'Meta anual','numerador','denominador','Resultado periodo',
                 'Riesgo (Alto - Medio- Bajo) periodo',"Tipo Riesgo",
                 'Cumplimiento respecto a meta','Análisis DPCG']