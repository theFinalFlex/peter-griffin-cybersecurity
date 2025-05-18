import os
import json
import logging
from datetime import datetime
import requests
from PIL import Image
import moviepy.editor as mp
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('video_generation.log'),
        logging.StreamHandler()
    ]
)

class VideoGenerator:
    def __init__(self):
        self.assets_dir = "assets"
        self.output_dir = "videos"
        self.gameplay_dir = os.path.join(self.assets_dir, "gameplay")
        self.images_dir = os.path.join(self.assets_dir, "images")
        
        # Create necessary directories
        for dir_path in [self.assets_dir, self.output_dir, self.gameplay_dir, self.images_dir]:
            os.makedirs(dir_path, exist_ok=True)
    
    def download_gameplay(self):
        """Download random gameplay footage for background"""
        # This would be replaced with actual gameplay download logic
        # For now, we'll assume we have gameplay footage in the assets directory
        gameplay_files = list(Path(self.gameplay_dir).glob("*.mp4"))
        if not gameplay_files:
            raise Exception("No gameplay footage found. Please add some to the assets/gameplay directory.")
        return str(gameplay_files[0])
    
    def get_tech_images(self, text):
        """Get relevant technology images based on text content"""
        # Map of technology keywords to image filenames
        tech_images = {
            "chrome": "chrome_logo.png",
            "google": "google_logo.png",
            "sonicwall": "sonicwall_logo.png",
            "vmware": "vmware_logo.png",
            "webmail": "webmail_icon.png",
            "security": "security_icon.png",
            "hack": "hacker_icon.png",
            "vulnerability": "vulnerability_icon.png",
        }
        
        images = []
        text_lower = text.lower()
        for keyword, image in tech_images.items():
            if keyword in text_lower:
                image_path = os.path.join(self.images_dir, image)
                if os.path.exists(image_path):
                    images.append(image_path)
        
        return images
    
    def generate_brainrot_video(self, segment_file, output_file):
        """Generate a brainrot-style video from a segment"""
        try:
            # Read the segment content
            with open(segment_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get gameplay footage
            gameplay_path = self.download_gameplay()
            
            # Get relevant tech images
            tech_images = self.get_tech_images(content)
            
            # Create brainrot.js configuration
            config = {
                "input": {
                    "text": content,
                    "gameplay": gameplay_path,
                    "images": tech_images
                },
                "output": output_file,
                "settings": {
                    "duration": 60,  # 60 seconds per segment
                    "style": "peter_griffin",  # or "rick_and_morty"
                    "image_duration": 3,  # seconds per image
                    "image_transition": 0.5  # seconds for transition
                }
            }
            
            # Save config for brainrot.js
            config_file = "brainrot_config.json"
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Call brainrot.js (this would be replaced with actual brainrot.js integration)
            # For now, we'll just create a placeholder video
            self._create_placeholder_video(output_file, content, gameplay_path, tech_images)
            
            logging.info(f"Successfully generated video: {output_file}")
            return output_file
            
        except Exception as e:
            logging.error(f"Error generating video: {e}")
            raise
    
    def _create_placeholder_video(self, output_file, text, gameplay_path, images):
        """Create a placeholder video until brainrot.js integration is complete"""
        # Load gameplay video
        gameplay = mp.VideoFileClip(gameplay_path)
        
        # Create text clip
        txt_clip = mp.TextClip(text, fontsize=24, color='white')
        txt_clip = txt_clip.set_duration(60)
        
        # Create image clips
        image_clips = []
        for image_path in images:
            img = Image.open(image_path)
            img_clip = mp.ImageClip(image_path).set_duration(3)
            image_clips.append(img_clip)
        
        # Combine all clips
        final_clip = mp.CompositeVideoClip([gameplay, txt_clip] + image_clips)
        
        # Write the result
        final_clip.write_videofile(output_file, fps=24)

def process_segments():
    """Process all segments and generate videos"""
    generator = VideoGenerator()
    
    # Get all segment files
    segment_files = list(Path("segments").glob("*.txt"))
    
    for segment_file in segment_files:
        # Create output filename
        output_file = os.path.join("videos", f"{segment_file.stem}.mp4")
        
        # Generate video
        generator.generate_brainrot_video(str(segment_file), output_file)

if __name__ == "__main__":
    process_segments() 