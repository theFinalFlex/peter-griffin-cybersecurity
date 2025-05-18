import schedule
import time
import logging
from datetime import datetime
from download_transcript import get_latest_transcript
from process_transcript import process_transcript
from generate_video import process_segments

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()
    ]
)

def run_pipeline():
    """Run the complete pipeline: download transcript, process it, and generate videos"""
    try:
        logging.info("Starting pipeline run")
        
        # Download the latest transcript
        transcript_file = get_latest_transcript()
        
        # Process the transcript into segments
        process_transcript(transcript_file, 'segments')
        
        # Generate videos from segments
        process_segments()
        
        logging.info("Pipeline run completed successfully")
        
    except Exception as e:
        logging.error(f"Pipeline run failed: {e}")

def main():
    # Run immediately on startup
    run_pipeline()
    
    # Schedule to run daily at 9 AM
    schedule.every().day.at("09:00").do(run_pipeline)
    
    logging.info("Pipeline scheduled to run daily at 09:00")
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 