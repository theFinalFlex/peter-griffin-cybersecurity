# Peter Griffin Cybersecurity News Pipeline

This project automates the creation of humorous cybersecurity news videos using Peter Griffin's voice and style. It processes the SANS Internet Storm Center's Stormcast podcast, segments it, and generates engaging video content.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/peter-griffin-cybersecurity.git
cd peter-griffin-cybersecurity
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
OPENAI_API_KEY=your_api_key_here
```

5. Download required assets:
```bash
python download_assets.py
```

## Usage

1. Download the latest podcast transcript:
```bash
python download_transcript.py
```

2. Process the transcript into segments:
```bash
python process_transcript.py
```

3. Generate videos from segments:
```bash
python generate_video.py
```

## Project Structure

- `assets/`: Contains images and other static assets
- `segments/`: Contains processed transcript segments
- `transcripts/`: Contains downloaded podcast transcripts
- `downloads/`: Temporary storage for downloaded files

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 