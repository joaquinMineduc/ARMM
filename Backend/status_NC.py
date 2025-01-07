from principal_functions import *
from analisis_datos import df

date_document = get_date()

CR_2 = ['Gabinete Ministerio','Gabinete Subsecretaría','CPEIP','DEG',
        'División de Planificación y Presupuesto','DAG','UCE','División Jurídica']

for index, CR in enumerate(CR_2):       
        df_status = create_query(df,['CR.2','Nivel', 'tag_ponderado'],
                          [CR,'NC','NO'],['and','and'], 
                          ['Variable','Riesgo (Alto - Medio- Bajo) periodo'])
        if index < 1:
                df_status_nc = df_status             
                df_status_NC = pd.concat([df_status_nc, df_status])
        else:
             df_status_NC = pd.concat([df_status_NC, df_status])
                


