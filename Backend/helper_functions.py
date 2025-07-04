from static_data import regiones
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from Frontend.Variables import dir_output, dir_output_PDFs, dir_in, path_report_format
import os
import re
import xlwings as xw
import win32com.client as win32
from pathlib import Path


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



def cut_parent_base():
  ruta_base = Path(__file__).parent
  for parent in  ruta_base.parents:
    if parent.name == "Proyecto ARMM":
      return parent
    
def adaptater_df_chart(df):
  df = df.sum()
  return df


def modify_status(sheet, status = False):
  ruta_base = cut_parent_base()
  location = ruta_base  / dir_in / path_report_format 
    
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
      
  plt.savefig(f"APP/Backend/output/graphics/NC/{chart_name}.png", dpi=800, bbox_inches='tight', pad_inches=0.2)
  
  
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
  plt.savefig(f"APP/Backend/output/graphics/PTR/{chart_name}.png", dpi=700, bbox_inches='tight', pad_inches=0.05)
  
  

def create_bar_chart_h(df, chart_name, configuration):
  categorias = ['Financieros', 'Estratégicos', 'Financieros']
  cumplidos = df['Cumplidos'].tolist()
  en_proceso = df['En proceso'].tolist()
  no_cumplidos = df['No Cumplidos/ Con retraso.'].tolist()


  # Posiciones en el eje Y
  y = np.arange(len(categorias))  # [0, 1, 2]
  altura_barra = 0.25

  # Crear gráfico
  plt.figure(figsize=(10, 6))

  bars1 = plt.barh(y - altura_barra, cumplidos, height=altura_barra, color=configuration['colors'][0], label='Cumplidos')
  bars2 =plt.barh(y, en_proceso, height=altura_barra, color=configuration['colors'][1], label='En Proceso')
  bars3 =plt.barh(y + altura_barra, no_cumplidos, height=altura_barra, color=configuration['colors'][2], label='No Cumplidos')

  # Ejes y título
  plt.yticks(y, categorias)
  plt.title(configuration['title'], fontsize = 10 , color ='#595959', fontweight = 'bold', pad = 10)
    
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
  plt.legend(handles=legend_elements, loc="lower left", bbox_to_anchor=(0.5, -0.30),
  ncol=3, frameon=False)  # ncol=3 para alineación horizontal
  
  # Mostrar valores al final de cada barra
  for bars in [bars1, bars2, bars3]:
      for bar in bars:
          width = bar.get_width()
          if width !=0:
            y_pos = bar.get_y() + bar.get_height() / 2
            plt.text(width + 1, y_pos, str(int(width)), va='center', fontsize= configuration['label_size'], color = '#595959')
          
  # Mostrar gráfico
  plt.tight_layout()
  plt.savefig(f"APP/Backend/output/graphics/PTR/{chart_name}.png", dpi=700, bbox_inches='tight', pad_inches=0.05)
  

      

