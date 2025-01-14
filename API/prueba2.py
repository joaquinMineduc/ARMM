import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

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
for col in ws.columns:
    col_letter = get_column_letter(col[0].column)
    for cell in col:
        if cell.value:
            max_length = len(str(cell.value))
            if max_length > 100:
                ws.column_dimensions[col_letter].width = (max_length*0.2)
            else:
                ws.column_dimensions[col_letter].width = 0
                

"""for col in ws.iter_cols(min_col = 0, max_col = 13, min_row = 4, max_row = 4):
    for cell in col:
        
        len(cell.value)"""
        
    
    
        


        
wb.save("archivo_modificado.xlsx")