from static_data import regiones
from Frontend.Variables import dir_output, dir_output_PDFs
import os
import re
import xlwings as xw
from win32com.client import constants



def classificator_by_reg(CR, arg):
  num_cr = CR.split(arg)
  num_cr = int(num_cr[1])
  for index, region in enumerate(regiones, start = 1):
    if index == num_cr:
      return region
    


def identificator_type_strings(var):
  """
    Esta función permite identificar si el STRING ingresado es un texto o un numero.
    Nota: Se recurre a esta función para hacer la distinción del tipo y según este,
    ejercer otra validación
    
    Args:
      var (String):  recibe el nombre de una de las hojas o parte del report mensual (PDF)
      
    Return:
      Boolean / int - 0:
        True: Si es cadena de texto
        False: Si es numero
        0: si es caracter especial
      Error:
        Si el argumento ingresado a la función es del tipo numerica o derivados.
  """
  try:
    return True if re.fullmatch(r'^[a-zA-Z!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>\/?\s]+$', var) else False
  except TypeError as e:
    print(f"Error del tipo --> {e}: Has ingreado un numero y no una cadena de texto")
    
    
    
def modfy_parts_reports(dir_base, path_file, new_path, drop_path):
  os.rename(os.path.join(dir_base, path_file), os.path.join(dir_base, f"{new_path}.pdf"))
  os.remove(dir_base + drop_path)
  
  
def drop_parts_report():
  dir_directory = os.path.join(dir_output, dir_output_PDFs)
  for file in os.listdir(dir_directory):
        route_file = os.path.join(dir_directory, file)
        os.remove(route_file)




def order_report_parts(data_list):
  """
  Esta función recibe el listado de rutas de cada una de las partes del informe en PDF(sheet name excel),
  Luego, se diseciona cada una a travpes de funciones split, además, el numero de orden es parseado
  de STRING a INT, para aplicar un orden de menor a mayor.

  Args:
      data_list (list): Se recibe la lista con las rutas de cada una de las partes del reporte(hojas pdf)

  Returns:
      return: lista de rutas ordena
  """
  # Primera parte : Disección de rutas
  segment_list = []
  reassembled_list = []
  for data in data_list:
    file = data.split("\\")[-1]
    file = file.split(".")[0]
    segment_list.append(int(file))
  segment_list = sorted(segment_list)
  # Segunda parte : Reestructuración de ruta con el orden requerido
  for part in segment_list:
    new_route =  os.path.join(dir_output, dir_output_PDFs,f"{part}.pdf")
    reassembled_list.append(new_route)
  return reassembled_list


  
"""def update_estructure_adp(document_path, sheet_file, rows_datas, row_comments):
  edges = [
    constants.xlEdgeLeft,
    constants.xlEdgeTop,
    constants.xlEdgeBottom,
    constants.xlEdgeRight
  ]
  
  wb = xw.Book(document_path)
  ws = wb.sheets[sheet_file]
  
  for _ in range(rows_datas):
    ws.range('6:6').api.EntireRow.Insert()
    
  for row in range(row_comments):
    range_border = ws.range(f'D{10+row}:J{10+row}')
    borders = range_border.api.Borders
    for edge in edges:
      b = borders(edge)
      b.LineStyle = constants.xlContinuous
      b.Weight    = constants.xlMedium
  wb.save()
  wb.close()"""