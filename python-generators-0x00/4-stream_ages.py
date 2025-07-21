# Generator to compute memory efficient aggregate function

# Implement a generator that yields user ages
from seed import connect_to_prodev

def stream_user_ages():

    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute(f"SELECT age FROM user_data;")

    for row in cursor:
          yield row[0]  # Only one row selected, so the index should be 0
    
    conn.close() 


# Function to calculate the average age wihtout loading the entire database into memory 
def average_age():
      
      total_age = 0
      count = 0     # Initial count of data for total number
      
      for age in stream_user_ages():
            count += 1
            total_age += age

      average = total_age / count
      print(f"Average age of users: {average}")

average_age()