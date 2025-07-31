import xlwings as xw
from Frontend.Variables import Path_last_report, path_last_anexo
from xlwings.constants import BordersIndex, LineStyle



def modify_anexo(file_path, sheet_name, df, columns, start_row, end_row):
    with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            if isinstance(columns, list):
                insert_values2(df, columns, start_row, end_row, ws)
            else:
                insert_date_document(df, columns, start_row, ws)
            wb.save(path_last_anexo)
            wb.close()
        
        
# funcion que inserta valores a la planilla Excel. recibe  df, 
# columnas del excel que se alteraran inicio y termino de la modificaicón, es decir, las filas        
def insert_values2(df, columns, start_row, end_row, ws):
   for index_column, column in enumerate(df):
        print(column)
        match index_column:
            case 0:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 1:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 2:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 3:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 4:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 5:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 6:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 7:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 8:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 9:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 10:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 11:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)
            case 12:
                insert_values_to_excel(df[column], columns[index_column], start_row, end_row, ws)


def modify_file(file_path, sheet_name, df, columns, start_row, end_row = None):
    with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        
        if end_row is None:
            end_row = start_row + len(df) -1
            
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            if isinstance(columns, list):
                insert_values(df, columns, start_row, end_row, ws)
            else:
                insert_date_document(df, columns, start_row, ws)
            wb.save(Path_last_report)
            wb.close()
        

        
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
    
     
def apply_borders(file_path, sheet_name):
     with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            used_range  = ws.used_range
            # Iterar por filas y columnas del rango usado
            for row in used_range.rows:
                for cell in row:
                    if cell.value or cell.value == 0:  # Validar si la celda tiene valor (no es None ni vacío)
                        # Aplicar bordes finos a la celda
                        for border_id in range(7, 13):  # Borde izquierdo, derecho, superior, inferior, y diagonales
                            cell.api.Borders(border_id).LineStyle = 1  # xlContinuous
                            cell.api.Borders(border_id).Weight = 2    # xlThin                   
            # Guardar los cambios
            wb.save(file_path)
            wb.close()
            

# Añade una formula para la validación de lso estados de cada indicador
def apply_format_formula(file_path, sheet_name, formula, columns, start_row, end_row):
    with xw.App(visible = False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            ws.range(f'{columns}{start_row}:{columns}{end_row}').formula = formula
        wb.save(Path_last_report)
        wb.close()
        
        
def insert_graphics(file_path, sheet_name, path_chart, chart_name):
    with xw.App(visible=False) as app:
        wb = app.books.open(file_path)
        sheet_panel = wb.sheets[sheet_name]

        for chart in sheet_panel.api.ChartObjects():
            if chart.Name == str(chart_name):
                top, left = chart.Top, chart.Left 
                height, width = chart.Height, chart.Width
                chart.Delete()
                print(f"✅ Insertando imagen desde: {path_chart}")
                # Insertar imagen en la misma posición
                new_pic = sheet_panel.pictures.add(str(path_chart), top = top, left = left)
                new_pic.height = height
                new_pic.width = width
                break
        wb.save(Path_last_report)
        wb.close()
        
        
def apply_right_border_column_j(file_path, sheet_name):
    with xw.App(visible=False) as app:
        wb = app.books.open(file_path)
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            ws = wb.sheets[sheet_name]
            used_range = ws.used_range

            for row in used_range.rows:
                if len(row) > 9:  # Verificamos que exista la columna J en la fila
                    cell = row[9]  # Columna J (índice 9)
                    if cell.value or cell.value == 0:
                        # Aplicar borde derecho (blanco)
                        border_right = cell.api.Borders(BordersIndex.xlEdgeRight)
                        border_right.LineStyle = LineStyle.xlContinuous
                        border_right.Weight = 2  # xlThin
                        border_right.Color = 16777215  # Blanco (RGB)

            wb.save(file_path)
            wb.close()


def insertar_files(file_path, sheet_name):
    with xw.App(visible=False) as app:
        wb = app.books.open(file_path)

        if sheet_name in [s.name for s in wb.sheets]:
            ws = wb.sheets[sheet_name]

            # Insertar desde la fila 12 hacia la 9 (en orden inverso para evitar desplazamientos)
            filas_a_insertar = [14, 13, 12, 11, 10]  # insertará una fila antes de cada número
            for fila in filas_a_insertar:
                ws.api.Rows(fila).Insert()

            wb.save(file_path)
            wb.close()
            print("✅ Filas insertadas entre la 9 y la 13.")
        else:
            print(f"❌ Hoja '{sheet_name}' no encontrada.")
       
       
def merge_files(file_path, sheet_name):
    with xw.App(visible=False) as app:
        wb = app.books.open(file_path)

        if sheet_name not in [s.name for s in wb.sheets]:
            print(f"La hoja '{sheet_name}' no existe.")
            wb.close()
            return

        ws = wb.sheets[sheet_name]

        pares_filas = [(9, 10), (11, 12), (13, 14), (15, 16), (17, 18)]

        for fila_inicio, fila_fin in pares_filas:
            for col in range(1, 14):  # Columnas de A (1) a M (13)
                rango = ws.range((fila_inicio, col), (fila_fin, col))
                rango.merge()
                
        # Ajustar altura de filas 10, 12, 14, 16, 18
        filas_ajustar_altura = [10, 12, 14, 16, 18]
        for fila in filas_ajustar_altura:
            ws.range(f"{fila}:{fila}").row_height = 160

        wb.save()
        wb.close()
        print("Celdas combinadas correctamente.")
        
