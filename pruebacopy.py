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
            frame1, text="Nuevo Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazUsuario),
            image=Nuevo_img, width=button_width, height=button_height
        )
        Nuevo_usuario.pack(pady=20)

        Modificar_usuario = CTkButton(
            frame1, text="Modificar Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Modificar_img,
            width=button_width, height=button_height
        )
        Modificar_usuario.pack(pady=20)

        Eliminar_usuario = CTkButton(
            frame1, text="Eliminar Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Eliminar_img,
            width=button_width, height=button_height
        )
        Eliminar_usuario.pack(pady=20)




class InterfazUsuario(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Marco principal
        scrollable_frame = CTkScrollableFrame(self, fg_color="#D9D9D9", corner_radius=20)
        scrollable_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        frame2 = CTkFrame(self, fg_color="white", corner_radius=20)
        frame2.grid(row=1, column=0, padx=30, pady=(10, 30), sticky="nsew")

        # Configurar columnas de frame2
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=1)
        frame2.grid_columnconfigure(2, weight=1)

        # Botones
        Regresar = CTkButton(frame2, text="Regresar", font=("", 15, "bold"), height=50,
                             fg_color="#FF5C5C", cursor="hand2", corner_radius=15,
                             command=lambda: controller.show_frame(Admin))
        Regresar.grid(row=0, column=0, sticky="w", padx=(30, 10), pady=(0, 10))

        guardar = CTkButton(frame2, text="Guardar", font=("", 15, "bold"), height=50,
                            fg_color="#0085FF", cursor="hand2", corner_radius=15,
                            command=self.validar_datos)
        guardar.grid(row=0, column=2, sticky="e", padx=(10, 30), pady=(0, 10))

        # Título
        title = CTkLabel(scrollable_frame, text="Registro de Inventario", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="n", pady=20)

        # Sección: Información general
        TipoRegistro = CTkOptionMenu(scrollable_frame, values=["Compra", "Donacion", "Dacion", "Fabricacion", "Comodato"],
                                      text_color="white", fg_color="black", font=("",15,"bold"), height=40)
        TipoRegistro.grid(row=1, column=0, sticky="ew", padx=30, pady=5)

        self.Nombres = self.create_entry(scrollable_frame, "Nombre", 2)
        self.Apellidos = self.create_entry(scrollable_frame, "Apellidos", 3)
        self.Fecha_Ingreso = self.create_entry(scrollable_frame, "Fecha Ingreso", 4)
        self.Fecha_Salida = self.create_entry(scrollable_frame, "Fecha Salida", 5)

        # Sección: Detalles adicionales
        section_title2 = CTkLabel(scrollable_frame, text="Detalles Adicionales", text_color="black", font=("", 20, "bold"))
        section_title2.grid(row=6, column=0, sticky="w", padx=30, pady=(10, 5))

        self.Descripcion = self.create_entry(scrollable_frame, "Descripción", 7)
        self.Cantidad = self.create_entry(scrollable_frame, "Cantidad", 8)
        self.Valor_Unitario = self.create_entry(scrollable_frame, "Valor Unitario", 9)
        self.Estado = self.create_entry(scrollable_frame, "Estado", 10)
        self.Ubicacion = self.create_entry(scrollable_frame, "Ubicación", 11)
        self.Registro_Fotografico = self.create_entry(scrollable_frame, "Registro Fotográfico", 12)
        self.UAA = self.create_entry(scrollable_frame, "UAA", 13)

        # Mensaje de resultados
        self.resultado_label = CTkLabel(frame2, text="", text_color="gray", font=("", 14, "italic"))
        self.resultado_label.grid(row=0, column=1, sticky="nsew", pady=10, padx=30)

        # Configuración de rejilla
        for i in range(15):
            scrollable_frame.grid_rowconfigure(i, weight=1)
        scrollable_frame.grid_columnconfigure(0, weight=1)

    def create_entry(self, parent, placeholder, row, show=None):
        entry = CTkEntry(parent, text_color="white", placeholder_text=placeholder,
                         fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), corner_radius=15, height=45, show=show)
        entry.grid(row=row, column=0, sticky="ew", padx=30, pady=5)
        return entry

    def validar_datos(self):
        # Validar los campos básicos
        campos = {
            "Nombre": self.Nombres.get(),
            "Apellidos": self.Apellidos.get(),
            "Fecha Ingreso": self.Fecha_Ingreso.get(),
            "Fecha Salida": self.Fecha_Salida.get(),
            "Cantidad": self.Cantidad.get()
        }

        for campo, valor in campos.items():
            if not valor.strip():
                self.resultado_label.configure(
                    text=f"El campo '{campo}' no puede estar vacío.",
                    text_color="red"
                )
                return

        # Validar que la cantidad sea un número
        try:
            cantidad = int(self.Cantidad.get())
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            self.resultado_label.configure(
                text="La cantidad debe ser un número positivo.",
                text_color="red"
            )
            return

        # Validar otros formatos si es necesario (por ejemplo, fechas)

        self.resultado_label.configure(
            text="Todos los datos son válidos. Guardando información...",
            text_color="green"
        )

