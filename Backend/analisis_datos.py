from principal_functions import *
from report_functions import *


YEAR = get_this_year()
 

# Creación del data frame
df = create_dataframe('Backend/Input/Reports/indicadores.xls', None, 1)

# Se clasifcan indicadores ponderados
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
df = concat_column_by_args(df, ['Cod_Sigemet','CR.2'], '-', 'Variable')
df = add_level(df, 'CR')
df = add_risk_as_binary(df, 'Nivel Riesgo')
df = rename_columns(df)
df = split_formula(df, 'Formula Aplicada')
df = add_weighthing(df, ['Cod_Sigemet','CR.2'])
df = change_errors(df)

# Se ramifica el data frame para filtrar todos los ponderados
df_informe = query_ponderation(df)
df = drop_unless_columns(df, None, None, None)
df = order_df(df)

create_informe_BI(df)

df_informe = format_informe_mensual(df_informe)
df_informe = format_variable(df_informe)

create_informe_mensual(df_informe)













