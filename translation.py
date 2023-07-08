from env import LANG

if LANG == 'en':
    LOGIN_HEAD = "Login"
    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    SHOW_PASSWORD_LABEL = "Show Password"
    SUBMIT_LABEL = "Submit"

    INCORRECT_PASSWORD = "Incorrect password"
    USER_NOT_FOUND = "User not found"
    MSG_ERROR_LABEL = "Error"
    MSG_QUIT_LABEL = "Quit"
    DATABASE_CONNECTION_ERROR = "Error connecting to MySQL database."
    QUIT_QUESTION = "Are you sure you want to quit?"

    OR = "or"
    QUIT_MENU = "Quit"
    FILE_MENU = "File"
    pass
elif LANG == 'fr':
    LOGIN_HEAD = "Connexion"
    USERNAME_LABEL = "Nom d'utilisateur"
    PASSWORD_LABEL = "Mot de passe"
    SHOW_PASSWORD_LABEL = "Montrer le mot de passe"
    SUBMIT_LABEL = "Envoyer"

    INCORRECT_PASSWORD = "Mot de passe incorrect"
    USER_NOT_FOUND = "Aucun utilisateur trouvé"
    MSG_ERROR_LABEL = "Erreur"
    MSG_QUIT_LABEL = "Quitter"
    DATABASE_CONNECTION_ERROR = "Erreur lors de la connexion à la base de données."
    QUIT_QUESTION = "Etes vous sûr de vouloir quitter?"

    OR = "ou"
    QUIT_MENU = "Quitter"
    FILE_MENU = "Fichier"
    pass
else:
    # code
    pass
