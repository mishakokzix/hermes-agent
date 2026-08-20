import requests
import subprocess
import sys

def main():
    url = "https://heteronomous-bridally-minerva.ngrok-free.dev"
    headers = {"ngrok-skip-browser-warning": "true"}
    
    try:
        print(f"Fetching {url} ...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    # Check if the response body contains the string "false"
    if "false" in response.text:
        try:
            # Run runner.py (ensure it's in the same directory or adjust path)
            subprocess.run(["python", "backup.py"], check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(e.returncode)
        except FileNotFoundError:
            sys.exit(1)
    else:
        print("")

if __name__ == "__main__":
    main()
