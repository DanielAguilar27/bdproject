from customtkinter import *
from tkinter import Canvas, Scrollbar
from PIL import Image
from controlador.conexion import execute_query

class InterfazTabla(CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Marco superior para el botón
        self.top_frame = CTkFrame(self, fg_color="white", corner_radius=20)
        self.top_frame.grid(row=0, column=0, padx=30, pady=(20, 10), sticky="ew")

        # Botón de "Nuevo Registro"
        nuevo_img = CTkImage(dark_image=Image.open("media/nuevoUsuario.png"), size=(50, 50))
        from interfaces.guardar import InterfazUsuario
        nuevo_usuario = CTkButton(
            self.top_frame, text="Nuevo Registro", font=("", 20, "bold"), fg_color="#0085FF",
            cursor="hand2", corner_radius=15, command=lambda: controller.show_frame(InterfazUsuario),
            image=nuevo_img, width=150, height=50
        )
        nuevo_usuario.pack(side="left", padx=10, pady=10)
        from interfaces.adminlogin import InterfazAdminLogin
        Regresar = CTkButton(self.top_frame, text="Regresar", font=("", 15, "bold"), height=50,
                             fg_color="#FF5C5C", cursor="hand2", corner_radius=15,
                             command=lambda: controller.show_frame(InterfazAdminLogin))
        Regresar.pack(side="left", padx=30, pady=10)

        # Canvas para la tabla
        self.canvas = Canvas(self, bg="#D9D9D9")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        self.h_scrollbar = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.h_scrollbar.grid(row=2, column=0, sticky="ew")

        self.v_scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.v_scrollbar.grid(row=1, column=1, sticky="ns")

        self.canvas.configure(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)

        self.scrollable_frame = CTkFrame(self.canvas, fg_color="white", corner_radius=20)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.table_frame = CTkFrame(self.scrollable_frame, fg_color="white", corner_radius=20)
        self.table_frame.grid(row=1, column=0, padx=30, pady=(10, 30), sticky="ew")

        self.entries = []
        self.actualizar_tabla()

    def actualizar_tabla(self):
                    
        query = '''select convert(s.ID_Tipo*100000 + s.ID_Subtipo*10000 + e.id_elemento,character) AS codigo,
                    e.Descripcion,
                    e.Cantidad,
                    e.Valor_Unitario as "Valor Unitario",
                    e.Estado,
                    e.Ubicacion,
                    CASE 
                        WHEN e2.ID_Facultad = f.ID_facultad THEN e2.Nombre 
                        WHEN f.ID_UAA = u.ID_UAA then f.Nombre 
                        ELSE u.Nombre 
                    END AS UAA,
                    i.Descripcion as Inconsistencia,
                    l.Nombre_Responsable as "Nombre del responsable",
                    l.Fecha_Salida as "Fecha Salida",
                    l.Fecha_Ingreso as "Fecha Ingreso",
                    e.Registro_Fotografico as "Registro Fotografico"
                    from inventario.elemento e
                    inner join inventario.subtipos s on s.ID_Subtipo  =  e.ID_Subtipo
                    inner join inventario.uaa u on u.ID_UAA  = e.ID_UAA
                    LEFT JOIN inventario.facultades f ON f.ID_UAA = u.ID_UAA
                    LEFT JOIN inventario.escuelas e2 ON e2.ID_Facultad = f.ID_facultad
                    inner join inventario.legalizacion l on l.ID_legalizacion  = e.ID_Legalizacion
                    left join inventario.inconsistencias i on i.ID_inconsistencia = e.ID_Inconsistencia
                    limit 25;'''
        rows = execute_query(query)

        for widget in self.table_frame.winfo_children():
            widget.grid_forget()

        headers = ["Codigo", "Descripcion","Cantidad", "Valor Unitario","Estado", 
                   "Ubicacion","UAA", "Inconsistencia","Nombre del responsable", 
                   "Fecha Salida","Fecha Ingreso", "Registro Fotografico"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.table_frame, text=header, text_color="black", font=("", 16, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        self.entries = []
        for i, row in enumerate(rows, start=1):
            row_entries = []
            for j, value in enumerate(row):
                entry = CTkEntry(self.table_frame, width=120)
                entry.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                entry.insert(0, str(value))  # Ensure value is a string
                entry.configure(state='readonly')
                row_entries.append(entry)

            edit_button = CTkButton(self.table_frame, text="Editar", command=lambda r=i: self.enable_edit(r))
            edit_button.grid(row=i, column=len(row), padx=5, pady=5, sticky="nsew")
            row_entries.append(edit_button)

            delete_button = CTkButton(self.table_frame, text="Eliminar", command=lambda r=i: self.delete_row())
            delete_button.grid(row=i, column=len(row) + 1, padx=5, pady=5, sticky="nsew")
            row_entries.append(delete_button)

            self.entries.append(row_entries)

        for col in range(len(headers)):
            self.table_frame.grid_columnconfigure(col, weight=1)

        self.table_frame.update_idletasks()

    def enable_edit(self, row):
        print(f"Enable edit for row {row}")

    def delete_row(self):
        codigo = self.entries[0][0].get()
        row_id = codigo[2:]
        query = "DELETE FROM elemento WHERE id = %s"
        execute_query(query, (int(row_id),))
        self.actualizar_tabla()
