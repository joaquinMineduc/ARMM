import os
import win32com.client as win32

# Obtener el directorio base del script
base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Directorio base: {base_dir}")

# Construir la ruta relativa al archivo Excel
excel_file = os.path.join(base_dir, "..", "Backend", "output", "informe_final.xlsx")
output_pdf_dir = os.path.join(base_dir, "..", "Backend", "output", "report_parts")

# Normalizar las rutas para evitar errores
excel_file = os.path.normpath(excel_file)
output_pdf_dir = os.path.normpath(output_pdf_dir)

# Crear el directorio de salida si no existe
os.makedirs(output_pdf_dir, exist_ok=True)

# Verificar que el archivo Excel existe
if not os.path.exists(excel_file):
    print(f"Error: No se encuentra el archivo Excel en: {excel_file}")
else:
    print(f"El archivo Excel existe en: {excel_file}")

    # Iniciar Excel y exportar a PDF
    excel_app = win32.Dispatch("Excel.Application")
    excel_app.Visible = False  # No mostrar la ventana de Excel

    try:
        # Abre el archivo Excel
        workbook = excel_app.Workbooks.Open(excel_file)

        # Iterar sobre todas las hojas del libro
        for  sheet in workbook.Sheets:
            # Verificar si la hoja está visible
            if sheet.Visible == win32.constants.xlSheetVisible:
                # Construir la ruta del archivo PDF para la hoja actual
                pdf_file = os.path.join(output_pdf_dir, f"{sheet.Name}.pdf")
                pdf_file = os.path.normpath(pdf_file)

                # Exportar la hoja actual a PDF
                print(f"Exportando hoja '{sheet.Name}' a {pdf_file}...")
                sheet.ExportAsFixedFormat(0, pdf_file)
            else:
                print(f"Hoja '{sheet.Name}' está oculta. No se exportará.")
        
        print(f"Exportación completada. Los archivos PDF están en: {output_pdf_dir}")
    
    except Exception as e:
        print(f"Error durante la exportación: {e}")
    
    finally:
        # Cerrar el archivo Excel
        workbook.Close(SaveChanges=False)
        
        # Salir de Excel
        excel_app.Quit()
