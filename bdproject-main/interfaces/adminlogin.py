from customtkinter import *
from PIL import Image
from interfaces.tabla import InterfazTabla
from controlador.conexion import execute_query

class InterfazLogin(CTkFrame):

    def accountValid(self,name,password):
        query = '''select contraseña from usuarios where nombre_usuario = %s'''
        row = execute_query(query,(name,))
        if len(row)!=1: return False
        real_password = row[0][0]
        return (real_password==password)
            


    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white") 

        # Configurar para que se centre en la pantalla
        self.grid_columnconfigure(0, weight=1, uniform="equal")
        self.grid_rowconfigure(0, weight=1, uniform="equal")

        def validar_admin():
            admin = admin_entry.get()
            passwd = passwd_entry.get()
            if self.accountValid(admin, passwd):
                passwd_entry.delete(0, 'end')
                return controller.show_frame(InterfazTabla)
            else:
                return resultado_label.configure(text="LA CONTRASEÑA O EL USUARIO ESTÁN EQUIVOCADOS.", text_color="red")
        
        def pressed_enter(event):
            validar_admin()

        bg_img = CTkImage(dark_image=Image.open("media/bg1.jpg"), size=(500, 500))
        bg_lab = CTkLabel(self, image=bg_img, text="", anchor="center")
        bg_lab.grid(row=0, column=0, columnspan=2, sticky="nsw")

        # Frame para los elementos
        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

        title = CTkLabel(frame1, text="Ingresar administrador", text_color="black", font=("", 35, "bold"), anchor="center")
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        admin_entry = CTkEntry(frame1, text_color="white", placeholder_text="Usuario", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        admin_entry.grid(row=1, column=0, sticky="nwe", padx=30)
        
        passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Contraseña", fg_color="black",
                                placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15,
                                height=45, show="*")
        passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)
        passwd_entry.bind("<Return>", pressed_enter)
      
        Salir = CTkButton(frame1, text="Salir", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=quit)
        Salir.grid(row=3, column=0, sticky="w", pady=20, padx=40)
        
        ingresar = CTkButton(frame1, text="Ingresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=validar_admin)
        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)

        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)
