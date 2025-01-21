from datetime import datetime

YEAR = datetime.now().year -1

regiones = [
    "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso",
    "O'Higgins", "Maule", "Biobío", "La Araucanía", "Los Lagos",
    "Aysén", "Magallanes", "Metropolitana", "Los Ríos",
    "Arica y Parinacota", "Ñuble"
]

df_NC_columns = ['División', 'Cumpl. promedio', 'Oportunidad', 'Consistencia', 'Completitud']

order_columns_NC = ['Lugar de medición','Promedio','Oportunidad.1','Consistencia.1','Completitud.1']

NC_columns = ['Lugar de medición', 'promedio', 'Oportunidad','Consistencia','Completitud']

# Se usa para crear el orden en la funcion order cr
indexs = [6,7,2,5,4,1,8,3,9,10,12,13,14,15,16,18,19,21,22,23,24,20,11,17,28]

drop_index = [0,1,2,3,5,6,7,8,10,12]

Group_5 = ['I23_006']
Group_10 = ['I21_011','I22_006','I21_012']
Group_13 = ['I16_052','I24_004']
Group_14 = ['I22_008']
Group_15 = ['I24_003','I23_007','I16_053','I24_011']
Group_16 = ['I20_014','I24_010','I16_054','I20_013']

Group_17 = ['I19_012','I16_043','I20_012','I16_062',
          'I24_014','I19_026','I20_011','I23_018',
          'I24_001','I24_013','I24_015','I16_002','I24_002','I20_017']

Group_18 = ['I21_002']
Group_23 = ['I21_001']

Group_27 = ['I23_019','I23_015']

Group_30 = ['I19_020','I24_007','I24_009','I24_006']

Group_33 = ['I24_12_13','I24_12_16']

Group_34 = ['I16_056']

Grupo_35 = ['I17_001','I23_004']

Group_40 = ['I19_019','I24_008']


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