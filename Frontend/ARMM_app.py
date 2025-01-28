import tkinter as tk
from tkinter import filedialog
import customtkinter as ct
from PIL import Image, ImageTk
from Variables import *
from Utility_functions import clear_dir_output, clear_dir_report_parts
from Backend.inserts_to_excel.ins_principal import call_all_inserts
from Backend.create_report import print_report_sheets, merge_parts_report
from Backend.helper_functions import drop_parts_report

def btn():
    #call_all_inserts()
    for index in range(2):
        for  args in (path_report, path_anexo):
            print_report_sheets(args)
        merge_parts_report(dir_output, index)
        drop_parts_report()
        
        

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
    frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight = 0)


    # Añadir una imagen al frame
    image_path = "APP/Frontend/icons/Mineduc-PI.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    lbImg = tk.Label(frame, image = photo)
    lbImg.grid(columnspan = 2, row = 0, pady = 50, sticky = 's')


    ## Añadir un label
    label_notify_report = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "✓  Información obtenida", 
                        text_color = Exgob_Gray).grid(columnspan = 2,row = 1, pady = 5)

     ## Añadir un label
    label_notify_data = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "✓ fuentes de datos creadas", 
                        text_color = Exgob_Gray).grid(columnspan = 2,row = 2, pady = 5)
    
     ## Añadir un label
    label_notify_create_report = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "✓ Informe creado", 
                        text_color = Exgob_Gray).grid(columnspan = 2, row = 3, pady = 5)

    # Botón que permite subir el plan de tratamiento
    btn_upload = ct.CTkButton(master = frame, width = 220, height = 55, 
                            font = ("inter",14,"bold"), text = "Crear informe", 
                            text_color = Exgob_white, fg_color = Exgob_Red, 
                            border_color = Exgob_Red, border_width = 2, hover_color = Exgob_hover_red, 
                            corner_radius = 0, command = btn)
    
    btn_upload.grid(columnspan = 2, row = 4, pady = 5)

    # Label para notificar Planes con errores
    lb_error = ct.CTkLabel(frame, font = ("inter", 12, "bold"), 
                                 text = f"", text_color = Exgob_Red, wraplength = 450)
    
    lb_error.grid(columnspan = 2, row = 5)

    # footer de la app
    label4 = ct.CTkLabel(frame, 
                         font = ("inter",10,"italic"),
                         text = "Aplicación propiedad del gobierno - desarrollado por el DPCG", 
                         text_color = Exgob_black)
    
    label4.grid(columnspan = 2, row = 9, pady = 80)

    # Ejecutar la aplicación
    app.mainloop()