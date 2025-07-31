from static_data import regiones
import time
import re
from collections import defaultdict
import ctypes
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from Frontend.Variables import *
import os
import re
import xlwings as xw
import win32com.client as win32
from pathlib import Path
import threading
import shutil





def second_threads(function, flag_wait = False):
  try:
    second_Thread = threading.Thread(target = function)
    second_Thread.start()
    if flag_wait:
        second_Thread.join()
  except Exception as e:
    raise Exception(f"Error scrapy {e}")

    
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
  dir_directory = os.path.join(dir_output_PDFs)
  for file in os.listdir(dir_directory):
        route_file = os.path.join(dir_directory, file)
        os.remove(route_file)


def drop_file_charts():
  for dir in [Path_charts_NC, Path_charts_PTR]:
    charts_files = os.listdir(dir)
    for file in charts_files:
      route_file = os.path.join(dir, file)
      os.remove(route_file)
      
      
def clear_directories():
  drop_parts_report()
  drop_file_charts()
  
  
# Estructura GUID para SHGetKnownFolderPath
class GUID(ctypes.Structure):
  _fields_ = [
      ("Data1", ctypes.c_uint32),
      ("Data2", ctypes.c_uint16),
      ("Data3", ctypes.c_uint16),
      ("Data4", ctypes.c_ubyte * 8),
  ]
  
  
def get_folder_id(folder_id):
  """Obtiene la ruta de una carpeta especial de Windows usando su GUID."""
  SHGetKnownFolderPath = ctypes.windll.shell32.SHGetKnownFolderPath
  SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_wchar_p)]
  SHGetKnownFolderPath.restype = ctypes.c_uint32

  # Convertir GUID desde string usando CLSIDFromString
  guid = GUID()
  ctypes.oledll.ole32.CLSIDFromString(folder_id, ctypes.byref(guid))

  path_ptr = ctypes.c_wchar_p()
  result = SHGetKnownFolderPath(ctypes.byref(guid), 0, None, ctypes.byref(path_ptr))
  if result != 0:
    raise Exception(f"Error obteniendo la carpeta: {result}")

  return Path(path_ptr.value)
  

def verify_donwload_reports(donwload_files):
  grouped_files = defaultdict(list)
  for file in donwload_files:
    # Eliminar sufijos como " (1)", " (2)" antes de la extensión
    base_name = re.sub(r' \(\d+\)$', '', file.stem) + file.suffix
    grouped_files[base_name].append(file)

    # ✅ Para cada grupo, quedarnos con el más reciente
    unique_files = []
    for base_name, files in grouped_files.items():
      most_recent = max(files, key=lambda f: f.stat().st_mtime)
      unique_files.append(most_recent)

    # ✅ Ordenar por fecha (más reciente primero)
    unique_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
  return unique_files


def normalizer_name_file(name_file):
  name_file = str(name_file).replace(" (","(")
  extention_file = str(name_file).split(".")[1]
  extract_name = str(name_file).split("(")[0]
  new_file_path = Path(f"{extract_name}.{extention_file}").resolve()
  return new_file_path

  
def get_download_reports():
  # GUID oficial para la carpeta Downloads
  FOLDERID_Downloads = "{374DE290-123F-4565-9164-39C4925E467B}"

  download_path = get_folder_id(FOLDERID_Downloads)

  if not download_path.exists():
    raise FileNotFoundError(f"No se encontró la carpeta Descargas: {download_path}")

  now = time.time()

  recent_files = [
    f for f in download_path.iterdir()
    if f.is_file() and (now - f.stat().st_mtime) < 190
  ]

  download_files = verify_donwload_reports(recent_files)
  length_files = len(download_files)
  for index, file in enumerate(download_files):
    if str(file).find("(") != -1:
      file = normalizer_name_file(file)
    print(file)
    if length_files == 7:
      match index:
        case 0:
          shutil.move(file, Path(directory_social_programs)/f'{file.name}')
        case 1|2:
            shutil.move(file, Path(directory_risk)/f"{file.name}")
        case 3:
            shutil.move(file, Path(directory_ADP)/f"{file.name}")
        case 4|5:
          if index == 4:
            shutil.move(file, Path(directory_sigemet)/"eval.xls")
          else:
            shutil.move(file, Path(directory_sigemet)/"indicadores.xls")
        case 6:
          shutil.move(file, Path(directory_ADP)/f"{file.name}")
    else:
        match index:
          case 0:
            shutil.move(file, Path(directory_social_programs)/f'{file.name}')
          case 1:
              shutil.move(file, Path(directory_risk)/f"{file.name}")
          case 2:
              shutil.move(file, Path(directory_ADP)/f"{file.name}")
          case 3|4:
            if index == 3:
              shutil.move(file, Path(directory_sigemet)/"eval.xls")
            else:
              shutil.move(file, Path(directory_sigemet)/"indicadores.xls")
          case 5:
            shutil.move(file, Path(directory_ADP)/f"{file.name}")
            

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
    new_route =  os.path.join(dir_output_PDFs,f"{part}.pdf")
    reassembled_list.append(new_route)
  return reassembled_list

    
