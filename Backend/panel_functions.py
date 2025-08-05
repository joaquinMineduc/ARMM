from principal_functions import *
from analisis_datos import clear_df_data_analisis



all_columns = ['Tipo', 'Riesgo Bajo', 'Riesgo Medio', 'Riesgo Alto']




def create_panel_df():
  list_new_type = []
  columns1 = ['Tipo','Tipo Riesgo','Nivel','tag_ponderado']
  #============= Tratamiento datos panel principal =================
  df = clear_df_data_analisis()
  panel_df = create_an_copy(df, columns1)
  panel_df = create_simple_query(panel_df, "tag_ponderado",'NO')

  """ Esta funcion se encarga de clasificar los indicadores 
  por su tipo y su origen, si es de nivel central o regional """
  for level, types in zip(panel_df['Nivel'], panel_df['Tipo']):
    if level == 'NC' and types == 'CDC':
      list_new_type.append('CDC NIVEL CENTRAL')
    elif level == 'Regiones' and types == 'CDC':
      list_new_type.append('CDC REGIONES')
    else:
      list_new_type.append(types)

  panel_df['Tipo'] = list_new_type
  return panel_df

# Estas funciones deben ser llamadas desde el manipulations_data.py
def create_df_low_risk():
  list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']
  panel_df = create_panel_df()
  df_low_risk = create_simple_query(panel_df, 'Tipo Riesgo', 1)
  df_low_risk = create_group_risk(df_low_risk, list_order_type, 'Riesgo Bajo')
  return df_low_risk
  
  
def create_df_medium_risk():
  list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']
  panel_df = create_panel_df()  
  df_medium_risk = create_simple_query(panel_df, 'Tipo Riesgo', 2)
  df_medium_risk = create_group_risk(df_medium_risk, list_order_type, 'Riesgo Medio')
  return df_medium_risk


def create_df_high_risk():
  list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']
  panel_df = create_panel_df()  
  df_high_risk = create_simple_query(panel_df, 'Tipo Riesgo', 3)
  df_high_risk = create_group_risk(df_high_risk, list_order_type, 'Riesgo Alto')
  return df_high_risk

def create_df_type_risk():
  list_order_type = ['CDC NIVEL CENTRAL','CDC REGIONES','H','PMG']
  df_low_risk = create_df_low_risk()
  df_medium_risk = create_df_medium_risk()
  df_high_risk = create_df_high_risk()
  df_types = pd.DataFrame(list_order_type, columns=['Tipo'])
  # Se crea el dataframe que contiene la información final de los estados de indicadores por tipo
  df_principal_panel = pd.concat([df_types, df_low_risk, df_medium_risk, df_high_risk], axis = 1)
  return df_principal_panel

#============= Creación data frame grafico PMG =================
def create_chart_PMG():
  columns_filter = ['CR.2','Cantidad Riesgo Bajo','Cantidad Riesgo Medio','Cantidad Riesgo Alto']
  df = clear_df_data_analisis()
  df_chart_PMG = create_an_copy(df)
  df_chart_PMG = create_query(df_chart_PMG, ['Tipo', 'tag_ponderado'], ['PMG', 'NO'], ['and', 'and'], ['==','=='], columns_filter)

  # Argumento 1 agrega la funcion .sum() al termino de la agrupación para que sume los valores
  # Si se el argumento "arg queda vacío agrupa y aplica de forma predetermianda la funcion .count()"
  df_chart_PMG = group_by_columns(df_chart_PMG, 'CR.2', 1)
  df_chart_PMG = cut_cr(df_chart_PMG)
  return df_chart_PMG
  
  
#============= Creación data frame grafico H =================
def create_chart_H():
  columns_filter = ['CR.2','Cantidad Riesgo Bajo','Cantidad Riesgo Medio','Cantidad Riesgo Alto']
  df = clear_df_data_analisis()
  df_chart_H = create_an_copy(df)
  df_chart_H = create_query(df_chart_H, ['Tipo', 'tag_ponderado'], ['H', 'NO'], ['and', 'and'], ['==','=='], columns_filter)
  df_chart_H = group_by_columns(df_chart_H, 'CR.2',1)
  df_chart_H = cut_cr(df_chart_H)
  return df_chart_H

#============= Creación data frame grafico CDC Nivel central =================
def create_chart_CDC():
  columns_filter = ['CR.2','Cantidad Riesgo Bajo','Cantidad Riesgo Medio','Cantidad Riesgo Alto']
  df = clear_df_data_analisis()
  df_chart_CDC = create_an_copy(df)
  df_chart_CDC = create_query(df_chart_CDC, ['Tipo', 'Nivel'], ['CDC', 'NC'], ['and','and'], ['==','=='], columns_filter)
  df_chart_CDC = group_by_columns(df_chart_CDC, 'CR.2', 1)
  df_chart_CDC = cut_cr(df_chart_CDC)
  return df_chart_CDC


#============ Creación data frame grafico CDC reg ==============
def create_chart_CDC_reg():
  columns_filter = ['CR.2','Cantidad Riesgo Bajo','Cantidad Riesgo Medio','Cantidad Riesgo Alto']
  df = clear_df_data_analisis()
  df_chart_reg = create_an_copy(df)
  columns_filter.insert(0,'CR')
  columns_filter.pop(1)
  df_chart_reg = create_query(df_chart_reg, ['Tipo', 'Nivel'], ['CDC', 'Regiones'], ['and','and'],['==','=='], columns_filter)
  df_chart_reg = group_by_columns(df_chart_reg, 'CR', 1)
  return df_chart_reg

