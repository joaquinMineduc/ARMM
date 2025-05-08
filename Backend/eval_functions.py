from principal_functions import *

date_document = get_date()

# =============== Tratamiento DF regional ==================================
df_regional = create_dataframe("APP/Backend/Input/Sigemet/eval.xls",
                            'Evaluación Interna por Región', 2)

df_regional = drop_unless_columns(df_regional, 1, 7, None)

df_regional = drop_unless_rows(df_regional, None, None, 16)
print(df_regional)

df_regional = classify_reg(df_regional)

format_eval_columns(df_regional)

print(df_regional)

# ================= Tratamiento DF NC =======================================
df_NC = create_dataframe('APP/Backend/Input/Sigemet/eval.xls',
                         'Evaluación Interna por División', 3)

df_NC = drop_unless_columns(df_NC, 1, 7, None)

# Particion de del dataframe NC
df_NC_part1 = partioner(df_NC, 0, 4)
df_NC_part2 = partioner(df_NC, 4, 6) 
df_NC_part3 = partioner(df_NC, 6, 7) 
df_NC_part4 = partioner(df_NC, 7, 8)


# =========== Tratamiento DF Evaluación proveedor interna de NC por variable ===================

df_NC2 = create_dataframe('APP/Backend/Input/Sigemet\eval.xls',
                          'Eval. interna por variable', 2)

"""df_NC2 = drop_unless_columns(df_NC2, 2, 12, None) # Se elimina antes para evitar el resize de los index
df_NC2 = drop_unless_columns(df_NC2, None, None, 0) # Se elimina porque este valor esta intercalado, es necesario eliminar por separado
"""

# Se realiza una query para excluir todos los indicadores PTR
df_NC2 = df_NC2.query("not Variable.str.contains('PTR')")

df_NC3 = pd.DataFrame()

for cr in ['CNT','RECFIN','SUBV','URAE','AUDITORIA',
    'ESTUDIOS','SEJEC_TP','AYUMIN','INNOV','GABSUB']:
    df_NC2_temp = create_simple_query(df_NC2, 'Lugar de medición', cr
        ,['Lugar de medición','Responsable','N° Variables',
        'Oportunidad','Consistencia','Completitud'])
    
    df_NC2_temp = modify_eval_values(df_NC2_temp)

    df_NC3 = pd.concat([df_NC3, df_NC2_temp], axis = 0)
    
df_NC3 = df_NC3.groupby(by=['Lugar de medición','Responsable'], as_index = False).mean()
df_NC3.drop(['Responsable','N° Variables'], inplace=True, axis=1)

df_NC3 = df_NC3.groupby(by=['Lugar de medición'], as_index = False).mean()


df_NC3.loc[:,'Promedio']= np.mean(df_NC3[['Consistencia','Oportunidad','Completitud']].values, axis = 1)

df_NC3 = df_NC3[order_partioner]
df_NC3.columns = df_NC_columns

df_NC3 = format_divition(df_NC3)


df_diplap = pd.DataFrame()
df_gabmin = pd.DataFrame()
df_gabsub = pd.DataFrame()

for row in df_NC3.itertuples(index=True):
    if row[1] in ["CNT",'Recursos Financieros','Subvenciones','URAE']:
        df_temp = partioner(df_NC3, row[0], row[0] + 1)
        df_diplap = pd.concat([df_diplap, df_temp ], axis = 0)
    if row[1] in ["Auditoria",'Estudios']:
        df_temp = partioner(df_NC3, row[0], row[0] + 1)
        df_gabmin = pd.concat([df_gabmin, df_temp ], axis = 0)
    if row[1] in ["Ayuda Mineduc",'Innovación','Gabinete Subsecretaría','TP']:
        df_temp = partioner(df_NC3, row[0], row[0] + 1)
        df_gabsub = pd.concat([df_gabsub, df_temp ], axis = 0)


# Concatenación de todos los df
df_eval_NC = pd.concat([df_NC_part1, df_diplap, df_NC_part2, 
    df_gabmin, df_NC_part3, df_gabsub, df_NC_part4], axis = 0)


format(df_eval_NC)

print(df_eval_NC)

df_eval_NC.to_excel("Eval. internal.xlsx", index = False)

