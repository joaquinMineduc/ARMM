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
    'Eval. interna por variable', 2)


# =========== Tratamiento DF Evaluación proveedor interna de NC por variable ===================



"""format(df_eval_NC)

print(df_eval_NC)

df_eval_NC.to_excel("Eval. internal.xlsx", index = False)
"""
