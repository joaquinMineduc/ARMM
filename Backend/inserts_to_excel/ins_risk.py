import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backend.inserts_to_excel.inserts_functions import modify_file, insert_graphics
from Frontend.Variables import dir_output, path_report
from risk_functions import *



DATE_REPORT = get_date()

columns = ['B','C','D']
columns_alerts = ['B', 'D', 'E']    
matriz_columns = ['G','I','L','O','R','T','V','X']
risk_columns = ['L','O','Q','S','T','V','W','Y']
columns_graph = ['C','D','E']
columns_eval_ptr = ['H', 'I','J', 'K', 'L']


def insert_data_risk():
    modify_file(dir_output + path_report, 'Gestión de riesgos', DATE_REPORT,'B', 4, 4)

    modify_file(dir_output + path_report, 'Gestión de riesgos', df_risk_tools, columns, 8, 15)

    modify_file(dir_output + path_report, 'Gestión de riesgos', df_monitoring, columns, 19, 23)

    modify_file(dir_output + path_report, 'Gestión de riesgos', df_matriz, matriz_columns, 14, 22)

    modify_file(dir_output + path_report, 'Gestión de riesgos', df_risk, risk_columns, 29, 37)

    modify_file(dir_output + path_report, 'data_riesgos', df_grap, columns_graph, 15, 39)
     
    if STATUS_PTR:
        configuration = {'title':f'Nivel de Cumplimiento - Estrategias para Señales de Alerta {datetime.now().today().year -1}',
            'colors':['#00B050','#0070C0','#C00000'], 'rotation': 0,'size': [2, 4], 'label_size': 28, 'dt_size': 35, 'leyenda': True}
        df_plan_tratamiento = adaptater_df_chart(df_plan_tratamiento)
        create_bar_chart(df_plan_tratamiento, 'Prueba2', configuration)
        create_bar_chart(df_alerts,'PTR_PRUEBA', configuration)
        # insert_graphics()
        
        modify_file(dir_output + path_report, 'Planes de tratamientos', DATE_PTR, 'A', 4, 4)
        modify_file(dir_output + path_report, 'Planes de tratamientos', df_plan_tratamiento, 
            columns, 13, 15)
        modify_file(dir_output + path_report, 'Planes de tratamientos', df_alerts, columns_alerts, 25, 25)
        modify_file(dir_output + path_report, 'Planes de tratamientos', df_eval_NC_ptr, 
            columns_eval_ptr, 21, 37)