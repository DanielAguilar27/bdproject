from customtkinter import *
from PIL import Image
# Configuración de apariencia en modo claro
set_appearance_mode("light")  # Activa el tema claro
set_default_color_theme("blue")  # Usa el tema azul (no afecta el fondo blanco)

# Clase principal que administra las interfaces


# Interfaz principal
class InterfazPrincipal(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")  # Fondo blanco específico para esta interfaz

        # Cargar imágenes
        bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))
        user_img = CTkImage(dark_image=Image.open("Usuario.png"), size=(50, 50))

        # Configuración de la interfaz
        bg_lab = CTkLabel(self, image=bg_img, text="")
        bg_lab.grid(row=0, column=0)

        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20, width=360, height=310)
        frame1.grid(row=0, column=1, padx=40)
        frame1.grid_propagate(False)
        
        
        title = CTkLabel(frame1, text="Bienvenido!", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=80)

        Usuario = CTkButton(frame1, text="Usuario", font=("", 20, "bold"), height=100, width=50, fg_color="#0085FF",
                          cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(Interfaz2), image=user_img)
        Usuario.grid(row=3, column=0, sticky="w", pady=20, padx=10)

        Admin = CTkButton(frame1, text="Admin", font=("", 20, "bold"), height=100, width=50, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, image=user_img,
                             command=lambda: controller.show_frame(AdminLogin))
        Admin.grid(row=3, column=0, sticky="ne", pady=20, padx=0)

# Segunda interfaz
class Interfaz2(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")  # Fondo blanco para la segunda interfaz

        bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))

        bg_lab = CTkLabel(self, image=bg_img, text="")
        bg_lab.grid(row=0, column=0)

        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.grid_rowconfigure(0, weight=0)  # El título no necesita expandirse
        frame1.grid_rowconfigure(1, weight=0)
        frame1.grid_rowconfigure(2, weight=0)
        frame1.grid_rowconfigure(3, weight=0)
        frame1.grid_rowconfigure(4, weight=0)
        frame1.grid_rowconfigure(5, weight=0)
        frame1.grid_rowconfigure(6, weight=0)
        frame1.grid_rowconfigure(7, weight=0)
        frame1.grid_columnconfigure(0, weight=1)

        title = CTkLabel(frame1, text="Ingresar a la cuenta", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        usrname_entry = CTkEntry(frame1, text_color="white", placeholder_text="Usuario", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        usrname_entry.grid(row=1, column=0, sticky="nsew", padx=30)

        passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Contraseña", fg_color="black",
                                placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15,
                                height=45, show="*")
        passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

        Regresar = CTkButton(frame1, text="Regresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazPrincipal))
        Regresar.grid(row=3, column=0, sticky="w", pady=20, padx=40)

        ingresar = CTkButton(frame1, text="Ingresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15)
        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
class AdminLogin(CTkFrame):
    def __init__(self, parent, controller):
        def validar_admin():
            admin = admin_entry.get()
            passwd = passwd_entry.get()
            if admin == "admin" and passwd == "1234":
                return controller.show_frame(Admin)
            else:
                return resultado_label.configure(text="LA CONTRASEÑA O EL USUARIO ESTAN EQUIVOCADA.", text_color="red")
            
        super().__init__(parent, fg_color="white")  # Fondo blanco para la segunda interfaz

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
      
            
        Regresar = CTkButton(frame1, text="Regresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazPrincipal))
        Regresar.grid(row=3, column=0, sticky="w", pady=20, padx=40)
        
            
        ingresar = CTkButton(frame1, text="Ingresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command= validar_admin)
        ingresar.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)
class Admin(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")  # Fondo blanco para la segunda interfaz
        
        # Crear un frame con tamaño específico
        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.place(relx=0.5, rely=0.5, anchor="center")
        frame1.configure(width=400, height=400)  # Cambia el tamaño aquí
        frame1.pack_propagate(False)

        # Cargar imágenes
        Eliminar_img = CTkImage(dark_image=Image.open("EliminarUsuario.png"), size=(50, 50))
        Modificar_img = CTkImage(dark_image=Image.open("modificarUsuario.png"), size=(50, 50))
        Nuevo_img = CTkImage(dark_image=Image.open("nuevoUsuario.png"), size=(50, 50))

        # Crear botones con el mismo tamaño
        button_width = 250  # Ancho uniforme para todos los botones
        button_height = 90  # Alto uniforme para todos los botones

        Nuevo_usuario = CTkButton(
            frame1, text="Nuevo Usuario", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazPrincipal),
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


# Ejecución de la aplicación
