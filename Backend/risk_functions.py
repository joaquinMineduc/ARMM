from principal_functions import *
from report_functions import *
from eval_functions import eval_ptr
from helper_functions import modify_status
from Frontend.Variables import directory_risk
from pathlib import Path



def create_df_tools():
    # ========== Se crea el df que contienen las herramientas del monitoreo ============================
    df_risk_tools = create_dataframe(Path(directory_risk)/'Monitoreo - Gestión de riesgos.xlsx',
        'Herramienta_Monitoreo', 3)

    df_risk_tools = drop_unless_columns(df_risk_tools, None, None, 0)
    df_risk_tools = clear_df(df_risk_tools)
    df_risk_tools = partioner(df_risk_tools, 0, 8)
    return df_risk_tools


def create_df_monitoring():
    # ==================== Creación del df del monitoreo ==============================================
    df_monitoring = create_dataframe(Path(directory_risk)/'Monitoreo - Gestión de riesgos.xlsx', 
        'Herramienta_Monitoreo', 14)

    df_monitoring = drop_unless_columns(df_monitoring, None, None, 0)
    return df_monitoring

def create_df_matriz():
    # ==================== Creación del df de la matriz ==============================================
    df_matriz = create_dataframe(Path(directory_risk)/'Monitoreo - Gestión de riesgos.xlsx', 
        'Matrices', None)
    columns = df_matriz.loc[3].iloc[1:5].tolist() + df_matriz.loc[4].iloc[5:9].tolist()
    df_matriz = drop_unless_columns(df_matriz, None, None, 0)
    df_matriz.columns = columns
    df_matriz = clear_df(df_matriz)
    df_matriz = partioner(df_matriz, 0, 9)
    return df_matriz

def create_df_risk():
    # ==================== Creación del df riesgos =================================================
    df_risk = create_dataframe(Path(directory_risk)/'Monitoreo - Gestión de riesgos.xlsx', 
        'Matrices', 18)
    df_risk = drop_unless_columns(df_risk, None, None, 0)
    df_risk = clear_df(df_risk)
    df_risk = partioner(df_risk, 0, 9)
    return df_risk

def create_df_grap():
    # ================= Creación del df para el grafico de calor ==============================
    df_grap = create_dataframe(Path(directory_risk)/'Monitoreo - Gestión de riesgos.xlsx', 
        'datos_Grafico', 2)

    df_grap = drop_unless_columns(df_grap, None, None, 0)
    return df_grap



def create_df_tratamiento():
    # ======== Creación del DataFrame para el Dashboard planes de tratamientos =================
    df_plan_tratamiento = create_dataframe(Path(directory_risk)/'Planilla_PTR.xlsx', header = 5)
    df_plan_tratamiento = drop_unless_columns(df_plan_tratamiento, columns=[0, 1, 5])
    df_plan_tratamiento.dropna(inplace = True)
    df_plan_tratamiento = df_plan_tratamiento.apply(lambda row: row.astype(int))
    return df_plan_tratamiento
       
def create_df_alerts():
    df_alerts = create_dataframe(Path(directory_risk)/'Planilla_PTR.xlsx', header = 17)
    df_alerts = drop_unless_columns(df_alerts, columns=[0, 1, 3])
    df_alerts.dropna(inplace = True)
    return df_alerts


    