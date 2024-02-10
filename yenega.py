import os
import argparse
import glob
import platform
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
parser.add_argument('command', choices=['migrate', 'seed', 'start', 'update', 'clean', 'get'], help='Available commands')
parser.add_argument("project_name", nargs="?", help="Specify the project name.")
parser.add_argument("--dependencies", nargs="+", help="Specify dependencies for 'get' command.")

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

# Define ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def install_dependencies(project_name, dependencies):
    activate_env_command = os.path.join(project_name, "venv", "Scripts", "activate") if platform.system() == "Windows" \
        else f"source {os.path.join(project_name, 'venv', 'bin', 'activate')}"

    subprocess.run(activate_env_command, shell=True)

    try:
        subprocess.run(["python", "-m", "pip", "install", "--upgrade"] + dependencies, check=True)
        print(f"{Colors.OKGREEN}Dependencies installed/updated successfully: {', '.join(dependencies)}{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Error occurred during dependency installation/update: {e}{Colors.ENDC}")

def clean_dependencies(project_name):
    activate_env_command = os.path.join(project_name, "venv", "Scripts", "activate") if platform.system() == "Windows" \
        else f"source {os.path.join(project_name, 'venv', 'bin', 'activate')}"

    subprocess.run(activate_env_command, shell=True)

    try:
        subprocess.run(["python", "-m", "pip", "freeze", "--local"], stdout=subprocess.PIPE, check=True)
        subprocess.run(["grep", "-v", "^#"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, check=True)
        subprocess.run(["xargs", "pip", "uninstall", "-y"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, check=True, shell=True)
        print(f"{Colors.OKGREEN}Cleaned all dependencies from the virtual environment.{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Error occurred during dependency cleanup: {e}{Colors.ENDC}")

# Perform actions based on the chosen command
if args.command == 'migrate':
    # Specify the path to the folder containing SQL files
    folder_path = os.path.join(project_dir, 'database', 'migration')
    # Get a list of SQL files in the folder
    sql_files = glob.glob(os.path.join(folder_path, '*.sql'))

    print(f'{Colors.OKBLUE}Database migration started ...{Colors.ENDC}')

    if args.refresh:
        print(f'{Colors.OKCYAN}\tRefreshing database ...{Colors.ENDC}')
        DB.delete_all_tables()  # Call the method to delete all tables
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.create_table_from_sql_file(sql_file)
            print(f"{Colors.OKGREEN}\tSuccessfully Created table from SQL file: '{file_name}'.{Colors.ENDC}")
        print(f'{Colors.OKCYAN}\tDatabase refreshed successfully.{Colors.ENDC}')

    if args.reset:
        print(f'{Colors.WARNING}\tDropping all table ...{Colors.ENDC}')
        DB.delete_all_tables()  # Call the method to delete all tables
        print(f'{Colors.WARNING}\tAll table dropped successfully.{Colors.ENDC}')
    else:
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.create_table_from_sql_file(sql_file)
            print(f"{Colors.OKGREEN}\tSuccessfully Created table from SQL file: '{file_name}'.{Colors.ENDC}")

    print(f'{Colors.OKBLUE}Database migration finished successfully.{Colors.ENDC}')

elif args.command == 'seed':
    print(f'{Colors.OKBLUE}Database seed started ...{Colors.ENDC}')

    if args.admin:
        print(f'{Colors.OKCYAN}\tSeeding admin ...{Colors.ENDC}')
        Auth.register_user('admin', 'admin')
        print(f'{Colors.OKGREEN}\tadmin seeded successfully.{Colors.ENDC}')

        if args.force:
            print(f'{Colors.WARNING}\tForce to seed admin{Colors.ENDC}')
            Auth.force_register_user('admin', 'admin')
            print(f'{Colors.OKGREEN}\tadmin seeded successfully.{Colors.ENDC}')
    else:
        # Specify the path to the folder containing SQL files
        folder_path = os.path.join(project_dir, 'database', 'seeder')
        # Get a list of SQL files in the folder
        sql_files = glob.glob(os.path.join(folder_path, '*.sql'))
        # Iterate through each SQL file and create tables
        for sql_file in sql_files:
            file_name = os.path.basename(sql_file)
            DB.seed_table_from_sql_file(sql_file)
            print(f"{Colors.OKGREEN}\tSuccessfully seed table from SQL file: '{file_name}'.{Colors.ENDC}")

    print(f'{Colors.OKBLUE}Database seed finished successfully.{Colors.ENDC}')

elif args.command == 'update':
    print(f'{Colors.OKBLUE}Updating the code...{Colors.ENDC}')

    try:
        subprocess.check_output(['git', 'pull'], cwd=project_dir)
        print(f'{Colors.OKGREEN}Code updated successfully.{Colors.ENDC}')
    except subprocess.CalledProcessError as e:
        print(f'{Colors.FAIL}Error updating code: {e}{Colors.ENDC}')

elif args.command == 'start':
    print(f'{Colors.OKBLUE}Starting the application ...{Colors.ENDC}')
    # Appeler la fonction principale ou instancier la classe principale ici
    LoginScreen()

elif args.command == 'clean':
    clean_dependencies(project_dir)

elif args.command == 'get':
    print(f'{Colors.OKBLUE}Getting dependencies...{Colors.ENDC}')

    # Vérifiez si l'argument --dependencies est fourni
    if args.dependencies:
        dependencies = args.dependencies
    else:
        # Si non fourni, utilisez une liste prédéfinie
        dependencies = ["mysql-connector-python", "Pillow", "clamd"]
    
    # Installez les dépendances
    install_dependencies(project_dir, dependencies)

else:
    print(f'{Colors.FAIL}Invalid command. Use "migrate", "seed", "start", "update", "clean", or "get".{Colors.ENDC}')