from analitics_class import *

YEAR = get_this_year()


# Creación del data frame
df = create_dataFrame('APP/Backend/Input/indicadores.xls')

# Se claisifcan indicadores ponderados
df = add_clasificator_ponderation(df)

df = add_split_indicador(df,'Indicador')

df = add_split_meta_periodo(df,'Período Meta')

df = add_classificator_type(df, 'Instrumento')

df = add_classificator_CR2(df, 'Centro Responsabilidad')
print(df)

df = add_new_column(df, [f'Numerador {str(YEAR)}',
                         f'Denominador {str(YEAR)}',
                         'Variacion Periodo',
                         'Nombre medios de verificación',
                         'Cumplimiento c/r a meta anual'])

df = add_order_CR(df, 'CR.2')
print(df)

df.to_excel("Anexo_octubre.xlsx", index = False)







