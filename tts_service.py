import os
from elevenlabs import ElevenLabs, VoiceSettings
from error_handler import handle_error
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("v_api_key")
print(f"your api key: {api_key}")
client = ElevenLabs(api_key=api_key)

def generate_audio(text, output_file):
    print(f"your api key: {api_key}")
    try:
        audio_generator = client.text_to_speech.convert(
            voice_id="ErXwobaYiN019PkySvjV",  # You can change this to your preferred voice ID
            optimize_streaming_latency="0",
            output_format="mp3_44100_128",
            text=text,
            voice_settings=VoiceSettings(
                stability=0.1,
                similarity_boost=0.3,
                style=0.2,
            ),
        )

        # Save the audio to a file
        with open(output_file, "wb") as file:
            for chunk in audio_generator:
                file.write(chunk)
                
        print(f"Audio written to the file {output_file}")

    except Exception as e:
        print(f"Sandesh yeta error ayo audio ko side ma: {str(e)}")

# EXAMPLE::
if __name__ == "__main__":
    generate_audio("Samir happy birthday", "test.mp3")
