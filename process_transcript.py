import re
import os
from datetime import datetime
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def clean_transcript(text):
    # Remove extra whitespace and normalize text
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_stories(text):
    # Split text into stories based on key phrases that indicate new topics
    story_markers = [
        "And Google released",
        "Now earlier this week",
        "And ESET is reporting",
    ]
    
    stories = []
    current_story = text
    
    for marker in story_markers:
        if marker in current_story:
            parts = current_story.split(marker, 1)
            if parts[0].strip():
                stories.append(parts[0].strip())
            current_story = marker + parts[1]
    
    if current_story.strip():
        stories.append(current_story.strip())
    
    return stories

def generate_peter_script(story):
    """Use OpenAI to generate a Peter Griffin style script from the story"""
    
    prompt = f"""Transform this cybersecurity news story into a script in Peter Griffin's voice. 
    Make it funny and entertaining while keeping the technical details accurate.
    Include:
    1. A simplified explanation of the technical issue
    2. A funny analogy that helps explain it
    3. Peter Griffin's characteristic speech patterns and reactions
    
    Original story:
    {story}
    
    Requirements:
    - Keep it under 200 words
    - Make it technically accurate but easy to understand
    - Use Peter Griffin's speech patterns (stuttering, random emphasis, characteristic phrases)
    - Add a meme-worthy analogy
    - End with a characteristic Peter Griffin reaction
    
    Format the response as:
    SCRIPT: [the script]
    ANALOGY: [the analogy]
    REACTION: [Peter's reaction]"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative writer who specializes in transforming technical content into entertaining scripts in Peter Griffin's voice."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Parse the response
        content = response.choices[0].message.content
        
        # Extract the different parts
        script_match = re.search(r'SCRIPT: (.*?)(?=ANALOGY:|$)', content, re.DOTALL)
        analogy_match = re.search(r'ANALOGY: (.*?)(?=REACTION:|$)', content, re.DOTALL)
        reaction_match = re.search(r'REACTION: (.*?)$', content, re.DOTALL)
        
        script = script_match.group(1).strip() if script_match else ""
        analogy = analogy_match.group(1).strip() if analogy_match else ""
        reaction = reaction_match.group(1).strip() if reaction_match else ""
        
        # Combine the parts
        final_script = f"{script}\n\n{analogy}\n\n{reaction}"
        return final_script
        
    except Exception as e:
        print(f"Error generating script: {e}")
        return "Error generating script. Please check your OpenAI API key and try again."

def process_transcript(input_file, output_dir):
    # Read the transcript
    with open(input_file, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    # Clean the transcript
    clean_text = clean_transcript(transcript)
    
    # Split into stories
    stories = split_into_stories(clean_text)
    
    # Process each story
    for i, story in enumerate(stories, 1):
        # Generate Peter Griffin script using OpenAI
        peter_script = generate_peter_script(story)
        
        # Create output filename
        timestamp = datetime.now().strftime("%Y%m%d")
        output_file = os.path.join(output_dir, f"segment_{timestamp}_{i}.txt")
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(peter_script)
        
        print(f"Created segment {i}: {output_file}")

if __name__ == "__main__":
    input_file = "transcripts/stormcast_2025-05-17_transcript.txt"
    output_dir = "segments"
    process_transcript(input_file, output_dir) 