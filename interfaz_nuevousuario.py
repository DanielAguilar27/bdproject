from customtkinter import *
import re
from PIL import Image

class MainApp(CTk):
    

    def __init__(self):
        super().__init__()
        self.title("Registro usuario")
        self.geometry("1200x700")
      
     
        self.container = CTkFrame(self, fg_color="white") 
        self.container.pack(fill="both", expand=True)
        self.frames = {}
        self.show_frame(InterfazPrincipal)

    def show_frame(self, frame_class):
        # Ocultar el frame actual si ya hay uno visible
        for frame in self.frames.values():
            frame.pack_forget()

        # Crear la interfaz si no ha sido creada
        if frame_class not in self.frames:
            frame = frame_class(self.container, self)
            self.frames[frame_class] = frame
            frame.pack(fill="both", expand=True)

        # Mostrar la interfaz solicitada
        frame = self.frames[frame_class]
        frame.pack(fill="both", expand=True)

class InterfazPrincipal(CTkFrame):
    
    def __init__(self, parent, controller):
        
        def validar_datos():
            nombre = name_entry.get()
            apellido = lastname_entry.get()
            correo = mail_entry.get()
            password=passwd_entry.get()

            if not (nombre.replace(" ", "").isalpha() and apellido.replace(" ", "").isalpha()):
                resultado_label.configure(text="Nombre y apellido deben contener solo letras.", text_color="red")
                return

            # Validar el formato  correo electrónico
            patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(patron_correo, correo):
                resultado_label.configure(text="El correo electrónico no tiene un formato válido.", text_color="red")
                return
            patron_password = r"\d+"  #Expersion regular que valida que sea numero
            
            if not re.match(patron_password,password):
                resultado_label.configure(text="La contraseña solo debe tener numeros.", text_color="red")
                return

            resultado_label.configure(text="Validación exitosa.", text_color="green")
            
        super().__init__(parent, fg_color="white")  

        bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))

        bg_lab = CTkLabel(self, image=bg_img, text="")
        bg_lab.grid(row=0, column=0)

        frame1 = CTkFrame(self, fg_color="#D9D9D9", corner_radius=20)
        frame1.grid(row=0, column=1, padx=40)

        title = CTkLabel(frame1, text="Ingrese los datos de donacion: ", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        name_entry = CTkEntry(frame1, text_color="white", placeholder_text="Nombre responsable", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        name_entry.grid(row=1, column=0, sticky="nwe", padx=30, pady=5)
        
        lastname_entry = CTkEntry(frame1, text_color="white", placeholder_text="Apellidos", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        lastname_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=5)
        
        mail_entry = CTkEntry(frame1, text_color="white", placeholder_text="Correo Electronico", fg_color="black",
                                 placeholder_text_color="white", font=("", 16, "bold"), width=200,
                                 corner_radius=15, height=45)
        mail_entry.grid(row=3, column=0, sticky="nwe", padx=30, pady=5)
        

        passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Contraseña", fg_color="black",
                                placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15,
                                height=45, show="*")
        passwd_entry.grid(row=4, column=0, sticky="nwe", padx=30, pady=5)
        Regresar = CTkButton(frame1, text="Regresar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15)
        Regresar.grid(row=5, column=0, sticky="w", pady=20, padx=40)

        guardar = CTkButton(frame1, text="Guardar", font=("", 15, "bold"), height=40, width=70, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=validar_datos)
        guardar.grid(row=5, column=0, sticky="ne", pady=20, padx=35)
        resultado_label = CTkLabel(frame1, text="")
        resultado_label.grid(pady=10)


# Ejecución de la aplicación
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

