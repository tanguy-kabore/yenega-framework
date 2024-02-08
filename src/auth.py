import mysql.connector
from mysql.connector import errorcode
import bcrypt # pip install bcrypt
from src.database import DB

class Auth:

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    @staticmethod
    def register_user(username, password):
        try:
            connection = DB.db_connection()
            cursor = connection.cursor()
            
            # Check if the username already exists in the database
            select_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(select_query, (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                print("\tUsername already exists.")
            else:
                hashed_password = Auth.hash_password(password)
                
                # Insert the user into the users table
                insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                values = (username, hashed_password)
                cursor.execute(insert_user_query, values)
                
                # Get the ID of the newly inserted user
                user_id = cursor.lastrowid
                
                # Get the ID of the "admin" role from the roles table
                select_role_query = "SELECT id FROM roles WHERE name = 'admin'"
                cursor.execute(select_role_query)
                admin_role_id = cursor.fetchone()[0]
                
                # Insert the user role into the user_roles table
                insert_user_role_query = "INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)"
                user_role_values = (user_id, admin_role_id)
                cursor.execute(insert_user_role_query, user_role_values)
                
                connection.commit()
                print("\tUser registered successfully with admin role.")
            
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
    def force_register_user(username, password):
        try:
            connection = DB.db_connection()
            cursor = connection.cursor()

            # Check if the username already exists in the database
            select_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(select_query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                # Update the user's information
                hashed_password = Auth.hash_password(password)
                update_query = "UPDATE users SET password = %s WHERE username = %s"
                values = (hashed_password, username)
                cursor.execute(update_query, values)
                connection.commit()
                print("\tUser information updated.")
            else:
                # Insert the user into the users table
                hashed_password = Auth.hash_password(password)
                insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                values = (username, hashed_password)
                cursor.execute(insert_user_query, values)
                connection.commit()
                print("\tUser registered successfully.")

                # Get the ID of the newly inserted user
                user_id = cursor.lastrowid

                # Get the ID of the "admin" role from the roles table
                select_role_query = "SELECT id FROM roles WHERE name = 'admin'"
                cursor.execute(select_role_query)
                admin_role_id = cursor.fetchone()[0]

                # Insert the user role into the user_roles table
                insert_user_role_query = "INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)"
                user_role_values = (user_id, admin_role_id)
                cursor.execute(insert_user_role_query, user_role_values)
                connection.commit()
                print("\tUser registered successfully with admin role.")

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
    def validate_login(username, password):
        try:
            select_query = "SELECT password FROM users WHERE username = %s"
            connection = DB.db_connection()
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            cursor.execute(select_query, (username,))
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            if row:
                hashed_password = row[0]
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    print("Login successful.")
                    return True
                else:
                    print("Incorrect password.")
                    return False
            else:
                print("User not found.")
                return False
        except Exception as e:
            print("An error occurred:", str(e))