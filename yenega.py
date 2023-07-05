import os
import argparse
import glob
from path import path
from src.database import DB

# Create the main parser
parser = argparse.ArgumentParser(description='CLI du framework yenega')
# Define a command with its action
parser.add_argument('command', choices=['migrate', 'command2'], help='Available commands')

# Add optional command "refresh" associated with "migrate"
if 'migrate' in parser.parse_known_args()[0].command:
    parser.add_argument('--refresh', action='store_true', help='Refresh the database before migration. Use --refresh to delete all tables in the database before performing migration.')

# Parse the command-line arguments
args = parser.parse_args()

# Perform actions based on the chosen command
if args.command == 'migrate':
    if args.refresh:
        print('Refreshing database ...')
        DB.delete_all_tables()  # Call the method to delete all tables
        print('Database refreshed successfully.')
    print('Database migration started ...')
    # Specify the path to the folder containing SQL files
    folder_path = path('database\migrations')
    # Get a list of SQL files in the folder
    sql_files = glob.glob(folder_path + '\*.sql')
    # Iterate through each SQL file and create tables
    for sql_file in sql_files:
        file_name = os.path.basename(sql_file)
        DB.create_table_from_sql_file(sql_file)
        print(f"Successfully Created table from SQL file: '{file_name}'.")
    print('Database migration finished successfully.')
elif args.command == 'command2':
    print('Running Command 2...')
    # Add your logic for Command 2 here