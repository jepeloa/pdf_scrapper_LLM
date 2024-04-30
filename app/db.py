import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

def store_processed_files(pdf_file):
    """ Conecta a MySQL y recupera algunos datos. """
    #guarda en la base de datps
    try:
        # Configuración de la conexión
        connection = mysql.connector.connect(
            host='mysql',  # Usamos el nombre del servicio definido en docker-compose.yml
            #user=os.getenv('MYSQL_USER'),  # El usuario de MySQL que definiste
            user='root',
            password=os.getenv('MYSQL_ROOT_PASSWORD'),  # La contraseña para el usuario de MySQL
            database=os.getenv('MYSQL_DATABASE') # El nombre de la base de datos
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            #quiero crear la tabla si no exite
            cursor.execute("CREATE table IF NOT EXISTS processed_files (filename TEXT);")
            sql = "INSERT INTO processed_files (filename) VALUES (%s)"
            val = (str(pdf_file),)
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "registro insertado.")
            print(cursor.lastrowid)
            print("Registro insertado correctamente.")
    except Error as e:
        print("Error durante la conexión o la consulta", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")
        

    

def connect_fetch(input,keys):
    """ Conecta a MySQL y recupera algunos datos. """
    #guarda en la base de datps
    try:
        # Configuración de la conexión
        connection = mysql.connector.connect(
            host='mysql',  # Usamos el nombre del servicio definido en docker-compose.yml
            #user=os.getenv('MYSQL_USER'),  # El usuario de MySQL que definiste
            user='root',
            password=os.getenv('MYSQL_ROOT_PASSWORD'),  # La contraseña para el usuario de MySQL
            database=os.getenv('MYSQL_DATABASE') # El nombre de la base de datos
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            for key in keys:
                r=input[key]['R']
                raw_text=input[key]['raw_text_1']
                start_page=input[key]['start_page']
                print(r)
                end_page=input[key]['end_page']
                pdf_name=input[key]['pdf_name']
                MODEL_NAME = os.getenv('MODEL')
                #quiero crear la tabla si no exite
                cursor.execute("CREATE table IF NOT EXISTS results (key_question TEXT, r TEXT, raw_text TEXT, start_page INT, end_page INT, pdf_name TEXT, model TEXT);")
                sql = "INSERT INTO results (key_question, r, raw_text, start_page, end_page, pdf_name, model) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (key, r, raw_text, start_page, end_page, pdf_name, MODEL_NAME)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "registro insertado.")
                print(cursor.lastrowid)
                print("Registro insertado correctamente.")
    except Error as e:
        print("Error durante la conexión o la consulta", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

def read_processed_files(pdf_file):
     try:
        # Configuración de la conexión
        connection = mysql.connector.connect(
            host='mysql',  # Usamos el nombre del servicio definido en docker-compose.yml
            #user=os.getenv('MYSQL_USER'),  # El usuario de MySQL que definiste
            user='root',
            password=os.getenv('MYSQL_ROOT_PASSWORD'),  # La contraseña para el usuario de MySQL
            database=os.getenv('MYSQL_DATABASE') # El nombre de la base de datos
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT filename FROM processed_files WHERE filename = %s", (str(pdf_file),))
            file_result=cursor.fetchone()
     except Error as e:
        print("Error durante la conexión o la consulta", e)
        return 'error'
     finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")
            return file_result
    
    
    
        



