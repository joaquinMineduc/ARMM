from principal_functions import *
from analisis_datos import df

list_new_type = []
all_columns = ['Tipo', 'Riesgo Bajo', 'Riesgo Medio', 'Riesgo Alto']
list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']
columns1 = ['Tipo','Tipo Riesgo','Nivel','tag_ponderado']
columns_filter = ['CR.2','Cantidad Riesgo Bajo','Cantidad Riesgo Medio','Cantidad Riesgo Alto']


#============= Tratamiento datos panel principal =================

panel_df = create_an_copy(df, columns1)
panel_df = create_simple_query(panel_df, "tag_ponderado",'NO')

for level, types in zip(panel_df['Nivel'],panel_df['Tipo']):
  if level == 'NC' and types == 'CDC':
    list_new_type.append('CDC NIVEL CENTRAL')
  elif level == 'Regiones' and types == 'CDC':
    list_new_type.append('CDC REGIONES')
  else:
    list_new_type.append(types)
    
panel_df['Tipo'] = list_new_type

df_low_risk = create_simple_query(panel_df, 'Tipo Riesgo', 1)

df_medium_risk = create_simple_query(panel_df, 'Tipo Riesgo', 2)

df_high_risk = create_simple_query(panel_df, 'Tipo Riesgo', 3)

df_low_risk = create_group_risk(df_low_risk, list_order_type, 'Riesgo Bajo')

df_medium_risk = create_group_risk(df_medium_risk, list_order_type, 'Riesgo Medio')

df_high_risk = create_group_risk(df_high_risk, list_order_type, 'Riesgo Alto')

df_types = pd.DataFrame(list_order_type, columns=['Tipo'])

# Se crea el dataframe que contiene la información final de los estados de indicadores por tipo
df_principal_panel = pd.concat([df_types, df_low_risk, df_medium_risk, df_high_risk], axis = 1)


#============= Creación data frame grafico PMG =================

df_grap_PMG = create_an_copy(df)
df_grap_PMG = create_simple_query(df_grap_PMG, 'Tipo','PMG', columns_filter)

# Argumento 1 agrega la funcion .sum() al termino de la agrupación para que sume los valores
# Si se el argumento "arg queda vacío agrupa y aplica de forma predetermianda la funcion .count()"
df_grap_PMG = group_by_columns(df_grap_PMG, 'CR.2', 1)
df_grap_PMG = cut_cr(df_grap_PMG)


#============= Creación data frame grafico H =================
df_grap_H = create_an_copy(df)
df_grap_H = create_simple_query(df_grap_H, 'Tipo','H', columns_filter)
df_grap_H = group_by_columns(df_grap_H, 'CR.2',1)
df_grap_H = cut_cr(df_grap_H)
print(df_grap_H)


#============= Creación data frame grafico CDC Nivel central =================
df_grap_CDC = create_an_copy(df)
df_grap_CDC = create_query(df_grap_CDC, ['Tipo', 'Nivel'], ['CDC', 'NC'], ['and'], columns_filter)
df_grap_CDC = group_by_columns(df_grap_CDC, 'CR.2', 1)
df_grap_CDC = cut_cr(df_grap_CDC)
print(df_grap_CDC)


#============ Creación data frame grafico CDC reg ==============
df_grap_reg = create_an_copy(df)
columns_filter.insert(0,'CR')
columns_filter.pop(1)
df_grap_reg = create_query(df_grap_reg, ['Tipo', 'Nivel'], ['CDC', 'Regiones'], ['and'], columns_filter)
df_grap_reg = group_by_columns(df_grap_reg, 'CR', 1)
print(df_grap_reg)