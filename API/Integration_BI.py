from openpyxl import Workbook
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import IconSetRule

# Crear un nuevo libro de Excel
wb = Workbook()
ws = wb.active

# Crear datos de ejemplo
ws.append(["Valor", "Semáforo"])
for i, val in enumerate([1, 2, 3, 2, 1, 3, 1], start=1):
    ws.cell(row=i + 1, column=1, value=val)

# Agregar una regla condicional de semáforos
icon_set_rule = IconSetRule(
    iconSet="3TrafficLights1",  # Estilo de semáforo (3 luces)
    type="num",                # Tipo de regla basada en números
    values=[1, 2, 3],          # Valores para definir los colores
    showValue=False            # Ocultar los valores en las celdas (opcional)
)

# Aplicar la regla a la columna A
ws.conditional_formatting.add("A2:A8", icon_set_rule)

# Guardar el archivo
wb.save("semaforos.xlsx")
