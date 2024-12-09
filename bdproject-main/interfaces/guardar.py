from customtkinter import *
from datetime import datetime
from controlador.conexion import execute_query
import re

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
                            command=self.guardar_datos)
        guardar.grid(row=0, column=2, sticky="e", padx=(10, 30), pady=(0, 10))

        self.resultado_label = CTkLabel(self.frame2, text="", text_color="black", font=("", 14, "bold"))
        self.resultado_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=(5, 0))

        title = CTkLabel(self.scrollable_frame, text="Registro de Inventario", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="n", pady=20)

        self.TipoRegistro = CTkOptionMenu(self.scrollable_frame, 
                                          values=["Compra", "Donacion", "Dacion", "Fabricacion", "Comodato","Otros"],
                                          text_color="white", fg_color="black", font=("", 15, "bold"), height=40,
                                          command=self.change_interface)
        self.TipoRegistro.grid(row=1, column=0, sticky="ew", padx=30, pady=5)

        self.dynamic_frame = CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.dynamic_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=10)
        self.dynamic_frame.grid_columnconfigure(0, weight=1)

        # Configurar para que las columnas se expandan
        self.dynamic_frame.grid_columnconfigure(0, weight=1)  # Columna 0 para etiquetas
        self.dynamic_frame.grid_columnconfigure(1, weight=2)  # Columna 1 para los campos de entrada, ocupando más espacio

        self.TipoRegistro.set("Otros")
        self.change_interface("Otros")

    def create_entry(self, parent, placeholder, row, show=None):
        frame = CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, sticky="ew", pady=5)
        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)

        entry = CTkEntry(frame, text_color="white", placeholder_text=placeholder,
                         fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), corner_radius=15, height=45, show=show)
        entry.grid(row=0, column=1, sticky="ew")

        entry.label = CTkLabel(frame, text=placeholder, text_color="black", font=("", 16, "bold"),anchor="center")
        entry.label.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        return entry

    def change_interface(self, seleccion):
        self.campos = {}
        self.resultado_label.configure(text="")

        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

        self.index = 0
        def icount():
            index = self.index
            self.index+=1
            return index
        
        def toggle_pais_entry():
            # Si el Checkbutton está marcado, mostrar el campo de país
            if self.importado.get():
                if self.campos['Pais_Proveniencia'] is None:
                    # Crear el campo de entrada para el país de proveniencia si no existe
                    self.campos['Pais_Proveniencia'] = self.create_entry(self.dynamic_frame, "País de Proveniencia", self.index)
            else:
                # Si no está marcado, ocultar el campo de país
                if self.campos['Pais_Proveniencia']:
                    self.campos['Pais_Proveniencia'].label.grid_forget()
                    self.campos['Pais_Proveniencia'].grid_forget()  # Eliminar la entrada del país
                    self.campos['Pais_Proveniencia'] = None

        self.campos['Descripcion'] = self.create_entry(self.dynamic_frame, "Descripción", icount())
        self.campos['Cantidad'] = self.create_entry(self.dynamic_frame, "Cantidad", icount())
        self.campos['Valor_Unitario'] = self.create_entry(self.dynamic_frame, "Valor Unitario", icount())
        self.campos['Estado'] = self.create_entry(self.dynamic_frame, "Estado", icount())
        self.campos['Ubicación'] = self.create_entry(self.dynamic_frame, "Ubicación", icount())
        self.campos['Registro_Fotográfico'] = self.create_entry(self.dynamic_frame, "Registro Fotográfico", icount())

        self.campos['UAA'] = self.create_entry(self.dynamic_frame, "UAA", icount())

        self.campos['Nombre_Responsable'] = self.create_entry(self.dynamic_frame, "Nombre del Responsable", icount())
        self.campos['Fecha_Ingreso'] = self.create_entry(self.dynamic_frame, "Fecha Ingreso (YYYY-MM-DD)", icount())
        self.campos['Fecha_Salida'] = self.create_entry(self.dynamic_frame, "Fecha Salida (YYYY-MM-DD)", icount())

        self.campos['Fecha_Ingreso'].bind("<KeyRelease>", self.formatear_fecha_ingreso)
        self.campos['Fecha_Salida'].bind("<KeyRelease>", self.formatear_fecha_salida)

        if seleccion == "Compra":
            self.campos['Pais_Proveniencia'] = None
            self.campos['Nombre_Comprador'] = self.create_entry(self.dynamic_frame, "Nombre Comprador", icount())
            self.importado = BooleanVar(value=False)
            checkbutton = CTkCheckBox(self.dynamic_frame, font=("", 15, "bold"), text="Importado", variable=self.importado, command=toggle_pais_entry)
            checkbutton.grid(row=icount(), column=0, columnspan=2, padx=10, pady=5, sticky="w")

        elif seleccion == "Donacion":
            self.campos['Nombre_Donante'] = self.create_entry(self.dynamic_frame, "Nombre del donante", icount())
            self.campos['Tipo_DNI_Donante'] = self.create_entry(self.dynamic_frame, "Tipo de documento", icount())
            self.campos['DNI_Donante'] = self.create_entry(self.dynamic_frame, "Documento del donante", icount())
            self.campos['Unidad_Donante'] = self.create_entry(self.dynamic_frame, "Nombre de la unidad donante", icount())

        elif seleccion == "Dacion":
            self.campos['Concepto_DMT'] = self.create_entry(self.dynamic_frame, "Concepto DMT", icount())
            self.campos['Concepto_DSI'] = self.create_entry(self.dynamic_frame, "Concepto DSI", icount())
            self.campos['Resolucion'] = self.create_entry(self.dynamic_frame, "Descripción", icount())

        elif seleccion == "Fabricacion":
            self.campos['Nombre_Fabricante'] = self.create_entry(self.dynamic_frame, "Nombre del Fabricante", icount())
            self.campos['Avaluo_Fabricacion'] = self.create_entry(self.dynamic_frame, "Avaluo de la fabricación", icount())

        elif seleccion == "Comodato":
            self.campos['Concepto_DMT'] = self.create_entry(self.dynamic_frame, "Concepto DMT", icount())
            self.campos['Concepto_DSI'] = self.create_entry(self.dynamic_frame, "Concepto DSI", icount())
            self.campos['Copia'] = self.create_entry(self.dynamic_frame, "Copia del comodato", icount())

    def formatear_fecha_ingreso(self,evento):
        tipo="Fecha_Ingreso"
        fecha = self.campos[tipo].get().strip()

        # Eliminar cualquier carácter no numérico y ajustar el formato de la fecha
        fecha_limpia = re.sub(r'\D', '', fecha)

        # Si la longitud es mayor de 8, recortar a 8 caracteres (formato YYYY-MM-DD)
        if len(fecha_limpia) > 8:
            fecha_limpia = fecha_limpia[:8]

        # Ahora se asegura de que el formato sea siempre YYYY-MM-DD
        if len(fecha_limpia) >= 5:
            fecha_limpia = f"{fecha_limpia[:4]}-{fecha_limpia[4:6]}-{fecha_limpia[6:8]}"

        # Actualizar el valor del campo con el formato correcto
        self.campos[tipo].delete(0, 'end')
        self.campos[tipo].insert(0, fecha_limpia)
    
    def formatear_fecha_salida(self,evento):
        tipo="Fecha_Salida"
        fecha = self.campos[tipo].get().strip()

        # Eliminar cualquier carácter no numérico y ajustar el formato de la fecha
        fecha_limpia = re.sub(r'\D', '', fecha)

        # Si la longitud es mayor de 8, recortar a 8 caracteres (formato YYYY-MM-DD)
        if len(fecha_limpia) > 8:
            fecha_limpia = fecha_limpia[:8]

        # Ahora se asegura de que el formato sea siempre YYYY-MM-DD
        if len(fecha_limpia) >= 5:
            fecha_limpia = f"{fecha_limpia[:4]}-{fecha_limpia[4:6]}-{fecha_limpia[6:8]}"

        # Actualizar el valor del campo con el formato correcto
        self.campos[tipo].delete(0, 'end')
        self.campos[tipo].insert(0, fecha_limpia)

    def validar_datos(self):
        # Dependiendo del tipo de registro seleccionado, se toman los campos de entrada
        try:
            # Revisa los datos comunes para las distintas selecciones
            if not self.campos['Nombre_Responsable'].get().strip():
                raise ValueError("El campo 'Nombres' no puede estar vacío.")
            if not self.campos['Fecha_Ingreso'].get().strip():
                raise ValueError("El campo 'Fecha Ingreso' no puede estar vacío.")
            if not self.campos['Fecha_Salida'].get().strip():
                raise ValueError("El campo 'Fecha Salida' no puede estar vacío.")
            if not self.campos['Descripcion'].get().strip():
                raise ValueError("El campo 'Descripción' no puede estar vacío.")
            
            # Revisa que sean números 
            if not self.campos['Cantidad'].get().strip().isdigit():
                raise ValueError("El campo 'Cantidad' debe ser un número entero.")
            if not self.campos['Valor_Unitario'].get().strip().replace('.', '', 1).isdigit():
                raise ValueError("El campo 'Valor Unitario' debe ser un número válido.")
            
            if not self.campos['Estado'].get().strip():
                raise ValueError("El campo 'Estado' no puede estar vacío.")
            if not self.campos['Ubicación'].get().strip():
                raise ValueError("El campo 'Ubicación' no puede estar vacío.")
            if not self.campos['Registro_Fotográfico'].get().strip():
                raise ValueError("El campo 'Registro Fotográfico' no puede estar vacío.")
            if not self.campos['UAA'].get().strip():
                raise ValueError("El campo 'UAA' no puede estar vacío.")
            if not self.revisar_UAA():
                raise ValueError("El campo 'UAA' no es valido.")
            
            # Revisa que la fecha sea valida
            if not self._validar_fecha(self.campos['Fecha_Ingreso'].get()):
                raise ValueError("La 'Fecha Ingreso' no tiene un formato válido.")
            if not self._validar_fecha(self.campos['Fecha_Salida'].get()):
                raise ValueError("La 'Fecha Salida' no tiene un formato válido.")

        except ValueError as e:
            # En caso de error, mostrar el mensaje de error
            return e

    def _validar_fecha(self, fecha):
        # Validación de fecha en formato "YYYY-MM-DD"
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def revisar_UAA(self):
        query = "select count(*) from uaa where uaa.Nombre like %s;"
        row = execute_query(query, (self.campos['UAA'].get(),))
        if len(row) == 0: 
            return False
        else: 
            if row[0][0] > 0:
                return True
            else:
                return False

    def insertar_elemento(self):
        # Obtiene los datos de las entries
        Fecha_Salida = self.campos['Fecha_Salida'].get()
        Fecha_Ingreso = self.campos['Fecha_Ingreso'].get()
        Nombre_Responsable = self.campos['Nombre_Responsable'].get()

        # Inserta los datos de legalización
        query = '''INSERT INTO Legalizacion (Fecha_Salida, Fecha_Ingreso, Nombre_Responsable) VALUES
                (%s, %s, %s);'''
        execute_query(query, (Fecha_Salida, Fecha_Ingreso, Nombre_Responsable,))

        # Obtiene el ID de la última legalización generada
        query = '''select ID from legalizacion order by id desc limit 1;'''
        ID_Legalizacion = execute_query(query)[0][0]

        # Obtiene el valor de la entry UAA
        UAA = self.campos['UAA'].get()

        # Obtiene el ID de la UAA seleccionada
        query = '''select ID from uaa where uaa.Nombre like %s;'''
        ID_UAA = execute_query(query, (UAA,))[0][0]

        # Inserta el nuevo elemento
        query = '''INSERT INTO Elemento (ID_Tipo, Secuencia, ID_Legalizacion, ID_UAA, ID_Inconsistencia, Descripcion, Cantidad, Valor_Unitario, Estado, Ubicacion, Registro_Fotografico) VALUES
        (1, 1, %s, %s, NULL, %s, %s, %s, %s, %s, %s);'''

        # Obtiene el valor de las entries necesarias
        Descripcion = self.campos['Descripcion'].get()
        Cantidad = self.campos['Cantidad'].get()
        Valor_Unitario = self.campos['Valor_Unitario'].get()
        Estado = self.campos['Estado'].get()
        Ubicacion = self.campos['Ubicación'].get()
        Registro_Fotografico = self.campos['Registro_Fotográfico'].get()

        execute_query(query, (ID_Legalizacion, ID_UAA, Descripcion, Cantidad, Valor_Unitario, Estado, Ubicacion, Registro_Fotografico))

        query = '''select ID from elemento order by id desc limit 1;'''

        ID_Elemento = execute_query(query)[0][0]
        
        return ID_Elemento

    def obtener_donante(self):
        query = '''select id from donantes where nombre = %s and dni = %s and tipo_dni = %s'''
        Nombre_Donante = self.campos['Nombre_Donante'].get()
        Tipo_DNI = self.campos['Tipo_DNI_Donante'].get()
        DNI = self.campos['DNI_Donante'].get()
        id_donante = execute_query(query,(Nombre_Donante,DNI,Tipo_DNI,))

        if len(id_donante)!=1:
            query = '''insert into donantes (Nombre, Tipo_DNI,DNI) values
                    (%s, %s,%s);'''
            execute_query(query,(Nombre_Donante,Tipo_DNI,DNI,))
            return self.obtener_donante()
        else:
            return id_donante[0][0]

    def guardar_datos(self):
        error = self.validar_datos()
        if error != None: 
            self.resultado_label.configure(text=str(error), text_color="red")
            return

        # Obtiene el ID del nuevo elemento creado
        ID_Elemento = self.insertar_elemento()

        Tipo_Registro = self.TipoRegistro.get()

        if Tipo_Registro == "Compra":
            query = '''insert into compra (ID_Elemento, Nombre_comprador) values
                    (%s, %s);'''

            # Obtiene el nombre del comprador y lo usa para insertar la compra  
            Nombre_Comprador = self.campos['Nombre_Comprador'].get()

            execute_query(query, (ID_Elemento, Nombre_Comprador,))

            if self.importado.get():
                query = '''select ID from compra order by id desc limit 1;'''

                ID_Compra = execute_query(query)[0][0]

                query = '''insert into importacion (ID_Compra, Pais_proveniencia) values
                        (%s, %s);'''

                Pais_Proveniencia = self.campos['Pais_Proveniencia'].get()

                execute_query(query, (ID_Compra, Pais_Proveniencia,))

            return
        
        elif Tipo_Registro == "Donacion":

            id_donante = self.obtener_donante()
            unidad = self.campos['Unidad_Donante'].get()

            query = '''insert into donacion (ID_Elemento, ID_Donante, Nombre_unidad) values
                    (%s, %s,%s);'''

            execute_query(query, (ID_Elemento, id_donante,unidad,))
            return
        
        elif Tipo_Registro == "Dacion":
            query = '''insert into dacion (ID_Elemento, Concepto_DMT,Concepto_DSI,Ref_Resolucion) values
                    (%s, %s,%s,%s);'''

            DMT = self.campos['Concepto_DMT'].get()
            DSI = self.campos['Concepto_DSI'].get()
            Resolucion = self.campos['Resolucion'].get() 

            execute_query(query, (ID_Elemento, DMT,DSI,Resolucion,))
            return
        
        elif Tipo_Registro == "Fabricacion":
            query = '''insert into fabricados (ID_Elemento, Nombre_Fabricante,Avaluo_Fabricacion) values
                    (%s, %s,%s);'''
                    
            Fabricante = self.campos['Nombre_Fabricante'] 
            Avaluo = self.campos['Avaluo_Fabricacion'] 

            execute_query(query, (ID_Elemento, Fabricante,Avaluo,))
            return
        
        elif Tipo_Registro == "Comodato":
            query = '''insert into compra (ID_Elemento, Concepto_DMT,Concepto_DSI,Copia_Comodato) values
                    (%s, %s,%s,%s);'''

            DMT = self.campos['Concepto_DMT']
            DSI = self.campos['Concepto_DSI'] 
            Copia = self.campos['Copia'] 

            execute_query(query, (ID_Elemento, DMT,DSI,Copia,))
            return
        
        self.resultado_label.configure(text="Datos validados correctamente!", text_color="green")
