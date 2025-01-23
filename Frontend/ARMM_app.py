import tkinter as tk
import time
from tkinter import filedialog
import customtkinter as ct
from PIL import Image, ImageTk
from Variables import *
from Utility_functions import clearDocuments




if __name__ == "__main__":
    clearDocuments() # limpiar todos los archivos generados durante su uso
    # Crear ventana principal  de la app
    app = tk.Tk()
    app.title("Unificador de planes de tratamiento")
    app.geometry("480x750")
    app.minsize(width = 450, height = 650)
    app.iconbitmap("ARMM/Frontend/icons/logo-ministerio.ico")


    # Añadir un frame
    frame = tk.Frame(app)
    frame.pack(padx = 10, pady = 10,)

    frame.columnconfigure([0, 1], weight = 1)
    frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight = 0)


    # Añadir una imagen al frame
    image_path = "ARMM/Frontend/icons/Mineduc-PI.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    lbImg = tk.Label(frame, image = photo)
    lbImg.grid(columnspan = 2, row = 0, pady = 50, sticky = 's')


    ## Añadir un label
    label = ct.CTkLabel(frame, font = ("inter", 16, "bold"), 
                        text = "Selecciona tus documentos:", 
                        text_color = Exgob_Gray).grid(columnspan = 2,row = 1, pady = 5)


    # Botón que permite subir el plan de tratamiento
    btn_upload = ct.CTkButton(master = frame, width = 220, height = 55, 
                            font = ("inter",14,"bold"), text = "Subir Excel", 
                            text_color = Exgob_blue, fg_color = Exgob_GrayLigth, 
                            border_color = Exgob_blue, border_width = 2,hover_color = Exgob_white, 
                            corner_radius = 0, command = "" )
    
    btn_upload.grid(columnspan = 2, row = 2, pady = 5)

   # label validación
    lb_verification = ct.CTkLabel(frame, 
                                  font = ("inter",12,"italic"),
                                  text = "Ningun plan seleccionado ...", 
                                  text_color = Exgob_black, 
                                  wraplength = 450)
    
    lb_verification.grid(columnspan = 2, row = 3, pady = 0)
    
    # Botón para descargar informe
    btn_download = ct.CTkButton(master = frame, state = "disabled",width = 195, 
                                bg_color=Exgob_white,height = 50, font = ("inter",14,"bold"), 
                                text = "Validar planes", text_color = Exgob_disabled_red, 
                                fg_color = Exgob_GrayLigth, border_color = Exgob_disabled_red,
                                border_width = 2, hover_color = Exgob_GrayLigth, corner_radius = 0, 
                                command = "") #command = download)
    
    btn_download.grid(columnspan = 2, row = 4, pady = 20)
    

    # Label para notificar Planes con errores
    lb_error = ct.CTkLabel(frame, font = ("inter", 12, "bold"), 
                                 text = f"", text_color = Exgob_Red, wraplength = 450)
    
    lb_error.grid(columnspan = 2, row = 5)
    
    
    # Label para notificar Planes con errores
    lb_error2 = ct.CTkLabel(frame, font = ("inter", 11, "bold"), 
                                 text = f"", text_color = Exgob_Red, wraplength = 450)
    
    lb_error2.grid(columnspan = 2, row = 6, pady = 10)


    # Label para mostrar la cantidad de planes subidos
    lb_download = ct.CTkLabel(frame, font = ("inter", 16, "bold"), text = f"",  
                              text_color = Exgob_Gray, wraplength = 450)

    lb_download.grid(columnspan = 2, row = 7)

    # footer de la app
    label4 = ct.CTkLabel(frame, 
                         font = ("inter",10,"italic"),
                         text = "Aplicación propiedad del gobierno - desarrollado por el DPCG", 
                         text_color = Exgob_black)
    
    label4.grid(columnspan = 2, row = 8, pady = 80)

    # Ejecutar la aplicación
    app.mainloop()