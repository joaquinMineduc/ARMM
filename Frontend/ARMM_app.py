import tkinter as tk
from tkinter import filedialog
import customtkinter as ct
from PIL import Image, ImageTk
from Variables import *
import time, threading
import sys
from pathlib import Path
# # Agrega la raíz del proyecto al path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from Utility_functions import clear_dir_output, clear_dir_report_parts
from Backend.inserts_to_excel.ins_principal import call_all_inserts
from Backend.create_report import print_report_sheets, merge_parts_report
from Backend.helper_functions import clear_directories, modify_status, get_download_reports, second_threads
from Integrations.integration_Sharepoint import get_instruments_files
from Integrations.integration_Sigemet import get_reports_sigemet


EVENT_END = threading.Event()
animation_thread = None 


def data_process():
    try:
        status_view(3, "disabled", Exgob_GrayLigth, Exgob_disabled_red, Exgob_Gray)
        animation("Extrayendo reportes y planillas",'gray')
        second_threads(get_instruments_files)
        second_threads(get_reports_sigemet,flag_wait=True)
        get_download_reports()
        EVENT_END.is_set()
        status_view(0)
        EVENT_END.clear() 
        animation("Realizando tratamiendo de datos",'gray')
        call_all_inserts()
        EVENT_END.is_set()
        status_view(1)
        EVENT_END.clear() 
        animation("Generando informe",'gray')
        for index in range(2):
            for  args in (Path_last_report, path_last_anexo):
                print_report_sheets(args)
            merge_parts_report(dir_output, index)
            clear_directories()
            modify_status("Planes de tratamientos", status = False)
            EVENT_END.is_set()
            status_view(2)
            EVENT_END.clear()
            status_view(4)
            # solicitar ubicación de guardado del informe
            clear_view(1)
    except Exception as e:
        print("Error:", e)
        EVENT_END.is_set()
        status_view(-1)
        clear_view(0)

    finally:
        EVENT_END.set()
        

def btn():
    EVENT_END.clear()
    second_threads(data_process)
    
    
def animation(text, text_color):
    global animation_thread

    # Detener hilo previo si sigue corriendo
    if animation_thread and animation_thread.is_alive():
        EVENT_END.set()       # Pedirle que se detenga
        animation_thread.join()  # Esperar a que termine
        EVENT_END.clear()     # Reiniciar evento para siguiente animación

    def loop():
        Aumento = ['.', '..', '...']
        while not EVENT_END.is_set():
            for i in Aumento:
                if EVENT_END.is_set():
                    break
                notify_process.configure(text=f"{text}{i}", text_color=text_color, font=("inter", 18))
                frame.update()
                time.sleep(1.5)

    animation_thread = threading.Thread(target=loop, daemon=True)
    animation_thread.start()
    

def status_view(widget, state_btn = None, background_color = None, fg_color = None, border_color = None):
    match widget:
        case 0:
            status_process_1.configure(text=f"Reportes y planillas extraidas: OK ✅", text_color= "green", font = ("inter", 20))
            frame.update()
        case 1:
            status_process_2.configure(text=f"Tratamientos de datos: OK ✅", text_color= "green", font = ("inter", 20))
            frame.update()
        case 2:
            status_process_3.configure(text=f"Informe mensual generado: OK ✅", text_color= "green", font = ("inter", 20))
            frame.update()
        case 3:
            btn_create_report.configure(state=state_btn, fg_color = background_color, text_color=fg_color, border_color = border_color )
            frame.update()
        case 4:
            notify_process.configure(text="")
            lb_error.configure(text = "¡El informe ha sido generado con éxito!", text_color = "green", font = ("inter", 20))
        case _:
            lb_error.configure(text=f"Ha ocurrido un error. Vuelva a ejecutar la app ❌", text_color= "red", font = ("inter", 20))
            time.sleep(2)
            lb_error.configure(text=f"Haz clic en el botón 'Generar informe'", text_color= "red", font = ("inter", 20))
            
            
def clear_view(mode_clear):
    match mode_clear:
        case 0:
            for widget in [status_process_1, status_process_2, status_process_3]:
                widget.configure(text="")
                frame.update()
            time.sleep(3)
            lb_error.configure(text="")
            notify_process.configure(text= "¡Hola, soy el BOT ARMM!", font=("inter", 20, "bold"))
            status_view(3, "normal", Exgob_Red, Exgob_white, Exgob_Red)
            frame.update()
        case 1:
            for widget in [status_process_1, status_process_2, status_process_3]:
                widget.configure(text="")
                frame.update()
            time.sleep(3)
            lb_error.configure(text="")
            notify_process.configure(text= "¡Hola, soy el BOT ARMM!", font=("inter", 20, "bold"))
            status_view(3, "normal", Exgob_Red, Exgob_white, Exgob_Red)
            frame.update()
        
                  
if __name__ == "__main__":
    clear_dir_output() # limpiar todos los archivos generados durante su uso
    clear_dir_report_parts()
    # Crear ventana principal  de la app
    app = tk.Tk()
    app.title("Generador de informes monitoreo mensual")
    app.geometry("480x750")
    app.minsize(width = 450, height = 650)
    app.iconbitmap("APP/Frontend/icons/logo-ministerio.ico")

    # Añadir un frame
    frame = tk.Frame(app)
    frame.pack(padx = 10, pady = 10,)

    frame.columnconfigure([0, 1], weight = 1)
    frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight = 0)

    # Añadir una imagen al frame
    image_path = "APP/Frontend/icons/Mineduc-PI.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    lbImg = tk.Label(frame, image = photo)
    lbImg.grid(columnspan = 2, row = 0, pady = 50, sticky = 's')

    ## Añadir un label
    notify_process = ct.CTkLabel(frame, font=("inter", 20, "bold"), 
                                  text="¡Hola, soy el BOT ARMM!", 
                                  text_color=Exgob_Gray)

    notify_process.grid(columnspan=2, row=1, pady=5)
    
    
     ## Añadir un label
    status_process_1 = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "", 
                        text_color = Exgob_Gray)
    
    status_process_1.grid(columnspan = 2,row = 2, pady = 5)
    
     ## Añadir un label
    status_process_2 = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "", 
                        text_color = Exgob_Gray)
    status_process_2.grid(columnspan = 2, row = 3, pady = 5)
    
    
     ## Añadir un label
    status_process_3 = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "", 
                        text_color = Exgob_Gray)
    status_process_3.grid(columnspan = 2, row = 4, pady = 5)

    # Botón pemite generar el informe
    btn_create_report = ct.CTkButton(master = frame, width = 220, height = 55, 
                            font = ("inter",14,"bold"), text = "Crear informe", 
                            text_color = Exgob_white, fg_color = Exgob_Red, 
                            border_color = Exgob_Red, border_width = 2, hover_color = Exgob_hover_red, 
                            corner_radius = 0, command = btn)
    
    btn_create_report.grid(columnspan = 2, row = 5, pady = 5)

    # Label para notificar Planes con errores
    lb_error = ct.CTkLabel(frame, font = ("inter", 12, "bold"), 
                                 text = f"", text_color = Exgob_Red, wraplength = 450)
    
    lb_error.grid(columnspan = 2, row = 6, pady = 5)

    # footer de la app
    label4 = ct.CTkLabel(frame, 
                         font = ("inter",10,"italic"),
                         text = "Aplicación propiedad del gobierno - desarrollado por el DPCG", 
                         text_color = Exgob_black)
    
    label4.grid(columnspan = 2, row = 7, pady = 80)

    # Ejecutar la aplicación
    app.mainloop()