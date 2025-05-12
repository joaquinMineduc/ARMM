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
df_NC_query = create_dataframe('APP/Backend/Input/Sigemet/eval.xls',
    'Eval. interna por variable', 2)

df_NC_query = df_NC_query.query("not Variable.str.contains('PTR')").copy()

# =========== Tratamiento DF Evaluación proveedor interna de NC por variable ===================
df_NC = pd.DataFrame()
for cr in cr_eval:
    if cr in ['DIPLAP', 'GABMIN', 'GABSUB']:
        df_temp = create_simple_query(df_NC_query, 'División', cr, ['División','Oportunidad',
            'Consistencia','Completitud'])
        df_sub_temp = create_simple_query(df_NC_query,'División', cr, 
            ['Lugar de medición','Oportunidad','Consistencia','Completitud'])
        df_unificated = build_df_eval_prov(df_temp, df_sub_temp)
        df_NC = pd.concat([df_NC, df_unificated], axis = 0)
    else:
        df_temp = create_simple_query(df_NC_query, 'División', cr, ['División','Oportunidad',
            'Consistencia','Completitud'])
        df_unificated = build_df_eval_prov(df_temp)
        df_NC = pd.concat([df_NC, df_unificated], axis = 0)
print(df_NC)
    
        
"""format(df_eval_NC)

print(df_eval_NC)

df_eval_NC.to_excel("Eval. internal.xlsx", index = False)
"""
