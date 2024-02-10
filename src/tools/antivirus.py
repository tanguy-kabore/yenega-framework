import pyclamd

class AntivirusScanner:
    @staticmethod
    def perform_scan(file_path):
        # Initialiser cd à None
        cd = None
        
        try:
            # Spécifier le chemin du socket Unix de clamd
            cd = pyclamd.ClamdAgnostic()

            # Tester si le serveur est accessible
            if cd.ping():
                print("Connection to ClamAV via Unix socket successful.")
            else:
                # Si la connexion échoue, tester avec un socket réseau
                cd = pyclamd.ClamdNetworkSocket()
                
                # Tester à nouveau la connexion
                if cd.ping():
                    print("Connection to ClamAV via network socket successful.")
                else:
                    raise ValueError("Could not connect to ClamAV server either by Unix or network socket.")

                # Afficher la version de ClamAV
                clamav_version = cd.version().split()[0]
                print(f"ClamAV Version: {clamav_version}")

                # Reloader les bases de données de ClamAV
                reload_result = cd.reload()
                print(f"ClamAV Reload Result: {reload_result}")

                # Afficher les statistiques de ClamAV
                stats_result = cd.stats().split()[0]
                print(f"ClamAV Statistics: {stats_result}")

        except pyclamd.ConnectionError:
            raise ValueError("Could not connect to ClamAV server either by Unix or network socket.")
        except Exception as e:
            # Afficher l'erreur pour le débogage
            print(f"Error: {str(e)}")

            # Vérifier si cd est toujours None avant de l'utiliser
            if cd is not None:
                # Scanner le fichier avec clamd
                scan_result = cd.scan_file(file_path)

                # Traiter le résultat de l'analyse
                if scan_result.get(file_path, '') == 'OK':
                    return "No threats found. File is clean."
                else:
                    return f"Threat Found: {scan_result.get(file_path, 'Unknown')}"

        # Cette section sera atteinte si aucune exception n'est levée
        return "Scanning completed."