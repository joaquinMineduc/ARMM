import xlwings as xw

# Abrir un libro de Excel existente
wb = xw.Book("formato.xlsx")
ws = wb.sheets['Sheet1']  # Seleccionar la hoja específica

# Seleccionar el rango donde aplicarás el formato condicional
range_cells = ws.range('A1:A10')

# Acceder al rango API para aplicar la regla de íconos
icon_set = range_cells.api.FormatConditions.AddIconSetCondition()

# Configurar los íconos de semáforo
icon_set.IconSet = ws.api.Application.IconSets(1)  # 1 corresponde a '3TrafficLights1'

# Configurar valores para los íconos
icon_set.IconCriteria(2).Value = 50
icon_set.IconCriteria(2).Operator = 7  # >=
icon_set.IconCriteria(3).Value = 80
icon_set.IconCriteria(3).Operator = 7  # >=

# Guardar el libro
wb.save("formato_actualizado.xlsx")

# Opcional: cerrar el libro y Excel
wb.close()