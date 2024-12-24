from principal_functions import *
from analisis_datos import df

CR_2 = ['Gabinete Ministerio','Gabinete Subsecretaría','CPEIP','DEG',
        'División de Planificación y Presupuesto','DAG','UCE','División Jurídica']
df_status_nc = pd.DataFrame()
for index, CR in enumerate(CR_2):
    df_status = create_query(df,['CR.2','Nivel', 'tag_ponderado'],
                          [CR_2[index],'NC','NO'],['and','and'], 
                          ['Variable','Riesgo (Alto - Medio- Bajo) periodo'])
    df_status_nc = pd.concat('', df_status)