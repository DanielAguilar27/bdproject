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
        self.grid_rowconfigure(0, weight=0)  # Fila del frame1, no debe expandirse verticalmente
        # Frame para los botones
        frame1 = CTkFrame(self, fg_color="#D9D9D9")
        frame1.grid(row=0, column=0, sticky="ew")  # Ubicar en la parte superior
        frame1.grid_columnconfigure((0, 1, 2), weight=1)  # Configurar columnas expansibles

        Eliminar_img = CTkImage(dark_image=Image.open("EliminarUsuario.png"), size=(50, 50))
        Modificar_img = CTkImage(dark_image=Image.open("modificarUsuario.png"), size=(50, 50))
        Nuevo_img = CTkImage(dark_image=Image.open("nuevoUsuario.png"), size=(50, 50))

        Nuevo_usuario = CTkButton(
            frame1, text="Nuevo Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazUsuario),
            image=Nuevo_img, width=250, height=90
        )

        Modificar_usuario = CTkButton(
            frame1, text="Modificar Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Modificar_img,
            width=250, height=90
        )

        Eliminar_usuario = CTkButton(
            frame1, text="Eliminar Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, image=Eliminar_img,
            width=250, height=90
        )

        # Colocar botones en la cuadrícula
        Nuevo_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        Modificar_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        Eliminar_usuario.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


class InterfazUsuario(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Marco principal
        self.scrollable_frame = CTkScrollableFrame(self, fg_color="#D9D9D9", corner_radius=20)
        self.scrollable_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        self.frame2 = CTkFrame(self, fg_color="white", corner_radius=20)
        self.frame2.grid(row=1, column=0, padx=30, pady=(10, 30), sticky="ew")

        # Configurar columnas de frame2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(2, weight=1)

        # Botones
        Regresar = CTkButton(self.frame2, text="Regresar", font=("", 15, "bold"), height=50,
                             fg_color="#FF5C5C", cursor="hand2", corner_radius=15,
                             command=lambda: controller.show_frame(Admin))
        Regresar.grid(row=0, column=0, sticky="w", padx=(30, 10), pady=(0, 10))

        guardar = CTkButton(self.frame2, text="Guardar", font=("", 15, "bold"), height=50,
                            fg_color="#0085FF", cursor="hand2", corner_radius=15,
                            command=self.validar_datos)
        guardar.grid(row=0, column=2, sticky="e", padx=(10, 30), pady=(0, 10))

        # Título
        title = CTkLabel(self.scrollable_frame, text="Registro de Inventario", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="n", pady=20)

        # Selector de tipo de registro
        self.TipoRegistro = CTkOptionMenu(self.scrollable_frame, 
                                          values=["Compra", "Donacion", "Dacion", "Fabricacion", "Comodato"],
                                          text_color="white", fg_color="black", font=("", 15, "bold"), height=40,
                                          command=self.cambio_interfaz)
        self.TipoRegistro.grid(row=1, column=0, sticky="ew", padx=30, pady=5)

        # Contenedor para los campos dinámicos
        self.dynamic_frame = CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.dynamic_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=10)
        self.dynamic_frame.grid_columnconfigure(0, weight=1)  # Asegurar que los elementos dentro ocupen todo el ancho

        # Inicializar con la opción predeterminada
        self.cambio_interfaz("Compra")

    def cambio_interfaz(self, seleccion):
        # Eliminar widgets existentes en el contenedor dinámico
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

        # Campos para "Compra"
        if seleccion == "Compra":
            self.create_entry(self.dynamic_frame, "Nombre", 0)
            self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.create_entry(self.dynamic_frame, "Descripción", 4)
            self.create_entry(self.dynamic_frame, "Cantidad", 5)
            self.create_entry(self.dynamic_frame, "Valor Unitario", 6)
            self.create_entry(self.dynamic_frame, "Estado", 7)
            self.create_entry(self.dynamic_frame, "Ubicación", 8)
            self.create_entry(self.dynamic_frame, "Registro Fotográfico", 9)
            self.create_entry(self.dynamic_frame, "UAA", 10)

        # Campos para "Donacion"
        elif seleccion == "Donacion":
            self.create_entry(self.dynamic_frame, "Nombre", 0)
            self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.create_entry(self.dynamic_frame, "Donante", 4)
            self.create_entry(self.dynamic_frame, "Valor Estimado", 5)

        # Agregar más casos para otras opciones según sea necesario

    def create_entry(self, parent, placeholder, row, show=None):
        # Marco para texto y entrada
        frame = CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, sticky="ew", pady=5)
        frame.grid_columnconfigure(0, weight=0)  # Columna del texto, no expansible
        frame.grid_columnconfigure(1, weight=1)  # Columna del CTkEntry, expansible

        # Texto al lado izquierdo
        label = CTkLabel(frame, text=placeholder, text_color="black", font=("", 16, "bold"))
        label.grid(row=0, column=0, sticky="w", padx=(0, 10))

        # Campo de entrada
        entry = CTkEntry(frame, text_color="white", placeholder_text=placeholder,
                         fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), corner_radius=15, height=45, show=show)
        entry.grid(row=0, column=1, sticky="ew")  # Asegurar expansión horizontal

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

