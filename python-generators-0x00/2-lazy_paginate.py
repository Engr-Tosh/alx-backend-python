# Fetch paginated data from the users database using a generator to lazily load each page

from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """
    Returns a list of user records from the database using LIMIT and OFFSET.
    """
    
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")

    rows = cursor.fetchall()
    
    connection.close()
    return rows



def lazy_paginate(page_size):
    """
    Fetches paginated data from the users databse using a generator to lazily load each page
    """

    offset = 0  # Starts at offset 0

    while True:
        rows = paginate_users(page_size, offset)    # Fetch a page of users
        if rows == []:      # If the page is empty stops the loop
            break

        for user in rows:
            
            yield user      # Yield each user in the current page
            
        offset += page_size  # After yielding all users in the page increase the offset by page size