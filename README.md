
Code Description:
01. Imported Libraries:

1.time: For adding delays between operations
2.pyttsx3: Text-to-speech conversion (offline)
3.speech_recognition: Voice input recognition using microphone
4.selenium.webdriver: Browser automation to control WhatsApp Web
5.selenium.webdriver.common.keys: For sending keyboard keys
6.selenium.webdriver.common.by: For locating elements in the DOM

02. Core Functions:
speak(text)

1.Purpose: Converts text to speech using pyttsx3.
2.Parameters:
text (str): The message to be spoken aloud.
3.Behavior:
Uses engine.say() to queue the speech.
engine.runAndWait() blocks until speech is complete.
4.listen()
Purpose: Captures microphone input and converts it to text using Google's speech recognition API.
5.Returns:
Recognized text (str) in lowercase.
Error message if recognition fails.
6.Exceptions Handled:
UnknownValueError: When speech is unclear.
RequestError: If the API is unavailable.
WaitTimeoutError: If no speech is detected within 5 seconds.

send_message(contact, message)
7.Purpose: Automates sending a WhatsApp message to a specified contact.
8.Parameters:
contact (str): Name of the WhatsApp contact.
message (str): Text to send.
9.Workflow:
.Finds the search box using XPath and types the contact name.
.Presses ENTER to open the chat.
.Locates the message input box and sends the text.
.Highlights the chat in red using JavaScript (visual feedback).
10.Error Handling:
.Speaks an error message if the contact is not found.

03. Main Workflow (whatsapp_voice_assistant())
1.Initialization:
.Opens WhatsApp Web in Chrome and waits for QR code scanning.
.Asks the user to press ENTER after scanning.
2.Voice Interaction:
.Asks for the contact name and message via voice.
.Calls send_message() to deliver the message.
.Offers to send another message (recursive loop if "yes").
3.Exit:
.Closes the browser when the user declines further messages.

04. Key Features:
.Hands-Free Operation: Fully controlled by voice commands.
.Visual Feedback: Highlights sent chats in red.
.Error Resilience: Gracefully handles speech recognition failures.
.Recursive Flow: Allows sending multiple messages without restarting.

05. Dependencies:
Install required packages:

pip install pyttsx3 speechrecognition selenium

.ChromeDriver: Must be installed and in PATH for Selenium.

06. Limitations:
.WhatsApp Web Changes: XPaths may break if WhatsApp updates its UI.
.Offline TTS: pyttsx3 uses system voices (quality varies).
.Ambient Noise: Requires a quiet environment for accurate speech recognition.

07. Suggested Improvements:
.Add a keyword (e.g., "exit") to terminate early.
.Implement contact validation before sending.
.Use config.ini for customizable settings (e.g., highlight color).
.Add logging for debugging.
