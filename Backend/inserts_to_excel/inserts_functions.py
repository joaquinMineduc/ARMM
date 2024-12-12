import xlwings as xw


def modify_file(file_path, sheet_name, df, columns, start_row, end_row):
    with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            insert_values(df, columns, start_row, end_row, ws)
            route = "APP/Backend/output/informe_final.xlsx"
            wb.save(route)
            return route

        
        
def insert_values(df, columns, start_row, end_row, ws):
   for index_column, column in enumerate(df):
      match index_column:
        case 0:
            insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
        case 1:
            insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
        case 2:
           insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
        case 3:
           insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
        case _:
           insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)



def insert_values_to_excel(values, columns, start_row, end_row, ws):
    values = values.tolist()
    for index_row, valor in enumerate(values, start = start_row):
        if index_row > end_row:
            break  # Salir si excede el rango de filas

        # Accede directamente a la celda de la columna 'D' y fila correspondiente
        cell = ws[f"{columns}{index_row}"]
        cell.value = valor
        

    
    
"""  # del D11 al D29
        columnas = ['E']  # Lista de columnas
        start_row = 11
        end_row = 29

        # Asegúrate de que los valores sean de tipo lista o iterable
        values = df_eval_NC['Oportunidad'].tolist()  # Convierte la serie a lista
        for index_row, valor in enumerate(values, start = start_row):
            if index_row > end_row:
                break  # Salir si excede el rango de filas

            # Accede directamente a la celda de la columna 'D' y fila correspondiente
            cell = ws[f"{columnas[0]}{index_row}"]
            cell.value = valor"""