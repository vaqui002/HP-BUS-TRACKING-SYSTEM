import mysql.connector

# Define database connection parameters
db_config = {
    "host": "sql12.freesqldatabase.com",
    "user": "sql12643803",
    "password": "yI6s7MmARh",
    "database": "sql12643803",
    "port": 3306,
}

try:
    # Establish a database connection
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("Connected to the database")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SQL queries and interact with the database

    query = "SELECT * FROM Bus_Route"  # Replace 'your_table_name' with your actual table name
    cursor.execute(query)

    # Fetch and process the results
    print("Fetching data from the database:")
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the cursor and database connection
    if 'connection' in locals():
        cursor.close()
        connection.close()
