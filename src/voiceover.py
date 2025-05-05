import requests

class VoiceOverGenerator:
    def __init__(self, api_key, voice_id="Josh"):
        self.api_key = api_key
        self.voice_id = voice_id

    def generate_voiceover(self, text, output_path):
        print(f"Generating voiceover for: {text}")
        with open(output_path, "w") as f:
            f.write(f"Voiceover: {text}")
