import mysql.connector # pip install mysql-connector-python
from mysql.connector import errorcode
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
                print(f"\tSuccessfully connected on database '{DATABASE}'.")
                return connection
            else:
                print(f"'{DATABASE}' is not supported")
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))

    @staticmethod
    def db_create(database_name):
        try:
            connection = DB.connection()
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            # Check if the database already exists
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            existing_databases = [db[0] for db in databases]
            if database_name in existing_databases:
                print(f"\tDatabase '{database_name}' already exists. No action required.")
            else:
                # Create the database
                cursor.execute(f"CREATE DATABASE {database_name}")
                print(f"\tDatabase '{database_name}' created successfully.")
            # Close the cursor and connection
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))

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
                print(f"\tDatabase '{DATABASE_NAME}' is successfully selected.")
                return connection
            else:
                print(f"\t'{DATABASE}' is not supported")
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))

    @staticmethod
    def create_table_from_sql_file(sql_file_path):
        try:
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
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))
    
    @staticmethod
    def seed_table_from_sql_file(sql_file_path):
        try:
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
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))

    @staticmethod
    def delete_all_tables():
        try:
            # Connect to the MySQL database
            connection = DB.db_connection()
            cursor = connection.cursor()
            # Get the list of foreign keys for the user_roles table
            cursor.execute("SELECT CONSTRAINT_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = 'user_roles' AND REFERENCED_TABLE_NAME IS NOT NULL")
            # Fetch all the foreign keys
            foreign_keys = cursor.fetchall()
            # Generate the ALTER TABLE statements to drop each foreign key
            alter_table_statements = []
            for fk in foreign_keys:
                constraint_name = fk[0]
                alter_table_statement = f"ALTER TABLE user_roles DROP FOREIGN KEY {constraint_name}"
                alter_table_statements.append(alter_table_statement)
            # Execute the ALTER TABLE statements to drop the foreign keys
            for alter_table_statement in alter_table_statements:
                cursor.execute(alter_table_statement)
            # Retrieve the list of table names
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            # Iterate through the table names and drop each table
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DROP TABLE {table_name}")
                print(f"\tTable '{table_name}' dropped.")
            # Commit the changes and close the connection
            connection.commit()
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\tAccess denied.')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('\tDatabase does not exist.')
            else:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print('\tData duplicate:', str(e))
                else:
                    print('\tAn error occurred:', str(e))
