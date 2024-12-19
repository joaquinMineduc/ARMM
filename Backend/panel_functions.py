from principal_functions import *
from analisis_datos import df

list_new_type = []
all_columns = ['Tipo', 'Riesgo Bajo', 'Riesgo Medio', 'Riesgo Alto']
list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']

#============= Tratamiento datos panel principal =================
columns = ['Tipo','Tipo Riesgo','Nivel','tag_ponderado']
panel_df = create_an_copy(df, columns)
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

df_low_risk = create_group_risk(df_low_risk, 'Riesgo Bajo', 'Tipo')

print(df_low_risk)