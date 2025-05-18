import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def peterify_transcript(transcript_file, output_file="peter_commentary.txt"):
    """
    Convert transcript into Peter Griffin-style commentary using OpenAI's API.
    
    Args:
        transcript_file (str): Path to the transcript file
        output_file (str): Path to save the Peter Griffin-style commentary
    
    Returns:
        str: Path to the output file
    """
    # Set OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Read the transcript
    with open(transcript_file, "r", encoding="utf-8") as f:
        transcript = f.read()
    
    # Create the prompt for Peter Griffin-style transformation
    prompt = f"""Transform this cybersecurity news transcript into a chaotic, humorous commentary in Peter Griffin's voice. \
Make it sound like an Instagram Reel news commentary. Include his characteristic speech patterns, \
random tangents, and reactions. Keep the core information but make it entertaining and over-the-top:\n\n{transcript}"""
    
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are Peter Griffin from Family Guy, providing chaotic and humorous commentary on cybersecurity news."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=2000
        )
        
        # Extract the generated text
        peter_commentary = response["choices"][0]["message"]["content"]
        
        # Save the commentary
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(peter_commentary)
        
        print(f"Peter Griffin-style commentary saved to {output_file}")
        return output_file
    
    except Exception as e:
        print(f"Error generating Peter Griffin commentary: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    transcript_file = "transcripts/stormcast_2024-03-21_transcript.txt"  # Update with your transcript file path
    peterify_transcript(transcript_file) 