from Frontend.Variables import directory_ADP, dir_output_PDFs
from PyPDF2 import PdfMerger
from pathlib import Path
import shutil


def merge_adp():
    merger = PdfMerger()
    directory_out = Path(directory_ADP/"8.pdf")
    pdfs = sorted(directory_ADP.glob("*.pdf"))
    
    for pdf in pdfs:
        print(f"📎 Añadiendo: {pdf.name}")
        merger.append(str(pdf))

    
    # Guardar archivo unificado antes de eliminar
    salida = Path(directory_out)
    merger.write(str(salida))
    merger.close()
    print(f"✅ Archivo combinado guardado como: {salida.name}")

    # Eliminar archivos originales
    for pdf in pdfs:
        print(f"🗑️ Eliminando original: {pdf.name}")
        pdf.unlink()
        

    print("✅ Archivos originales eliminados.")
    
    
def copy_adp():
    shutil.copy(Path(directory_ADP)/"8.pdf", Path(dir_output_PDFs)/"8.pdf")
