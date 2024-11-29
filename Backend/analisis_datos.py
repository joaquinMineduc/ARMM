from analitics_class import *

YEAR = get_this_year()


# Creación del data frame
df = create_dataFrame('ARMM/Backend/Input/indicadores.xls')

# Se claisifcan indicadores ponderados
df = add_clasificator_ponderation(df)

df = add_split_indicador(df,'Indicador')

df = add_split_meta_periodo(df,'Período Meta')

df = add_classificator_type(df, 'Instrumento')

df = add_classificator_CR2(df, 'Centro Responsabilidad')


df = add_new_column(df, [f'Numerador {str(YEAR)}',
                         f'Denominador {str(YEAR)}',
                         'Variacion Periodo',
                         'CR inf',
                         'Nombre medios de verificación',
                         'Cumplimiento c/r a meta anual'])

df = add_order_CR(df, 'CR.2')

df = add_cr(df, 'CR.2')
print(df)

df = concat_column_by_args(df,['Cod_Sigemet','CR.2'],'-','Variable')

df = add_level(df, 'CR')

df = add_risk_as_binary(df, 'Nivel Riesgo')

df = rename_columns(df)

df = split_formula(df, 'Formula Aplicada')

df = add_weighthing(df, 'Cod_Sigemet','CR.2')
df = change_errors(df)
df = drop_unless_columns(df)
df = order_df(df)

create_informe_BI(df)










