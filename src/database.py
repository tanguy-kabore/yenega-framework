import mysql.connector # pip install mysql-connector-python
from env import DATABASE, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

class DB:

    @staticmethod
    def connection():
        try:
            if  DATABASE == "mysql":
                # Establish a connection to the MySQL database
                connection = mysql.connector.connect(
                    host= DATABASE_HOST[0].strip(),
                    user= DATABASE_USER[0].strip(),
                    password= DATABASE_PASSWORD[0].strip(),
                )
                print(f"Successfully connected on database '{DATABASE}'.")
                return connection
            else:
                print(f"'{DATABASE}' is not supported")
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database.")

    @staticmethod
    def db_create(database_name):
        connection = DB.connection()
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        # Check if the database already exists
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        existing_databases = [db[0] for db in databases]
        if database_name in existing_databases:
            print(f"Database '{database_name}' already exists. No action required.")
        else:
            # Create the database
            cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database '{database_name}' created successfully.")
        # Close the cursor and connection
        cursor.close()
        connection.close()

    @staticmethod
    def db_connection():
        DB.db_create(DATABASE_NAME)
        try:
            if  DATABASE == "mysql":
                # Establish a connection to the MySQL database
                connection = mysql.connector.connect(
                    host= DATABASE_HOST[0].strip(),
                    database= DATABASE_NAME,
                    user= DATABASE_USER[0].strip(),
                    password= DATABASE_PASSWORD[0].strip(),
                )
                print(f"Database '{DATABASE_NAME}' is successfully selected.")
                return connection
            else:
                print(f"'{DATABASE}' is not supported")
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database.")

    @staticmethod
    def create_table_from_sql_file(sql_file_path):
        connection = DB.db_connection()
        # Read the SQL file
        with open(sql_file_path, 'r') as file:
            sql_statements = file.read()
        # Split SQL statements into individual statements
        statements = sql_statements.split(';')
        # Execute each statement
        cursor = connection.cursor()
        for statement in statements:
            statement = statement.strip()
            if statement:
                cursor.execute(statement)
        # Commit the changes
        connection.commit()
        cursor.close()
        connection.close()
    
    def delete_all_tables():
        # Connect to the MySQL database
        connection = DB.db_connection()
        cursor = connection.cursor()
        # Retrieve the list of table names
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        # Iterate through the table names and drop each table
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"Table '{table_name}' dropped.")
        # Commit the changes and close the connection
        connection.commit()
        connection.close()
