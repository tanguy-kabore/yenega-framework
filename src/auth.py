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
                print("Username already exists.")
            else:
                hashed_password = Auth.hash_password(password)
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                values = (username, hashed_password)
                cursor.execute(insert_query, values)
                connection.commit()
                print("\tUser registered successfully.")
            cursor.close()
            connection.close()
        except Exception as e:
            print("An error occurred:", str(e))

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
                print("User information updated.")
            else:
                hashed_password = Auth.hash_password(password)
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                values = (username, hashed_password)
                cursor.execute(insert_query, values)
                connection.commit()
                print("\tUser registered successfully.")
            cursor.close()
            connection.close()
        except Exception as e:
            print("An error occurred:", str(e))

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
