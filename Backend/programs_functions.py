from principal_functions import *
from report_functions import *


df_programs = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
    'programas sociales', 1)


df_monitoring = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
                                'Monitoreo y exante', header = 1)
df_monitoring = drop_unless_columns(df_monitoring, None, None, [2,3])
df_monitoring = partioner(df_monitoring, 0, 6)
#df_monitoring = clear_df(df_monitoring)
#drop_unless_rows(df_monitoring, None, None, [7])


print(df_programs)
print("----------------------")
print(df_monitoring)


df_exante = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",'Monitoreo y exante', header = 10)
df_exante = drop_unless_columns(df_exante, columns = 1 )
df_exante = clear_df(df_exante)

print(df_exante)

df_graph = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
                            'datos_graficos', 0)

print(df_graph)