def adaptater_df_chart(df):
  df = df.sum()
  return df

# modifica el estatus de visible cuando requiere realizar el reporte de indicadores PTR
def modify_status(sheet, status = False):
  location = path_report_format 
    
  init_excel = win32.gencache.EnsureDispatch('Excel.Application')
    
  init_excel.Visible = False # Para que la app de Excel no se inicialice en segundo plano, es decir, sin modo ventana
    
  constants = win32.constants
    
  wb = init_excel.Workbooks.Open(str(location))
  sheet = wb.Sheets(sheet)
    
  if status:
    sheet.Visible = constants.xlSheetVisible
  else:
    sheet.Visible = constants.xlSheetHidden
    
  wb.Save()
  wb.Close()
  init_excel.Quit()
    
  
def create_chart_panel(chart_name, categories, low_risk, medium_risk, high_risk, configuration):
  ind = np.arange(len(categories)) * configuration['size'][1]
  width = configuration['size'][0]

  fig, ax = plt.subplots(figsize=(len(categories) * configuration['size'][1], configuration['height']))
  
  G1 = ax.bar(ind, low_risk, width, color = configuration['colors'][0])
  G2 = ax.bar(ind, medium_risk, width, bottom=low_risk, color = configuration['colors'][1])
  G3 = ax.bar(ind, high_risk, width, bottom=np.array(low_risk) + np.array(medium_risk), color = configuration['colors'][2])
  
  
  # Ocultar todos los bordes del gráfico
  for spine in ax.spines:
    if spine != 'bottom':
      ax.spines[spine].set_visible(False)


  ax.yaxis.set_visible(False)
  ax.set_xticks(ind)
  ax.set_xticklabels(categories, fontsize= configuration['label_size'], fontweight = 'bold', rotation = configuration['rotation'])
  ax.set_ylabel('Valores')
  
  for label in ax.get_xticklabels():
    label.set_color('#595959')
  
    # Modificar etiquetas de datos con formato personalizado:
  for i in range(len(categories)):
      # medium_risk: agregar “✔” y color blanco
      ax.text(ind[i], low_risk[i]/2, f"{low_risk[i]}" if low_risk[i] > 0 else "", ha='center', va='center', color='white', fontweight='bold', 
        fontsize=configuration['dt_size'])
          
      # Amarillo: mostrar solo valor en negrita y color negro
      ax.text(ind[i], low_risk[i] + medium_risk[i]/2, f"{medium_risk[i]:.0f}" if  medium_risk[i] > 0  else "", ha='center', va='center',
        color='black', fontweight='bold', fontsize=configuration['dt_size'])
          
      # Rojo: mostrar valor con signo “⚠” y en rojo
      ax.text(ind[i], low_risk[i] + medium_risk[i] + high_risk[i]/2, f"{high_risk[i]}" if  high_risk[i] > 0  else "", ha='center',
        va='center', color='white', fontweight='bold', fontsize=configuration['dt_size'])
      
      plt.tight_layout()
      
  plt.savefig(Path(Path_charts_NC)/f'{chart_name}.png', dpi=800, bbox_inches='tight', pad_inches=0.2)
  
  
