import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def transcribe_audio(audio_file, output_dir="transcripts"):
    """
    Transcribe audio file using OpenAI's API.
    
    Args:
        audio_file (str): Path to the audio file
        output_dir (str): Directory to save the transcript
    
    Returns:
        str: Path to the transcript file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Set OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        # Open the audio file
        with open(audio_file, "rb") as audio:
            # Transcribe the audio
            print(f"Transcribing {audio_file}...")
            transcript = openai.Audio.transcribe(
                model="whisper-1",
                file=audio
            )
        
        # Save the transcript
        output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(audio_file))[0]}_transcript.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript.text)
        
        print(f"Transcript saved to {output_file}")
        return output_file
    
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    audio_file = "downloads/stormcast_2025-05-17.mp3"  # Use the latest downloaded file
    transcribe_audio(audio_file) 