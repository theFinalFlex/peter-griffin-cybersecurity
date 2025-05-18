# Brainrot Pipeline

A modular pipeline that downloads the SANS Stormcast podcast, transcribes it, and converts it into Peter Griffin-style commentary.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the main pipeline:
```bash
python main.py
```

Or run individual components:
```bash
python download_podcast.py
python transcribe_audio.py
python peterify.py
```

## Components

- `download_podcast.py`: Downloads today's SANS Stormcast podcast
- `transcribe_audio.py`: Transcribes the MP3 using OpenAI's Whisper
- `peterify.py`: Converts the transcript into Peter Griffin-style commentary
- `main.py`: Orchestrates the entire pipeline

## Output

The final output will be saved as `peter_commentary.txt` in the project directory. 