def create_bar_chart(df, chart_name, configuration = None):
  if configuration['simple_df']:
    estados = df.columns.tolist()
    valores = df.iloc[0].tolist()
  else:
    estados = df.index.tolist()
    valores = df.values.flatten().tolist()
    
  col_a, col_b, col_c = estados
  
  # Colores según el estado
  colores = {
        col_a: configuration['colors'][0],  # Implementada / cumplidos
        col_b: configuration['colors'][1],   # En proceso de implementación / En proceso
        col_c: configuration['colors'][2]  # No implementada / No cumplidos
  }

  # Aplicar colores a cada barra según su estado
  colores_barras = [colores[estado] for estado in estados]

  # Crear gráfico
  plt.figure(figsize=(configuration['size'][0], configuration['size'][1]))
  
  plt.bar(estados, valores, color=colores_barras)
  
  ax = plt.gca()
  for spine in ax.spines:
    if spine != 'bottom':
      ax.spines[spine].set_visible(False)
      
  ax.yaxis.set_visible(False)
  ax.xaxis.set_visible(False)

  if configuration['categories']:
    ax.xaxis.set_visible(True)
    ax.tick_params(axis='x', labelsize=10, color = '#595959')

  if configuration['leyenda']:
    # creación de leyendas
    legend_elements = [
        Patch(facecolor = configuration['colors'][0], label = col_a),
        Patch(facecolor = configuration['colors'][1], label = col_b),
        Patch(facecolor = configuration['colors'][2], label = col_c)
    ]
    
    # Mostrar leyenda
    plt.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, -0.30),
      ncol=3, frameon=False)  # ncol=3 para alineación horizontal
  
  # Título y etiquetas
  plt.title(configuration['title'], fontsize = 10 , color ='#595959', fontweight = 'bold', pad = 25)
  plt.ylabel("Cantidad")
  
  for label in ax.get_xticklabels():
    label.set_color('#595959')

  # Mostrar valores sobre cada barra
  for i, valor in enumerate(valores):
    plt.text(i, valor + 1, str(valor), ha='center')

  # Mostrar gráfico
  plt.tight_layout()
  plt.savefig(Path(Path_charts_PTR)/f'{chart_name}.png', dpi=700, bbox_inches='tight', pad_inches=0.05)
  
  

def create_bar_chart_h(df, chart_name, configuration):
  categorias = ['Financieros', 'Estratégicos', 'Institucionales']
  cumplidos = df['Cumplidos'].tolist()
  en_proceso = df['En proceso'].tolist()
  no_cumplidos = df['No Cumplidos/ Con retraso.'].tolist()


  # Posiciones en el eje Y
  y = np.arange(len(categorias))  # [0, 1, 2]
  altura_barra = 0.28

  # Crear gráfico
  plt.figure(figsize=(9.3, 7.3))

  bars1 = plt.barh(y - altura_barra, cumplidos, height=altura_barra, color=configuration['colors'][0], label='Cumplidos')
  bars2 =plt.barh(y, en_proceso, height=altura_barra, color=configuration['colors'][1], label='En Proceso')
  bars3 =plt.barh(y + altura_barra, no_cumplidos, height=altura_barra, color=configuration['colors'][2], label='No Cumplidos')

  # Ejes y título
  plt.yticks(y, categorias, fontsize = 20)
  plt.title(configuration['title'], fontsize = 20 , color ='#595959', fontweight = 'bold', pad = 5, loc='left')
    
  ax = plt.gca()
  for spine in ax.spines:
    if spine != 'left':
      ax.spines[spine].set_visible(False)
      
  ax.xaxis.set_visible(False)
    
  for label in ax.get_xticklabels():
    label.set_color('#595959')
      
  if configuration['leyenda']:
    # creación de leyendas
    legend_elements = [
        Patch(facecolor = configuration['colors'][0], label = 'Cumplidos'),
        Patch(facecolor = configuration['colors'][1], label = 'En proceso'),
        Patch(facecolor = configuration['colors'][2], label = 'No cumplidos / con retraso')
    ]
      
  # Mostrar leyenda
  plt.legend(handles=legend_elements, loc="lower left", bbox_to_anchor=(0.5, -0.15),
  ncol=3, frameon=False, fontsize=20)  # ncol=3 para alineación horizontal
  
  # Mostrar valores al final de cada barra
  for bars in [bars1, bars2, bars3]:
      for bar in bars:
          width = bar.get_width()
          if width !=0:
            y_pos = bar.get_y() + bar.get_height() / 2
            plt.text(width + 1, y_pos, str(int(width)), va='center', fontsize= 18, color = '#595959')
          
  # Mostrar gráfico
  plt.tight_layout()
  plt.savefig(Path(Path_charts_PTR)/f'{chart_name}.png', dpi=700, bbox_inches='tight', pad_inches=0.05)
  

