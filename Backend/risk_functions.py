from principal_functions import *
from report_functions import *
from eval_functions import eval_ptr
from helper_functions import modify_status

STATUS_PTR = False
month_validation = get_month()

# ========== Se crea el df que contienen las herramientas del monitoreo ============================
df_risk_tools = create_dataframe("APP/Backend/Input/Adm_risk/Monitoreo - Gestión de riesgos.xlsx", 
    'Herramienta_Monitoreo', 3)

df_risk_tools = drop_unless_columns(df_risk_tools, None, None, 0)
df_risk_tools = clear_df(df_risk_tools)
df_risk_tools = partioner(df_risk_tools, 0, 8)


# ==================== Creación del df del monitoreo ==============================================
df_monitoring = create_dataframe("APP/Backend/Input/Adm_risk/Monitoreo - Gestión de riesgos.xlsx", 
    'Herramienta_Monitoreo', 14)

df_monitoring = drop_unless_columns(df_monitoring, None, None, 0)


# ==================== Creación del df de la matriz ==============================================
df_matriz = create_dataframe("APP/Backend/Input/Adm_risk/Monitoreo - Gestión de riesgos.xlsx", 
    'Matrices', None)
columns = df_matriz.loc[3].iloc[1:5].tolist() + df_matriz.loc[4].iloc[5:9].tolist()
df_matriz = drop_unless_columns(df_matriz, None, None, 0)
df_matriz.columns = columns
df_matriz = clear_df(df_matriz)
df_matriz = partioner(df_matriz, 0, 9)

# ==================== Creación del df riesgos =================================================
df_risk = create_dataframe("APP/Backend/Input/Adm_risk/Monitoreo - Gestión de riesgos.xlsx", 
    'Matrices', 18)
df_risk = drop_unless_columns(df_risk, None, None, 0)
df_risk = clear_df(df_risk)
df_risk = partioner(df_risk, 0, 9)

# ================= Creación del df para el grafico de calor ==============================
df_grap = create_dataframe("APP/Backend/Input/Adm_risk/Monitoreo - Gestión de riesgos.xlsx", 
    'datos_Grafico', 2)

df_grap = drop_unless_columns(df_grap, None, None, 0)

print(month_validation)
if month_validation in ['ABRIL','JULIO','OCTUBRE']:
    match month_validation:
        case 'ABRIL':
            date_text = 'Primer Trimestre -'
        case 'JULIO':
            date_text = 'Segundo Trimestre -'
        case 'OCTUBRE':
            date_text = 'Tercer Trimestre -'
    STATUS_PTR = True
    DATE_PTR = get_date(format2=True, text= date_text)
    df_eval_NC_ptr = eval_ptr()
    modify_status("Planes de tratamientos", status = True)

    # ======== Creación del DataFrame para el Dashboard planes de tratamientos =================
    df_plan_tratamiento = create_dataframe("APP/Backend/Input/Adm_risk/Planilla_PTR.xlsx", header = 5)
    df_plan_tratamiento = drop_unless_columns(df_plan_tratamiento, columns=[0, 1, 5])
    df_plan_tratamiento.dropna(inplace = True)
    df_plan_tratamiento = df_plan_tratamiento.apply(lambda row: row.astype(int))

    df_alerts = create_dataframe("APP/Backend/Input/Adm_risk/Planilla_PTR.xlsx", header = 17)
    df_alerts = drop_unless_columns(df_alerts, columns=[0, 1, 3])
    df_alerts.dropna(inplace = True)

    print(df_plan_tratamiento)
    print(df_alerts)
    