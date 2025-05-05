# Text-to-Video Manga Generator

This project generates a manga-inspired video by combining AI-generated images, captions, and voiceovers. The pipeline parses a script, creates manga panels with captions, generates voiceovers for dialogue, and assembles everything into a video.

## Features
- **AI-Generated Images**: Create manga panels from textual descriptions.
- **Caption Overlay**: Add dialogue captions to manga panels.
- **Voiceovers**: Realistic AI voiceovers using ElevenLabs API.
- **Video Assembly**: Combine panels and voiceovers into a final video.

## Repository Structure
```plaintext
text-to-video-manga/
├── data/
│   ├── script.txt            # Input script containing scene descriptions and dialogues
├── src/
│   ├── parser.py             # Parses the script into scenes
│   ├── image_generator.py    # Generates manga panels from descriptions
│   ├── caption_overlay.py    # Adds captions to images
│   ├── voiceover.py          # Generates voiceovers from dialogue
│   ├── video_assembler.py    # Combines images and audio into a video
│   ├── main.py               # Main pipeline for the project
├── output/                   # Directory for the final output video
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-to-video-manga.git
   cd text-to-video-manga
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following are installed:
   - Stable Diffusion or any image generation API.
   - ElevenLabs API key for voiceover generation.
   - FFMPEG for video assembly.

## Usage
1. Add your script to `data/script.txt` following the format:
   ```
   # Scene 1
   Description: A heroic manga character stands on a cliff at sunset.
   Dialogue: "I will save the world, no matter the cost."

   # Scene 2
   Description: A villainous figure laughs in the shadows.
   Dialogue: "You think you can stop me? Foolish hero."
   ```

2. Run the main pipeline:
   ```bash
   python src/main.py
   ```

3. Find the final video in the `output/` directory.

## Contributing
Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License.
