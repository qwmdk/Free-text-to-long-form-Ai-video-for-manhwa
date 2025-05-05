import os
from parser import parse_script
from image_generator import MangaPanelGenerator
from caption_overlay import CaptionOverlay
from voiceover import VoiceOverGenerator
from video_assembler import VideoAssembler

def main():
    script_path = "../data/script.txt"
    output_video_path = "../output/final_video.mp4"

    panel_generator = MangaPanelGenerator()
    caption_overlay = CaptionOverlay()
    voiceover_generator = VoiceOverGenerator("your-elevenlabs-api-key")
    video_assembler = VideoAssembler()

    scenes = parse_script(script_path)

    images = []
    audio_files = []

    for i, scene in enumerate(scenes):
        image_path = f"../data/generated_images/scene_{i + 1}.png"
        audio_path = f"../data/generated_audio/scene_{i + 1}.mp3"

        panel_generator.generate_panel(scene['description'], image_path)
        caption_overlay.add_caption(image_path, scene['dialogue'], image_path)
        voiceover_generator.generate_voiceover(scene['dialogue'], audio_path)

        images.append(image_path)
        audio_files.append(audio_path)

    video_assembler.assemble_video(images, audio_files, output_video_path)

if __name__ == "__main__":
    main()
