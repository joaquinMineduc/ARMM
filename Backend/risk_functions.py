from principal_functions import *
from report_functions import *



# ========== Se crea el df que contienen las herramientas del monitoreo ============================
df_risk_tools = create_dataframe("Backend/Input/Gestion riesgos/planilla_riesgos.xlsx", 
                                'Herramienta_Monitoreo', 3)

df_risk_tools = drop_unless_columns(df_risk_tools, None, None, 0)
df_risk_tools = clear_df(df_risk_tools)
df_risk_tools = partioner(df_risk_tools, 0, 8)


# ==================== Creación del df del monitoreo ==============================================
df_monitoring = create_dataframe("Backend/Input/Gestion riesgos/planilla_riesgos.xlsx", 
                                'Herramienta_Monitoreo', 14)

df_monitoring = drop_unless_columns(df_monitoring, None, None, 0)


# ==================== Creación del df de la matriz ==============================================
df_matriz = create_dataframe("Backend/Input/Gestion riesgos/planilla_riesgos.xlsx", 
                                'Matrices', None)
columns = df_matriz.loc[3].iloc[1:5].tolist() + df_matriz.loc[4].iloc[5:9].tolist()
df_matriz = drop_unless_columns(df_matriz, None, None, 0)
df_matriz.columns = columns
df_matriz = clear_df(df_matriz)
df_matriz = partioner(df_matriz, 0, 9)

# ==================== Creación del df riesgos =================================================
df_risk = create_dataframe("Backend/Input/Gestion riesgos/planilla_riesgos.xlsx", 
                            'Matrices', 18)
df_risk = drop_unless_columns(df_risk, None, None, 0)
df_risk = clear_df(df_risk)
df_risk = partioner(df_risk, 0, 9)



# ====================== Creación del df para el grafico de calor ==============================
df_grap = create_dataframe("Backend/Input/Gestion riesgos/planilla_riesgos.xlsx", 
                        'datos_Grafico', 2)
df_grap = drop_unless_columns(df_grap, None, None, 0)

