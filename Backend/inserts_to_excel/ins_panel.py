import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from panel_functions import *
from Backend.inserts_to_excel.inserts_functions import modify_file, insert_graphics
from Frontend.Variables import Path_report_final, Path_charts_NC



DATE_REPORT = get_date()

columns = ['G','K','M','O']
columns_graps = ['B','C','D','E']

def insert_data_panel():
    
    configurations_cdc = {'title':None,'colors':['green','yellow','red'], 'rotation': 0,'size': [1.2, 1.8], 'label_size': 16, 'dt_size': 42}
    configurations_reg = {'title':None,'colors':['green','yellow','red'], 'rotation': 75,'size': [1, 1.7], 'label_size': 28, 'dt_size': 35}
    configurations_H = {'title':None,'colors':['green','yellow','red'], 'rotation': 0,'size': [4, 7], 'label_size': 28, 'dt_size': 35}
    configuration = {'title':None,'colors':['green','yellow','red'], 'rotation': 0,'size': [2, 4], 'label_size': 28, 'dt_size': 35}
    chart_names = ['chart_CDC_reg', 'chart_H', 'chart_CDC', 'chart_PMG']
    
    for instrument, df in zip(chart_names, [df_chart_reg, df_chart_H, df_chart_CDC, df_chart_PMG]):
        if instrument ==  chart_names[0]:
            create_chart_panel(instrument, df['CR'], df['Cantidad Riesgo Bajo'], 
            df['Cantidad Riesgo Medio'], df['Cantidad Riesgo Alto'], configurations_reg)
        elif instrument == chart_names[1]:
            create_chart_panel(instrument, df['CR.2'], df['Cantidad Riesgo Bajo'], 
                df['Cantidad Riesgo Medio'], df['Cantidad Riesgo Alto'], configurations_H)
        elif instrument ==  chart_names[2]:
            create_chart_panel(instrument, df['CR.2'], df['Cantidad Riesgo Bajo'], 
            df['Cantidad Riesgo Medio'], df['Cantidad Riesgo Alto'], configurations_cdc)
        else:
             create_chart_panel(instrument, df['CR.2'], df['Cantidad Riesgo Bajo'], 
                df['Cantidad Riesgo Medio'], df['Cantidad Riesgo Alto'], configuration)
        
    # Crear una validación para identificar imagenes con los nombres asignados
    for path_charts in Path_charts_NC.iterdir():
        if path_charts.is_file():
            insert_graphics(Path_report_final, '01-PANEL', path_charts.resolve(), path_charts.stem)

    
    # Se agrega la fecha al documento
    modify_file(Path_report_final, '01-PANEL', DATE_REPORT, 'N', 5, 5)
    # Se modifica el panel del informe, la primera página que contiene los gráficos.
    modify_file(Path_report_final,'01-PANEL', df_principal_panel, columns, 10, 13)
    
