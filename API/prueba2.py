import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.worksheet.page import PageMargins

# Crear un DataFrame de ejemplo

fill_color = PatternFill(start_color="002060", end_color="002060", fill_type="solid")
text_color = Font(bold=True, color='FFFFFF')
alignment_center_top = Alignment(horizontal="center", vertical="top", wrap_text=True)
alignment_center_left = Alignment(horizontal="left", vertical="top", wrap_text=True)
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

wb = load_workbook("informe_diciembre.xlsx")
ws = wb.active

ws.insert_rows(1, amount = 3)

ws.merge_cells('F3:H3')

ws['F3'].fill = fill_color
ws['F3'].font = text_color
ws['F3'].alignment = alignment_center_top
ws['F3'].value = "Año 2024"


for col in ws.iter_cols(min_col = 0, max_col = 13, min_row = 4 , max_row = 4):
    for cell in col: 
        cell.font = text_color
        cell.fill = fill_color
        cell.alignment = alignment_center_top
        
for col in ws.iter_cols(min_col = 0, max_col = 13, min_row = 5, max_row = 111):
    for cell in col:
        cell.alignment = alignment_center_left
        cell.border = thin_border


# Validar límite de extensión de alto de c/u de las celdas
# para columnas      
"""for col in ws.columns:
    col_letter = get_column_letter(col[0].column)
    for cell in col:
        if cell.value:
            max_length = len(str(cell.value))
            if max_length > 300:
                ws.column_dimensions[col_letter].width = (max_length*0.03)
            else:
                ws.column_dimensions[col_letter].width = 0"""

list_range_columns = []
for col in ws.iter_cols(min_col = 0, max_col = 13, min_row = 4, max_row = 4):
    for cell in col:
        list_range_columns.append(len(cell.value))


            

for col in ws.columns:
    col_letter = get_column_letter(col[0].column)
    for cell in col:
        for cell in col:
            if col_letter == 'B': 
                ws.column_dimensions[col_letter].width = list_range_columns[1] + 1
            if col_letter == 'A':
                ws.column_dimensions[col_letter].width = list_range_columns[0] + 8
            if col_letter == 'C':
                ws.column_dimensions[col_letter].width = list_range_columns[2] - 8
            if col_letter == 'E':
                ws.column_dimensions[col_letter].width = list_range_columns[4] + 3
            if col_letter == 'D':
                ws.column_dimensions[col_letter].width = list_range_columns[3] + 1.5
            if col_letter == 'F':
                ws.column_dimensions[col_letter].width = list_range_columns[5] + 3
            if col_letter == 'J':
                ws.column_dimensions[col_letter].width = list_range_columns[9] - 4
            if col_letter == 'G':
                ws.column_dimensions[col_letter].width = list_range_columns[6] + 3
            if col_letter == 'H':
                ws.column_dimensions[col_letter].width = list_range_columns[7]  + 3
            if col_letter == 'K':
                ws.column_dimensions[col_letter].width = list_range_columns[10] - 4
            if col_letter == 'I':
                ws.column_dimensions[col_letter].width = list_range_columns[8] - 7
            if col_letter == 'L':
                ws.column_dimensions[col_letter].width = list_range_columns[11] - 9
            if col_letter == 'M':
                ws.column_dimensions[col_letter].width = 120
            
            


ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE  # Landscape orientation
ws.page_setup.paperSize = ws.PAPERSIZE_LEGAL            # A4 paper size
ws.page_setup.scale = 65  # Fit to one page in width

# Set print titles (repeat first row on every printed page)
ws.print_title_rows = '3:4'

# Set margins
ws.page_margins = PageMargins(
    left=0, right=0,
    top=0, bottom=0,
    header=0, footer=0
)

# Set gridlines to be printed
ws.sheet_view.showGridLines = True

        
wb.save("archivo_modificado.xlsx")