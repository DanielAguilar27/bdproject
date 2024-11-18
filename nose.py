import customtkinter as ctk
import re

# Función de validación
def validar_datos():
    nombre = name_entry.get()
    apellido = last_name_entry.get()
    correo = email_entry.get()

    # Verificar que el nombre y apellido solo contengan letras
    if not (nombre.replace(" ", "").isalpha() and apellido.replace(" ", "").isalpha()):
        resultado_label.configure(text="Nombre y apellido deben contener solo letras.", text_color="red")
        return

    # Validar el formato del correo electrónico
    patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(patron_correo, correo):
        resultado_label.configure(text="El correo electrónico no tiene un formato válido.", text_color="red")
        return

    # Si todo está bien
    resultado_label.configure(text="Validación exitosa.", text_color="green")

# Configuración de la aplicación
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

app = ctk.CTk()
app.geometry("400x400")
app.title("Validación de Entradas")

# Campos de entrada
name_entry = ctk.CTkEntry(app, placeholder_text="Nombre")
name_entry.pack(pady=10)

last_name_entry = ctk.CTkEntry(app, placeholder_text="Apellido")
last_name_entry.pack(pady=10)

email_entry = ctk.CTkEntry(app, placeholder_text="Correo Electrónico")
email_entry.pack(pady=10)

# Botón para validar
validar_btn = ctk.CTkButton(app, text="Validar", command=validar_datos)
validar_btn.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=10)

# Ejecutar la aplicación
app.mainloop()
