# funcion que elimina los documentos remanentes en caso de salida forzada
import os
from Variables import dir_output, dir_output_PDFs


def clear_dir_output():
    try:
        documents = os.listdir(dir_output)
        for document in documents:
            if document not in ['anexo.xlsx','informe_final.xlsx','report_parts']:
                os.remove(os.path.join(dir_output, document))
                print(document)
    except:       
        print("the directory is empty")
    return


def clear_dir_report_parts():
    try:
        documents = os.listdir(os.path.join(dir_output, dir_output_PDFs))
        for document in documents:
            os.remove(os.path.join(dir_output, dir_output_PDFs, document))
    except:       
        print("the directory is empty")
    return
