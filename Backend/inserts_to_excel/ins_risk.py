import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backend.inserts_to_excel.inserts_functions import modify_file, insert_graphics
from Frontend.Variables import Path_last_report, Path_charts_PTR
from risk_functions import *



DATE_REPORT = get_date()

columns = ['B','C','D']
columns_alerts = ['B', 'D', 'E']    
matriz_columns = ['G','I','L','O','R','T','V','X']
risk_columns = ['L','O','Q','S','T','V','W','Y']
columns_graph = ['C','D','E']
columns_eval_ptr = ['H', 'I','J', 'K', 'L']



def insert_data_risk():
    STATUS_PTR = False
    month_validation = get_month()
    df_risk_tools = create_df_tools()
    df_monitoring = create_df_monitoring()
    df_matriz = create_df_matriz()
    df_risk = create_df_risk()
    df_grap = create_df_grap()
    
    modify_file(Path_last_report, 'Gestión de riesgos', DATE_REPORT,'B', 4, 4)

    modify_file(Path_last_report, 'Gestión de riesgos', df_risk_tools, columns, 8, 15)

    modify_file(Path_last_report, 'Gestión de riesgos', df_monitoring, columns, 19, 23)

    modify_file(Path_last_report, 'Gestión de riesgos', df_matriz, matriz_columns, 14, 22)

    modify_file(Path_last_report, 'Gestión de riesgos', df_risk, risk_columns, 29, 37)

    modify_file(Path_last_report, 'data_riesgos', df_grap, columns_graph, 15, 39)
    
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

     
    if STATUS_PTR:
        configuration = {'title':f'Nivel de Cumplimiento - Estrategias para Señales de Alerta {datetime.now().today().year -1}',
            'colors':['#00B050','#0070C0','#C00000'], 'rotation': 0,'size': [6, 3], 
            'label_size': 16, 'dt_size': 35, 'leyenda': True, 'simple_df':True, 'categories': False}
        
        configuration_b = {'title':f'Nivel de Cumplimiento - Planes de Tratamiento de Riesgos {datetime.now().today().year -1}',
            'colors':['#00B050','#0070C0','#C00000'], 'rotation': 0,'size': [6, 3], 
            'label_size': 14, 'dt_size': 35, 'leyenda': False, 'simple_df':False, 'categories': True}
        
        configuration_c = {'title':f'Planes de Tratamiento de Riesgos Comprometidos el {datetime.now().today().year -1}',
            'colors':['#00B050','#0070C0','#C00000'], 'rotation': 0,'size': [6, 3], 
            'label_size': 20, 'dt_size': 35, 'leyenda': True, 'simple_df':False, 'categories': True}
        
        df_plan_tratamiento = create_df_tratamiento()
        df_alerts = create_df_alerts()
        df_chart_modify = adaptater_df_chart(df_plan_tratamiento)
        print(df_chart_modify)
        create_bar_chart(df_chart_modify, 'ptr_chart', configuration_b)
        create_bar_chart(df_alerts,'signals_chart', configuration)
        create_bar_chart_h(df_plan_tratamiento, 'ptr_chart_A', configuration_c)
        
        # Crear una validación para identificar imagenes con los nombres asignados
        for path_charts in Path_charts_PTR.iterdir():
            if path_charts.is_file():
                insert_graphics(Path_last_report, 'Planes de tratamientos', path_charts.resolve(), path_charts.stem)
        
        modify_file(Path_last_report, 'Planes de tratamientos', DATE_PTR, 'A', 4, 4)
        modify_file(Path_last_report, 'Planes de tratamientos', df_plan_tratamiento, 
            columns, 13, 15)
        modify_file(Path_last_report, 'Planes de tratamientos', df_alerts, columns_alerts, 25, 25)
        modify_file(Path_last_report, 'Planes de tratamientos', df_eval_NC_ptr, 
            columns_eval_ptr, 21, 37)