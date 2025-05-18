import os
import requests
from datetime import datetime

def download_podcast(output_dir="downloads", mp3_url=None):
    """
    Download a SANS Stormcast podcast from a direct MP3 URL.
    
    Args:
        output_dir (str): Directory to save the podcast
        mp3_url (str, optional): Direct MP3 URL to download. If None, returns None.
    
    Returns:
        str: Path to the downloaded podcast file, or None if download failed
    """
    if not mp3_url:
        print("❌ No MP3 URL provided.")
        return None

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate output filename
    today = datetime.now()
    output_file = os.path.join(output_dir, f"stormcast_{today.strftime('%Y-%m-%d')}.mp3")

    try:
        print(f"Downloading podcast from {mp3_url}...")
        response = requests.get(mp3_url, stream=True)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded podcast to {output_file}")
        return output_file
    except Exception as e:
        print(f"Error downloading podcast: {e}")
        return None

if __name__ == "__main__":
    # Example: Download today's episode
    mp3_url = "https://traffic.libsyn.com/securitypodcast/9454.mp3"
    download_podcast(mp3_url=mp3_url) 