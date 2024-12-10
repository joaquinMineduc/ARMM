from principal_functions import *


# =============== Tratamiento DF regional ==================================
df_regional = create_dataframe("Backend/Input/Eval_internal/eval.xls",
                            'Evaluación Interna por Región', 2)

df_regional = drop_unless_columns(df_regional, 1, 7, None)

df_regional = drop_unless_rows(df_regional, None, None, 16)
print(df_regional)

df_regional = classify_reg(df_regional)

format_eval_columns(df_regional)

print(df_regional)

# ================= Tratamiento DF NC =======================================
df_NC = create_dataframe('Backend/Input/Eval_internal/eval.xls',
                         'Evaluación Interna por División', 3)

df_NC = drop_unless_columns(df_NC, 1, 7, None)

# Particion de del dataframe NC
df_NC_part1 = partioner(df_NC, 0, 4)
df_NC_part2 = partioner(df_NC, 4, 6) 
df_NC_part3 = partioner(df_NC, 6, 7) 
df_NC_part4 = partioner(df_NC, 7, 8)



# =========== Tratamiento DF NC por responsable ===================

df_NC2 = create_dataframe('Backend/Input/Eval_internal/eval.xls',
                          'Eval. interna por responsable', 3)

df_NC2 = drop_unless_columns(df_NC2, None, None, 0) # Se elimina porque este valor esta intercalado, es necesario eliminar por separado
df_NC2 = drop_unless_columns(df_NC2, 1, 12, None)

#Se particiona el dataframe eval interna por responsables
df_NC2_part1 = partioner(df_NC2, 3, 10)
df_NC2_part2 = partioner(df_NC2, 10, 13)
df_NC2_part3 = partioner(df_NC2, 13, 17)

print(df_NC2_part1)