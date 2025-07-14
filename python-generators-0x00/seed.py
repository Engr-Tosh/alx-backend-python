import mysql.connector
from contextlib import contextmanager

# Create a database connection to the mysl server
def connect_db():
    """
    This function creates a connection to a mysql database server    
    """
    print("Connecting to the server...")
    
    try:
        conn_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "benedictalovesme"
        )
        
        if conn_db.is_connected():
            print(f"The connection was successful to {conn_db.server_info} \n")        
        return conn_db
    

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

    
# Create a specific database connection
def create_database(connection):
    """
    This function connects to a database server, checks for a particular database, if doesn't exist, it is then created
    """
    # a connection is made to the sql server and a cursor activated to run queries
    cursor = connection.cursor()
    
    try:
        cursor.execute("SHOW DATABASES;")   # Outputs all available databases 
        databases = cursor.fetchall()
        
        if databases:
            print("The available databases are: \n")
            for database in databases:                
                print(f"{database}")

        else:
            print("No Databases yet...")


        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev'; ")    # Checks for a specific database 
        db_query_result = cursor.fetchone()

        if db_query_result:
            print(f"The {db_query_result[0]} database is available...")
        else:
            print("Database not available, creating database...")
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS ALX_prodev;"
            )
            print(f"Database created successfully")
            

    except (TypeError, mysql.connector.InternalError, mysql.connector.Error) as err:
        print(err)

    finally:
        cursor.close()
    
 

# Create a connection to the specific database
def connect_to_prodev():
    """
    This function creates a connection to the specified database in MySQL
    """
    print("\n")
    print("Connecting to the prodev database...")
    prodev_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "benedictalovesme",
        database = "ALX_prodev"
    )
    
    if prodev_db.is_connected():
        print("ALX_prodev DB connected successfully")
    return prodev_db



# Create a table with required fields in prodev database
def create_table(connection):
    """This function creates a table in the specified db"""
    try:
        # connection = connect_to_prodev()
        cursor = connection.cursor()

        # sql to create the table
        sql = "CREATE TABLE IF NOT EXISTS user_data(user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(150) NOT NULL, email VARCHAR(150) NOT NULL,age DECIMAL(4, 1) NOT NULL);"
        cursor.execute(sql)
    
    finally:
        cursor.close()

# Inserts/streams data into the database using a generator
def insert_data(connection, data):
    """
    This function inserts data in the database if it does not exist
    """
    # connection = connect_to_prodev()
    cursor = connection.cursor()
    sql = "INSERT INTO user_data (name, email, age) VALUES(%s, %s, %s)"

    # Bring in the file that contains the data to be inserted.
    import csv
    try:
        with open(data, 'r') as file: # using a resource manager, the file is called and opened
            reader = csv.reader(file)
            next(reader) # Skips the header row.

            for row in reader:
                cursor.execute(sql, (row[0], row[1], row[2]))
    
    except mysql.connector.Error as err:
        print(err)
    
    finally:
        connection.commit()
        cursor.close()