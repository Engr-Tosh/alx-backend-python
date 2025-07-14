# Creating a generator to stream rows from an SQL database one by on
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
password = os.getenv("DB_PASSWORD")

# First step is to establish a database connection.
def stream_users():
    try:
        print("Connecting to database...\n")
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = password,
            database = "ALX_prodev"

        )
        if connection:
            print("Database connected succesfully...\n")

        # Create a cursor to handle queries   
        cursor = connection.cursor()
        sql = "SELECT * FROM user_data;"
        cursor.execute(sql)

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            print("Streaming row:", row)
            yield row

    except mysql.connector.Error as err:
        print(f"There was a problem with the connection: {err}")
    
    finally:
        while cursor.nextset(): # If the cursor has unread results left, this will make sure it doesn't cause an error and pass over
            pass
        cursor.close()
        connection.close()

