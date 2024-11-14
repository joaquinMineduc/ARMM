# funcion que elimina los documentos remanentes en caso de salida forzada
import datetime, os, shutil
import threading
import pandas as pd
import multiprocessing.process
from Variables import dir_in, dir_output


def clearDocuments():
    try:
        documents = os.listdir(dir_in)
        for document in documents:
            os.remove(dir_in + documents)
        #os.remove(dir_output)
    except:       
        print("the directory is empty")
    return 

