# WhatsApp Voice Assistant

This is a Python-based voice assistant that allows you to send WhatsApp messages using voice commands. It uses speech recognition to capture your voice input and Selenium to interact with WhatsApp Web.

## Features

- Voice input for contact name or phone number
- Voice input for message content
- Sends messages via WhatsApp Web
- Highlights sent chats in red for confirmation
- Supports sending to contacts by name or directly by phone number

## Requirements

- Python 3.x
- Chrome browser
- Internet connection
- Microphone for voice input

### Python Libraries

Install the required libraries using pip:

```
pip install pyttsx3 speech_recognition selenium
```

You also need to download the ChromeDriver for Selenium. Make sure it's in your PATH or in the same directory as the script.

## How to Run

1. Run the script:
   ```
   python tempCodeRunnerFile.py
   ```

2. The script will open WhatsApp Web in Chrome.

3. Scan the QR code with your phone's WhatsApp app and press Enter in the terminal.

4. Follow the voice prompts:
   - Say the contact name or phone number (with country code).
   - Say the message you want to send.
   - Confirm if you want to send another message.

## Usage

- The assistant will ask for the recipient (contact name or phone number).
- Then, dictate your message.
- The message will be sent automatically.
- You can choose to send more messages or exit.

## Notes

- Ensure your microphone is working and permissions are granted.
- The script uses Google Speech Recognition, so an internet connection is required for speech-to-text.
- Be cautious with sending messages; the script sends them immediately after voice confirmation.

## Troubleshooting

- If speech recognition fails, check your microphone and internet connection.
- If Selenium can't find elements, ensure WhatsApp Web is loaded properly and try again.
- For ChromeDriver issues, download the correct version for your Chrome browser from https://chromedriver.chromium.org/downloads.

## License

This project is for educational purposes. Use responsibly and in accordance with WhatsApp's terms of service.
