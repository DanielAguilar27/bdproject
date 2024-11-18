from customtkinter import *
from PIL import Image
import re
# Configuración de apariencia en modo claro
set_appearance_mode("light")  # Activa el tema claro

class AdminLogin(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white") 
        def validar_admin():
            admin = admin_entry.get()
            passwd = passwd_entry.get()
            if admin == "admin" and passwd == "1234":
                return controller.show_frame(Admin)
            else:
                return resultado_label.configure(text="LA CONTRASEÑA O EL USUARIO ESTAN EQUIVOCADA.", text_color="red")
            
        bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))
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
                             cursor="hand2", corner_radius=15, command= validar_admin)
        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)

class Admin(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")  # Fondo blanco para la segunda interfaz
        
        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.place(relx=0.5, rely=0.5, anchor="center")
        frame1.configure(width=400, height=400)  
        frame1.pack_propagate(False)
        Eliminar_img = CTkImage(dark_image=Image.open("EliminarUsuario.png"), size=(50, 50))
        Modificar_img = CTkImage(dark_image=Image.open("modificarUsuario.png"), size=(50, 50))
        Nuevo_img = CTkImage(dark_image=Image.open("nuevoUsuario.png"), size=(50, 50))
        button_width = 250  # Ancho uniforme para todos los botones
        button_height = 90  # Alto uniforme para todos los botones

        Nuevo_usuario = CTkButton(
            frame1, text="Nuevo Usuario", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazUsuario),
            image=Nuevo_img, width=button_width, height=button_height
        )
        Nuevo_usuario.pack(pady=20)

        Modificar_usuario = CTkButton(
            frame1, text="Modificar Usuario", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Modificar_img,
            width=button_width, height=button_height
        )
        Modificar_usuario.pack(pady=20)

        Eliminar_usuario = CTkButton(
            frame1, text="Eliminar Usuario", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Eliminar_img,
            width=button_width, height=button_height
        )
        Eliminar_usuario.pack(pady=20)

class InterfazUsuario(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)  
        
        # Create the main frame
        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        frame2=CTkFrame(self, fg_color="white", corner_radius=20)
        frame2.grid(row=1, column=0, padx=30 , sticky="nsew")
         # Button to go back
        Regresar = CTkButton(frame2, text="Regresar", font=("", 15, "bold"), height=50, 
                             fg_color="#0085FF", cursor="hand2", corner_radius=15, command=lambda:controller.show_frame(Admin))
        Regresar.grid(row=0,column=0)  

        # Save button with validation
        guardar = CTkButton(frame2, text="Guardar", font=("", 15, "bold"), height=50, 
                            fg_color="#0085FF", cursor="hand2", corner_radius=15, 
                            command=self.validar_datos)
        guardar.grid(row=0,column=1)
        # Title
        title = CTkLabel(frame1, text="Ingrese los datos: ", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="ns", pady=30, padx=10)

        # Option menu for TipoRegistro
        TipoRegistro = CTkOptionMenu(frame1, values=["Compra", "Donacion", "Dacion", "Fabricacion", "Comodato"],
                                      text_color="white", fg_color="black", font=("",15,"bold"), height=40)
        TipoRegistro.grid(row=1, column=0, sticky="ew", padx=30, pady=5)

        # Entry fields for name, lastname, DNI, and password
        self.create_entry(frame1, "Nombre responsable", 2)
        self.create_entry(frame1, "Apellidos", 3)
        self.create_entry(frame1, "DNI", 4)
        self.create_entry(frame1, "Estado", 5)
        # Result label to show validation messages
        self.resultado_label = CTkLabel(frame1, text="")
        self.resultado_label.grid(row=7, column=0, sticky="nsew", pady=10, padx=30)

        # Configure grid weights for responsiveness
        for i in range(8):
            frame1.grid_rowconfigure(i, weight=1)
        frame1.grid_columnconfigure(0, weight=1)

    def create_entry(self, parent, placeholder, row, show=None):
        entry = CTkEntry(parent, text_color="white", placeholder_text=placeholder, 
                         fg_color="black", placeholder_text_color="white", 
                         font=("", 16, "bold"), corner_radius=15, height=45, show=show)
        entry.grid(row=row, column=0, sticky="nsew", padx=30, pady=5)
        return entry

    def validar_datos(self):
        nombre = self.nombres.get()
        apellido = self.apellidos.get()
        correo = self.dni.get()
        password = self.password.get()
        
        if not (nombre.replace(" ", "").isalpha() and apellido.replace(" ", "").isalpha()):
            self.resultado_label.configure(text="Nombre y apellido deben contener solo letras.", text_color="red")
            return
        
        # Validate email format
        patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(patron_correo, correo):
            self.resultado_label.configure(text="El correo electrónico no tiene un formato válido.", text_color="red")
            return
        
        patron_password = r"\d+"  # Password must contain only numbers
        if not re.match(patron_password, password):
            self.resultado_label.configure(text="La contraseña solo debe tener números.", text_color="red")
            return
        
        self.resultado_label.configure(text="Validación exitosa.", text_color="green")