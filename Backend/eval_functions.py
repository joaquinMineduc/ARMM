from principal_functions import *

date_document = get_date()

# =============== Tratamiento DF regional ==================================
df_regional = create_dataframe("APP/Backend/Input/Sigemet/eval.xls",
    'Evaluación Interna por Región', 2)

df_regional = drop_unless_columns(df_regional, 1, 7, None)

df_regional = drop_unless_rows(df_regional, None, None, 16)

df_regional = classify_reg(df_regional)

format_eval_columns(df_regional)

# ================= Tratamiento DF NC =======================================
df_NC = create_dataframe('APP/Backend/Input/Sigemet/eval.xls',
    'Eval. interna por variable', 2)

df_NC = df_NC.query("not Variable.str.contains('PTR')").copy()

# =========== Tratamiento DF Evaluación proveedor interna de NC por variable ===================
df_eval_NC = pd.DataFrame()
for cr in cr_eval:
    if cr in ['DIPLAP', 'GABMIN', 'GABSUB']:
        df_temp = create_simple_query(df_NC, 'División', cr, ['División','Lugar de medición',
            'Oportunidad','Consistencia','Completitud'])
        df_temp = modify_eval_values(df_temp)
        df_temp = group_by_columns(df_temp, ['División','Lugar de medición'], 2)
        df_temp.loc[:,"Cumpl. Promedio"] = np.mean(df_temp[['Oportunidad',
        'Consistencia','Completitud']].values, axis = 1)
        df_sub_temp = df_temp.copy()
        df_unificated = build_df_eval_prov(df_temp, df_sub_temp)
        df_eval_NC = pd.concat([df_eval_NC, df_unificated], axis = 0)
    else:
        df_temp = create_simple_query(df_NC, 'División', cr, ['División','Lugar de medición',
            'Oportunidad','Consistencia','Completitud'])
        df_temp = modify_eval_values(df_temp)
        df_temp = group_by_columns(df_temp, ['División','Lugar de medición'], 2)
        df_temp.loc[:,"Cumpl. Promedio"] = np.mean(df_temp[['Oportunidad',
        'Consistencia','Completitud']].values, axis = 1)
        df_unificated = build_df_eval_prov(df_temp)
        df_eval_NC = pd.concat([df_eval_NC, df_unificated], axis = 0)

df_eval_NC = df_eval_NC[df_NC_columns]
 
df_eval_NC = format_divition(df_eval_NC)

format(df_eval_NC)

df_eval_NC.to_excel("Eval. internal.xlsx", index = False)



def eval_ptr():
    # ===== Creación de dataframe para evaluación proveedores indicadores PTR ============
    df_NC_ptr = create_dataframe('APP/Backend/Input/Sigemet/eval.xls',
        'Eval. interna por variable', 2)

    df_NC_ptr = df_NC_ptr.query("Responsable.str.contains('PTR')").copy()

    # =========== Tratamiento DF Evaluación proveedor interna de NC por variable para indicadores PTR ===================
    df_eval_NC_ptr = pd.DataFrame()

    for cr in cr_eval:
        if cr in ['DIPLAP', 'GABMIN', 'GABSUB']:
            df_temp = create_simple_query(df_NC_ptr, 'División', cr, ['División','Lugar de medición',
                'Oportunidad','Consistencia','Completitud'])
            df_temp = modify_eval_values(df_temp)
            df_temp = group_by_columns(df_temp, ['División','Lugar de medición'], 2)
            df_temp.loc[:,"Cumpl. Promedio"] = np.mean(df_temp[['Oportunidad',
            'Consistencia','Completitud']].values, axis = 1)
            df_sub_temp = df_temp.copy()
            df_unificated = build_df_eval_prov(df_temp, df_sub_temp)
            df_eval_NC_ptr = pd.concat([df_eval_NC_ptr, df_unificated], axis = 0)
        else:
            df_temp = create_simple_query(df_NC_ptr, 'División', cr, ['División','Lugar de medición',
                'Oportunidad','Consistencia','Completitud'])
            df_temp = modify_eval_values(df_temp)
            df_temp = group_by_columns(df_temp, ['División','Lugar de medición'], 2)
            df_temp.loc[:,"Cumpl. Promedio"] = np.mean(df_temp[['Oportunidad',
            'Consistencia','Completitud']].values, axis = 1)
            df_unificated = build_df_eval_prov(df_temp)
            df_eval_NC_ptr = pd.concat([df_eval_NC_ptr, df_unificated], axis = 0)
            
    df_eval_NC_ptr = df_eval_NC_ptr[df_NC_columns] 
    df_eval_NC_ptr = format_divition(df_eval_NC_ptr)
    format(df_eval_NC_ptr)
    
    return df_eval_NC_ptr
        

