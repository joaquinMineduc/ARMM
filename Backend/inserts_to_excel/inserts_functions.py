import xlwings as xw


def modify_file(file_path, sheet_name, df, columns, start_row, end_row):
    with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            if isinstance(columns, list):
                insert_values(df, columns, start_row, end_row, ws)
            else:
                insert_date_document(df, columns, start_row, ws)
            route = "Backend/output/informe_final.xlsx"
            wb.save(route)
            return route

        
# funcion que inserta valores a la planilla Excel. recibe  df, 
# columnas del excel que se alteraran inicio y termino de la modificaicón, es decir, las filas        
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

def insert_date_document(date, column, row, ws):
    cell = ws[f"{column}{row}"]
    cell.value = date
    
    
        

    
