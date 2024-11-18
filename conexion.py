import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='admin')
    def crearusuario(self):
        sql= "INSERT INTO usuario VALUES (1,usuario,contraseña)"
    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx 
class Guardar():   
    def __init__(self):
        pass
    def guardar_usuario(nombre, correo, contrasena):
        try:
            # Conexión a la base de datos
            connection = mysql.connector.connect(
                host="localhost",        # Dirección del servidor MySQL
                user="root",             # Usuario de MySQL
                password="",             # Contraseña (vacía por defecto en XAMPP)
                database="nombre_base_datos"  # Nombre de tu base de datos
            )

            if connection.is_connected():
                cursor = connection.cursor()

                # Consulta SQL para insertar un nuevo usuario
                query = """
                    INSERT INTO usuarios (nombre, correo, contraseña)
                    VALUES (%s, %s, %s)
                """
                valores = (nombre, correo, contrasena)

                # Ejecutar la consulta
                cursor.execute(query, valores)

                # Confirmar los cambios
                connection.commit()

                print(f"Usuario '{nombre}' guardado correctamente.")



        finally:
            # Cerrar la conexión
            if connection.is_connected():
                cursor.close()
                connection.close()

