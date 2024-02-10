import subprocess

class AntivirusScanner:
    @staticmethod
    def perform_scan(file_path):
        try:
            result = subprocess.run(['clamscan', '--no-summary', file_path], capture_output=True, text=True)

            if result.returncode == 0:
                return "No threats found. File is clean."
            elif result.returncode == 1:
                return "Threat Found: Malware detected."
            else:
                return f"Error occurred during the scan. ClamAV returned {result.returncode}"

        except Exception as e:
            return f"Error: {str(e)}"