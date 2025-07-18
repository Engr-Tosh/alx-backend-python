# Script to use a generator to fetch and process data in batches

# Create database connection
# Connect cursor to handle queries
# Use yield to return results

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
password = os.getenv("DB_PASSWORD")

def stream_users_in_batches(batch_size):
    """
    This function fetches rows in batches
    """
    
    try:
        print("Connecting to the database...")
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "ALX_prodev",
            password = password
        )                                                                   

        if conn:
            print("DB connected successfully")      # Created db connection

        cursor = conn.cursor()      # Created cursor connection. Handles queries
        sql = "SELECT * FROM user_data;"
        cursor.execute(sql)  # Loads up the data into a variable

        while True:
            rows = cursor.fetchmany(batch_size)
            yield rows
            
            if not rows:
                break

    except mysql.connector.Error as err:
        raise err
    
    finally:
        while cursor.nextset():
            pass
        cursor.close()
        conn.close()


# Batch processing function to filter users over the age of 25
def batch_processing(batch_size):
    """
    Processes users in batches and yields the users over the age of 25
    """
    
    try:
        batches = stream_users_in_batches(batch_size)

        for batch in batches:
            for row in batch:
                if row[3] >= 25:
                    yield row
    
    except mysql.connector.Error as err:
        raise err
