import os
import win32com.client as win32

# Obtener el directorio base del script
base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Directorio base: {base_dir}")

# Construir la ruta relativa al archivo Excel
excel_file = os.path.join(base_dir, "..", "Backend", "output", "informe_final.xlsx")
output_pdf = os.path.join(base_dir, "..", "Backend", "output", "report_parts")

# Normalizar las rutas para evitar errores
excel_file = os.path.normpath(excel_file)
output_pdf = os.path.normpath(output_pdf)

# Verificar que el archivo Excel existe
if not os.path.exists(excel_file):
    print(f"Error: No se encuentra el archivo Excel en: {excel_file}")
else:
    print(f"El archivo Excel existe en: {excel_file}")

    # Construir la ruta del archivo PDF
    pdf_file = os.path.join(output_pdf, "informe_final.pdf")
    pdf_file = os.path.normpath(pdf_file)
    
    # Iniciar Excel y exportar a PDF
    excel_app = win32.Dispatch("Excel.Application")
    excel_app.Visible = False  # No mostrar la ventana de Excel
    
    # Abre el archivo Excel
    workbook = excel_app.Workbooks.Open(excel_file)
    
    # Seleccionar la hoja activa
    sheet = workbook.Sheets(1)
    
    # Exportar la hoja a PDF
    sheet.ExportAsFixedFormat(0, pdf_file)
    
    # Cerrar el archivo Excel
    workbook.Close(SaveChanges=False)
    
    # Salir de Excel
    excel_app.Quit()
    
    print(f"Hoja exportada a PDF en: {pdf_file}")
