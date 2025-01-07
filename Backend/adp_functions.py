from principal_functions import *
from report_functions import *

# Se crea el DF con las fechas de los servicios
df_adp_data = create_dataframe("APP/Backend/Input/ADP/Planilla ADP monitoreo.xlsx", None, header = 3)
df_adp_data = drop_unless_columns(df_adp_data, None, None, 0)
df_adp_data = clear_df(df_adp_data)


# Se crea el DF con los comentarios de los servicios
df_adp_comments = create_dataframe("APP/Backend/Input/ADP/Planilla ADP monitoreo.xlsx", None, header = 15)
df_adp_comments = drop_unless_columns(df_adp_comments, None, None, [0,3,4,5,6,7,8])


date_document = get_date(True)

date_subtitle = get_date(text = 'Hitos ADP ocurridos al')


