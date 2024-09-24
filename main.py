import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from quote_generator import generate_quote
from error_handler import handle_error
from tts_service import generate_audio

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_system_prompt():
    try:
        with open("system_prompt.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.error("system_prompt.txt not found")
        return None

def create_quotes_folder():
    quotes_folder = "Quotes"
    if not os.path.exists(quotes_folder):
        os.makedirs(quotes_folder)
    return quotes_folder

def generate_foldername():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return timestamp

def create_quote_folder(quotes_folder, foldername):
    quote_folder = os.path.join(quotes_folder, foldername)
    os.makedirs(quote_folder)
    return quote_folder

def save_quote_text(quote_folder, quote):
    file_path = os.path.join(quote_folder, "quote.txt")
    with open(file_path, "w") as file:
        file.write(quote)
    return file_path

def text_to_speech(text, quote_folder):
    # Save the audio file
    audio_filename = "quote_audio.mp3"
    audio_path = os.path.join(quote_folder, audio_filename)
    generate_audio(text, audio_path)
    return audio_path

def main():
    # Load environment variables
    load_dotenv()
    
    # Load system prompt
    system_prompt = load_system_prompt()
    if not system_prompt:
        return

    # Create Quotes folder
    quotes_folder = create_quotes_folder()

    try:
        # Generate quote
        quote = generate_quote(system_prompt)
        logging.info(f"Generated quote: {quote}")

        # Generate foldername
        foldername = generate_foldername()

        # Create folder for this quote
        quote_folder = create_quote_folder(quotes_folder, foldername)

        # Save quote text
        text_file_path = save_quote_text(quote_folder, quote)
        logging.info(f"Saved quote text to: {text_file_path}")

        # Generate audio
        logging.debug("Attempting to generate audio...")
        audio_path = text_to_speech(quote, quote_folder)
        logging.info((f"Damn generate audio file:{audio_path}"))

        print(f"Quote: {quote}")
        print(f"Text file: {text_file_path}")
        print(f"Audio file:{audio_path}")

    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()