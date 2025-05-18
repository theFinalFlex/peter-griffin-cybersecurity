import os
from download_podcast import download_podcast
from transcribe_audio import transcribe_audio
from peterify import peterify_transcript

def run_pipeline():
    """Run the complete brainrot pipeline."""
    print("🚀 Starting Brainrot Pipeline...")
    
    # Step 1: Download the podcast
    print("\n📥 Step 1: Downloading today's SANS Stormcast podcast...")
    audio_file = download_podcast()
    if not audio_file:
        print("❌ Failed to download podcast. Exiting...")
        return
    
    # Step 2: Transcribe the audio
    print("\n🎙️ Step 2: Transcribing the podcast...")
    transcript_file = transcribe_audio(audio_file)
    if not transcript_file:
        print("❌ Failed to transcribe audio. Exiting...")
        return
    
    # Step 3: Convert to Peter Griffin style
    print("\n🎭 Step 3: Converting to Peter Griffin-style commentary...")
    output_file = peterify_transcript(transcript_file)
    if not output_file:
        print("❌ Failed to generate Peter Griffin commentary. Exiting...")
        return
    
    print("\n✨ Pipeline completed successfully!")
    print(f"📝 Final output saved to: {output_file}")

if __name__ == "__main__":
    run_pipeline() 