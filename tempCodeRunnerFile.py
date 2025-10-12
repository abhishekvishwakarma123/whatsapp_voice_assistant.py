
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speaking speed

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Speech service unavailable."
        except sr.WaitTimeoutError:
            return "You didn't say anything."

# Open WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
speak("Please scan the QR code on WhatsApp Web and press enter to continue.")
input("Press Enter after scanning the QR code...")

def send_message(contact, message):
    """Send message to a contact"""
    try:
        # Find contact and click
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        search_box.click()
        search_box.send_keys(contact)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        
        # Send message
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@title='Type a message']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        # Highlight chat in red
        script = """
        let chat = document.querySelector('div.copyable-text');
        if (chat) { chat.style.backgroundColor = 'lightcoral'; }
        """
        driver.execute_script(script)

        speak(f"Message sent to {contact}")

    except Exception as e:
        speak("I couldn't find the contact.")
        print(e)

# Main function
def whatsapp_voice_assistant():
    speak("Who do you want to message?")
    contact_name = listen()

    speak(f"What message do you want to send to {contact_name}?")
    message = listen()

    send_message(contact_name, message)

    speak("Would you like to send another message?")
    response = listen()
    if "yes" in response:
        whatsapp_voice_assistant()
    else:
        speak("Okay, closing WhatsApp. Have a great day!")
        driver.quit()

# Run the assistant
whatsapp_voice_assistant()

import time

def send_message_by_number(phone_number, message):
    """Send a message to a phone number directly via WhatsApp Web."""
    try:
        # Load WhatsApp Web chat for given number
        url = f"https://web.whatsapp.com/send?phone={phone_number}"
        driver.get(url)
        time.sleep(10)  # wait for chat to load

        # Locate message input box and send
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@title='Type a message']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        speak(f"Message sent to {phone_number}")

    except Exception as e:
        speak("I couldn't send the message.")
        print(e)

def whatsapp_voice_assistant():
    speak("Please tell the phone number with country code. For example, nine one nine eight...")

    phone_number = listen().replace(" ", "").replace("-", "")
    # Optional: Convert words to digits if necessary

    speak(f"What message do you want to send to {phone_number}?")
    message = listen()

    send_message_by_number(phone_number, message)

    speak("Would you like to send another message?")
    response = listen()
    if "yes" in response:
        whatsapp_voice_assistant()
    else:
        speak("Okay, closing WhatsApp. Have a great day!")
        driver.quit()

