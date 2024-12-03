from customtkinter import *
from PIL import Image
from interfaces.tabla import InterfazTabla

class InterfazAdminLogin(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white") 
        def validar_admin():
            admin = admin_entry.get()
            passwd = passwd_entry.get()
            if admin == "admin" and passwd == "1234":
                return controller.show_frame(InterfazTabla)
            else:
                return resultado_label.configure(text="LA CONTRASEÑA O EL USUARIO ESTAN EQUIVOCADOS.", text_color="red")
            
        bg_img = CTkImage(dark_image=Image.open("media/bg1.jpg"), size=(500, 500))
        bg_lab = CTkLabel(self, image=bg_img, text="")
        bg_lab.grid(row=0, column=0)

        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.grid(row=0, column=1, padx=40)

        title = CTkLabel(frame1, text="Ingresar administrador ", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        admin_entry = CTkEntry(frame1, text_color="white", placeholder_text="Admin", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        admin_entry.grid(row=1, column=0, sticky="nwe", padx=30)
        
        passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Contraseña", fg_color="black",
                                placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15,
                                height=45, show="*")
        passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)
      
        Salir = CTkButton(frame1, text="Salir", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=quit)
        Salir.grid(row=3, column=0, sticky="w", pady=20, padx=40)
        
        ingresar = CTkButton(frame1, text="Ingresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=validar_admin)
        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)