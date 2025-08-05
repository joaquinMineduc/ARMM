from principal_functions import *
from analisis_datos import clear_df_data_analisis

date_document = get_date()

CR_2 = ['Gabinete Ministerio','Gabinete Subsecretaría','CPEIP','DEG',
        'División de Planificación y Presupuesto','DAG','UCE','División Jurídica']

def create_df_NC():
        df = clear_df_data_analisis()
        df_status_nc = pd.DataFrame()
        for index, CR in enumerate(CR_2):
                df_status = create_query(df,['CR.2', 'Nivel', 'tag_ponderado', 'Tipo'],
                                [CR,'NC','NO','Riesgos'], ['and', 'and','and', 'and'], ['==','==','==','!='],
                                ['CR.2','Tipo','Nombre del Indicador','Riesgo (Alto - Medio- Bajo) periodo','Cod_Sigemet'])
                if index == 0:        
                        df_status_NC = pd.concat([df_status_nc, df_status])
                else:
                        df_status_NC = pd.concat([df_status_NC, df_status])
        return df_status_NC
                