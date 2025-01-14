from principal_functions import *
from report_functions import *

DATE_REPORT = get_date()
YEAR_REPORT = DATE_REPORT[-4:]
 
# Creación del data frame
df = create_dataframe('APP/Backend/Input/Reports/indicadores.xls', None, 1)

# Se clasifcan indicadores ponderados
df = add_clasificator_ponderation(df)

df = add_split_indicador(df,'Indicador')
df = add_split_meta_periodo(df,'Período Meta')
df = add_classificator_type(df, 'Instrumento')
df = add_classificator_CR2(df, 'Centro Responsabilidad')

df = add_new_column(df, [f'Numerador {str(YEAR_REPORT)}',
                         f'Denominador {str(YEAR_REPORT)}',
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


# === Se Ordena el DF informe en base al formato requerido ======#
df_regiones = pd.DataFrame()
df_instrument = pd.DataFrame()
df_NC = pd.DataFrame()

for index, cr in enumerate(regiones):
   df_query = create_query(df_informe, ['Tipo','CR'], ['CDC',cr], ['and'])
   df_regiones = pd.concat([df_regiones, df_query])
print(df_regiones)

for index, ins in enumerate(['H','PMG']):
   df_query = create_query(df_informe, ['Tipo'], [ins], ['and'])
   df_instrument = pd.concat([df_instrument, df_query])
print(df_instrument)

for index, cr in enumerate(['CPEIP','DAG','DEG','DIPLAP','GABINETE','JURIDICA','UCE']):
   df_query = create_query(df_informe, ['Tipo','CR'], ['CDC',cr], ['and'])
   df_NC = pd.concat([df_NC, df_query])
print(df_NC)

df_informe = pd.concat([df_instrument, df_NC, df_regiones])
create_informe_mensual(df_informe)













