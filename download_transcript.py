import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('transcript_download.log'),
        logging.StreamHandler()
    ]
)

def get_latest_transcript():
    """Download the latest SANS Stormcast transcript"""
    
    # SANS Stormcast RSS feed URL
    url = "https://isc.sans.edu/podcast.xml"
    
    try:
        # Get the RSS feed
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the XML
        soup = BeautifulSoup(response.content, 'xml')
        
        # Get the latest episode
        latest_item = soup.find('item')
        if not latest_item:
            raise Exception("No episodes found in the feed")
        
        # Get the transcript URL
        transcript_url = latest_item.find('link').text
        
        # Get the transcript content
        transcript_response = requests.get(transcript_url)
        transcript_response.raise_for_status()
        
        # Parse the transcript page
        transcript_soup = BeautifulSoup(transcript_response.content, 'html.parser')
        
        # Find the transcript content (this selector might need adjustment)
        transcript_content = transcript_soup.find('div', class_='transcript-content')
        if not transcript_content:
            raise Exception("Could not find transcript content on the page")
        
        # Create transcripts directory if it doesn't exist
        os.makedirs('transcripts', exist_ok=True)
        
        # Save the transcript
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f'transcripts/stormcast_{date_str}_transcript.txt'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(transcript_content.get_text())
        
        logging.info(f"Successfully downloaded transcript to {filename}")
        return filename
        
    except Exception as e:
        logging.error(f"Error downloading transcript: {e}")
        raise

if __name__ == "__main__":
    get_latest_transcript() 