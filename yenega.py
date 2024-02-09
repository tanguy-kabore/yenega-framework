import os
import argparse
import glob
import subprocess
from src.database import DB
from src.auth import Auth
from screen.auth.login import LoginScreen

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up two directories to reach the project directory
project_dir = os.path.abspath(os.path.join(current_dir))
# Create the main parser
parser = argparse.ArgumentParser(description='CLI du framework yenega')
# Define a command with its action
parser.add_argument('command', choices=['migrate', 'seed', 'start', 'update'], help='Available commands')

# Add optional command "refresh" associated with "migrate"
if 'migrate' in parser.parse_known_args()[0].command:
    parser.add_argument('--refresh', action='store_true', help='Refresh the database before migration. Use --refresh to delete all tables in the database before performing migration.')
    parser.add_argument('--reset', action='store_true', help='Drop all table in database.')
# Add optional command "refresh" associated with "migrate"
if 'seed' in parser.parse_known_args()[0].command:
    parser.add_argument('--admin', action='store_true', help="Create admin access. username='admin' and password='hash('admin')'.")
    parser.add_argument('--force', action='store_true', help="Force to recreate admin if already exist.")
# Parse the command-line arguments
args = parser.parse_args()

# Perform actions based on the chosen command
if args.command == 'migrate':
    # Specify the path to the folder containing SQL files
    folder_path = os.path.join(project_dir, 'database', 'migration')
    # Get a list of SQL files in the folder
    sql_files = glob.glob(os.path.join(folder_path, '*.sql'))
    print('Database migration started ...')
    if args.refresh:
        print('\tRefreshing database ...')
        DB.delete_all_tables()  # Call the method to delete all tables
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.create_table_from_sql_file(sql_file)
            print(f"\tSuccessfully Created table from SQL file: '{file_name}'.")
        print('\tDatabase refreshed successfully.')
    if args.reset:
        print('\tDropping all table ...')
        DB.delete_all_tables()  # Call the method to delete all tables
        print('\tAll table droped successfully.')
    else: 
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.create_table_from_sql_file(sql_file)
            print(f"\tSuccessfully Created table from SQL file: '{file_name}'.")
    print('Database migration finished successfully.')

elif args.command == 'seed':
    print('Database seed started ...')
    if args.admin:
        print('\tSeeding admin ...')
        Auth.register_user('admin', 'admin')
        print('\tadmin seeded successfully.')
        if args.force:
            print('\tForce to seed admin')
            Auth.force_register_user('admin', 'admin')
            print('\tadmin seeded successfully.')
    else:
        # Specify the path to the folder containing SQL files
        folder_path = os.path.join(project_dir, 'database', 'seeder')
        # Get a list of SQL files in the folder
        sql_files = glob.glob(os.path.join(folder_path, '*.sql'))
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.seed_table_from_sql_file(sql_file)
            print(f"\tSuccessfully seed table from SQL file: '{file_name}'.")
    print('Database seed finished successfully.')
elif args.command == 'update':
    print('Updating the code...')
    try:
        subprocess.check_output(['git', 'pull'], cwd=project_dir)
        print('Code updated successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error updating code: {e}')
        
elif args.command == 'start':
    print('Starting the application ...')
    # Appeler la fonction principale ou instancier la classe principale ici
    LoginScreen()

else:
    print('Invalid command. Use "migrate", "seed", "start", or "update".')