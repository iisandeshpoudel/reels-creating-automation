import os
import logging
from gtts import gTTS
from error_handler import handle_error

def generate_audio(text, quote_folder):
    try:
        logging.debug("Initializing Text-to-Speech...")
        tts = gTTS(text=text, lang='en', slow=False)

        file_path = os.path.join(quote_folder, "quote.mp3")
        logging.debug(f"Saving audio to {file_path}...")
        
        tts.save(file_path)

        logging.info(f"Audio file saved successfully: {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"Error in generate_audio: {str(e)}")
        handle_error(e)
        return None