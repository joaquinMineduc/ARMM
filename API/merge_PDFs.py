from PyPDF2 import PdfMerger

# Lista de archivos PDF que deseas concatenar
pdf_files = [
    "hoja_1.pdf",
    "hoja_2.pdf",
    "hoja_3.pdf"
]

# Nombre del archivo PDF final
output_pdf = "archivo_concatenado.pdf"

# Crear el objeto PdfMerger
merger = PdfMerger()

# Agregar cada archivo PDF al objeto merger
for pdf in pdf_files:
    merger.append(pdf)

# Guardar el PDF combinado
merger.write(output_pdf)
merger.close()

print(f"Archivo PDF combinado creado en: {output_pdf}")
