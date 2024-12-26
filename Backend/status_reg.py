from principal_functions import *
from analisis_datos import df

columns = ['I23_014', 'I16_066', 'I24_12_', 'I16_056']

for index, cod in enumerate(columns):
    if index < 1:
        df_status_REG = pd.DataFrame()  
    df_status = create_query(df,['Cod_Sigemet', 'Nivel', 'tag_ponderado'],
                            [cod, 'Regiones', 'NO'],['and', 'and'], 
                            ['Cod_Sigemet', 'Variable', 'CR', 'Riesgo (Alto - Medio- Bajo) periodo'])
    if index == 1:
        df_status.loc[len(df_status)] = ["I16_066","I16_066-SECREDUC 13",'Metropolitana','No aplica']
        df_status.loc[len(df_status)] = ["I16_066","I16_066-SECREDUC 16","Ñuble","No aplica"]
    df_status = order_reg_by_columns(df_status, 'Variable')
    df_status_REG = pd.concat([df_status_REG, df_status])
    
    if index == 2:
        df_status = df.query("Cod_Sigemet.str.contains('I24_12_')" + 
                             "and `Nivel` == 'Regiones'" + 
                             "and `tag_ponderado` =='NO'")[['Cod_Sigemet', 
                                                            'Variable','CR', 
                                                            'Riesgo (Alto - Medio- Bajo) periodo']]
        df_status = order_reg_by_columns(df_status, 'Variable')
        df_status_REG = pd.concat([df_status_REG, df_status])
  
   
        
        

    


    
                     
 

        
   

            

                