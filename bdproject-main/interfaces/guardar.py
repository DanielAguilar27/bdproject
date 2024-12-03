from customtkinter import *
from datetime import datetime


# Configuración de apariencia en modo claro
set_appearance_mode("light")  # Activa el tema claro

class InterfazUsuario(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.campos = {}
        self.scrollable_frame = CTkScrollableFrame(self, fg_color="#D9D9D9", corner_radius=20)
        self.scrollable_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")
        self.frame2 = CTkFrame(self, fg_color="white", corner_radius=20)
        self.frame2.grid(row=1, column=0, padx=30, pady=(10, 30), sticky="ew")

        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)
        self.frame2.grid_columnconfigure(2, weight=1)

        from interfaces.tabla import InterfazTabla
        Regresar = CTkButton(self.frame2, text="Regresar", font=("", 15, "bold"), height=50,
                             fg_color="#FF5C5C", cursor="hand2", corner_radius=15,
                             command=lambda: controller.show_frame(InterfazTabla))
        Regresar.grid(row=0, column=0, sticky="w", padx=(30, 10), pady=(0, 10))

        guardar = CTkButton(self.frame2, text="Guardar", font=("", 15, "bold"), height=50,
                            fg_color="#0085FF", cursor="hand2", corner_radius=15,
                            command=self.validar_datos)
        guardar.grid(row=0, column=2, sticky="e", padx=(10, 30), pady=(0, 10))

        self.resultado_label = CTkLabel(self.frame2, text="", text_color="black", font=("", 14, "bold"))
        self.resultado_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=(5, 0))

        title = CTkLabel(self.scrollable_frame, text="Registro de Inventario", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="n", pady=20)

        self.TipoRegistro = CTkOptionMenu(self.scrollable_frame, 
                                          values=["Compra", "Donacion", "Dacion", "Fabricacion", "Comodato"],
                                          text_color="white", fg_color="black", font=("", 15, "bold"), height=40,
                                          command=self.cambio_interfaz)
        self.TipoRegistro.grid(row=1, column=0, sticky="ew", padx=30, pady=5)

        self.dynamic_frame = CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.dynamic_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=10)
        self.dynamic_frame.grid_columnconfigure(0, weight=1)

        self.cambio_interfaz("Compra")

    def create_entry(self, parent, placeholder, row, show=None):
        frame = CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, sticky="ew", pady=5)
        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)

        label = CTkLabel(frame, text=placeholder, text_color="black", font=("", 16, "bold"))
        label.grid(row=0, column=0, sticky="w", padx=(0, 10))

        entry = CTkEntry(frame, text_color="white", placeholder_text=placeholder,
                         fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), corner_radius=15, height=45, show=show)
        entry.grid(row=0, column=1, sticky="ew")

        return entry

    def cambio_interfaz(self, seleccion):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()
        self.campos = {}
        if seleccion == "Compra":
            self.campos['Nombres'] = self.create_entry(self.dynamic_frame, "Nombres", 0)
            self.campos['Apellidos'] = self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.campos['Descripcion'] = self.create_entry(self.dynamic_frame, "Descripción", 4)
            self.campos['Cantidad'] = self.create_entry(self.dynamic_frame, "Cantidad", 5)
            self.campos['Valor_Unitario'] = self.create_entry(self.dynamic_frame, "Valor Unitario", 6)
            self.campos['Estado'] = self.create_entry(self.dynamic_frame, "Estado", 7)


        elif seleccion == "Donacion":
            self.campos['Nombres'] = self.create_entry(self.dynamic_frame, "Nombres", 0)
            self.campos['Apellidos'] = self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.campos['Donante']= self.create_entry(self.dynamic_frame, "Donante", 4)
            self.campos['Valor_estimado']= self.create_entry(self.dynamic_frame, "Valor Estimado", 5)

        elif seleccion == "Dacion":
            self.campos['Nombres'] = self.create_entry(self.dynamic_frame, "Nombres", 0)
            self.campos['Apellidos'] = self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.campos['Descripcion']  = self.create_entry(self.dynamic_frame, "Descripción", 4)
            self.campos['Valor_Estimado']   = self.create_entry(self.dynamic_frame, "Valor Estimado", 5)

        elif seleccion == "Fabricacion":
            self.campos['Nombres'] = self.create_entry(self.dynamic_frame, "Nombres", 0)
            self.campos['Apellidos'] = self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.campos['Cantidad']  = self.create_entry(self.dynamic_frame, "Cantidad", 4)
            self.campos['Valor_Unitario'] =  self.create_entry(self.dynamic_frame, "Valor Unitario", 5)

        elif seleccion == "Comodato":
            self.campos['Nombres'] = self.create_entry(self.dynamic_frame, "Nombres", 0)
            self.campos['Apellidos'] = self.create_entry(self.dynamic_frame, "Apellidos", 1)
            self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso", 2)
            self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida", 3)
            self.campos['Ubicacion']  = self.create_entry(self.dynamic_frame, "Ubicación", 3)
            self.campos['Estado']  = self.create_entry(self.dynamic_frame, "Estado", 4)

    def validar_datos(self):
        # Realizar validación de datos según el tipo de registro seleccionado
        try:
            datos = {key: campo.get() for key, campo in self.campos.items()}
            if not isinstance(datos.get("Nombres"), str) or not datos.get("Nombres").strip():
                raise ValueError("El campo 'nombres' debe ser una cadena no vacía.")

            if not isinstance(datos.get("Apellidos"), str) or not datos.get("Apellidos").strip():
                raise ValueError("El campo 'apellidos' debe ser una cadena no vacía.")

            # Validar fechas
            fecha_ingreso = datetime.strptime(datos.get("Fecha_Ingreso"), "%Y-%m-%d")
            fecha_salida = datetime.strptime(datos.get("Fecha_Salida"), "%Y-%m-%d")
            cantidad = int(datos.get("Cantidad"))  
            Valor_unitario=int(datos.get("Valor_Unitario"))
            if fecha_salida < fecha_ingreso:
                raise ValueError("La 'Fecha_salida' no puede ser anterior a la 'Fecha_ingreso'.")

            if not isinstance(datos.get("Descripcion"), str) or not datos.get("Descripcion"):
                raise ValueError("El campo 'descripcion' debe ser una cadena no vacía.")

            if not isinstance(cantidad, int) or cantidad <= 0:
                raise ValueError("El campo 'Cantidad' debe ser un entero positivo.")

            if not isinstance(Valor_unitario, (int, float)) or Valor_unitario <= 0:
                raise ValueError("El campo 'valor_unitario' debe ser un número positivo.")

            return True
        except ValueError as e:
            self.resultado_label.configure(text=f"Error de validación: {e}")
        return False