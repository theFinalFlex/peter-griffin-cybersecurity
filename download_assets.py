import os
import requests
from pathlib import Path

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

def main():
    # Create directories
    os.makedirs("assets/gameplay", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    # Download technology logos
    logos = {
        "chrome_logo.png": "https://www.google.com/chrome/static/images/chrome-logo.svg",
        "google_logo.png": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "sonicwall_logo.png": "https://www.sonicwall.com/wp-content/themes/sonicwall/images/sonicwall-logo.svg",
        "vmware_logo.png": "https://www.vmware.com/content/dam/digitalmarketing/vmware/en/images/logo/vmware-logo.svg",
        "security_icon.png": "https://cdn-icons-png.flaticon.com/512/2092/2092663.png",
        "hacker_icon.png": "https://cdn-icons-png.flaticon.com/512/2092/2092663.png",
        "vulnerability_icon.png": "https://cdn-icons-png.flaticon.com/512/2092/2092663.png"
    }
    
    for filename, url in logos.items():
        filepath = os.path.join("assets/images", filename)
        download_file(url, filepath)
    
    # Download a sample gameplay video (Subway Surfers gameplay)
    gameplay_url = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"
    gameplay_path = os.path.join("assets/gameplay", "gameplay.mp4")
    download_file(gameplay_url, gameplay_path)

if __name__ == "__main__":
    main() 