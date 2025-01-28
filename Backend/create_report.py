import os
import win32com.client as win32
from  helper_functions import identificator_type_strings, modfy_parts_reports, order_report_parts
from PyPDF2 import PdfMerger

def print_report_sheets(dir_document):
    # Obtener el directorio base del script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Directorio base: {base_dir}")

    # Construir la ruta relativa al archivo Excel
    excel_file = os.path.join(base_dir, "..", "Backend", "output", f"{dir_document}")
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
            for index, sheet in enumerate(workbook.Sheets, start = 0):
                # Verificar si la hoja está visible
                if sheet.Visible == win32.constants.xlSheetVisible:
                    if sheet.Name in ['anexo_final','anexo_risk']:
                        pdf_file = os.path.join(output_pdf_dir, f"{sheet.Name}.pdf")
                        pdf_file = os.path.normpath(pdf_file)
                    else:
                        # Construir la ruta del archivo PDF para la hoja actual
                        pdf_file = os.path.join(output_pdf_dir, f"{index}.pdf")
                        pdf_file = os.path.normpath(pdf_file)
                    # Exportar la hoja actual a PDF
                    sheet.ExportAsFixedFormat(0, pdf_file)
        except Exception as e:
            # Crear funcion que muestre el mensaje de error 
            print(f"Error durante la exportación: {e}")
        
        finally:
            # Cerrar el archivo Excel
            workbook.Close(SaveChanges=False)
            
            # Salir de Excel
            excel_app.Quit()

def merge_parts_report(dir_output, loop):
    # Lista de archivos PDF que deseas concatenar
    list_report_parts = []
    dir_report_parts = os.path.join(dir_output, "report_parts")
    for parts in os.listdir(dir_report_parts):
        part = parts.split(".")[0]  # Se disecciona para poder ejercer un orden jerarquico
        if identificator_type_strings(part):
            if loop == 0  and part == "anexo_final":
                modfy_parts_reports(dir_report_parts, parts, '6', '/anexo_risk.pdf')
                output_pdf = os.path.join(dir_output, 
                    f"Informe indicadores PMG CDC y Formularios H.pdf")   
            if loop == 1 and part == "anexo_risk":
                modfy_parts_reports(dir_report_parts, parts, '6', '/anexo_final.pdf')
                output_pdf = os.path.join(dir_output, 
                    f"Informe indicadores PMG CDC y Formularios H con Riesgos.pdf")
        else:
            if part == str(7):
                part = str(5)
                os.rename(os.path.join(dir_report_parts, parts), 
                        os.path.join(dir_report_parts, 
                        f"{part}.pdf"))
 
    for file in os.listdir(dir_report_parts):
        file = os.path.join(dir_report_parts, file)
        list_report_parts.append(file)
        
    list_report_parts = order_report_parts(list_report_parts)
    # Crear el objeto PdfMerger
    merger = PdfMerger()

    # Agregar cada archivo PDF al objeto merger
    for pdf in list_report_parts:
        merger.append(pdf)

    # Guardar el PDF combinado
    merger.write(output_pdf)
    merger.close()

    print(f"Archivo PDF combinado creado en: {output_pdf}")


