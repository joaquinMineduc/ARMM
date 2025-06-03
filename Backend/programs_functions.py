from principal_functions import *
from report_functions import *


df_programs = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
    'programas sociales', 0)

df_programs = drop_unless_columns(df_programs, None, None, [2,3,4])
df_programs = clear_df(df_programs)


df_monitoring = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
                                'Monitoreo y exantes', header = None)
df_monitoring = drop_unless_columns(df_monitoring, None, None, [2,3,4])
df_monitoring = clear_df(df_monitoring)
drop_unless_rows(df_monitoring, None, None, 0)

df_milestones_programs = create_dataframe("APP/Backend/Input/social_programs/Planillas "+ 
    "programas sociales.xlsx", 'programas sociales')

df_milestones_programs = drop_unless_columns(df_milestones_programs, None, None, [0,1,2])
df_milestones_programs = clear_df(df_milestones_programs)
drop_unless_rows(df_milestones_programs, None, None, 0)


print(df_programs)
print(df_milestones_programs)

df_exante = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
                            'Monitoreo y exantes', header = None)
df_exante = partioner(df_exante, 10, 23)
df_exante = drop_unless_columns(df_exante, None, None, [1,3])
df_exante = clear_df(df_exante)

print(df_exante)

df_graph = create_dataframe("APP/Backend/Input/social_programs/Planillas programas sociales.xlsx",
                            'datos_graficos', 0)

print(df_graph)