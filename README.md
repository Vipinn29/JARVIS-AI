# Jarvis AI Voice Assistant

This is a simple voice assistant project named "Jarvis AI" implemented in Python. It listens to voice commands and can open popular websites like YouTube, Google, Wikipedia, and Instagram. It can also tell the current time and respond to basic commands.

## Features

- Voice recognition using the microphone
- Opens websites based on voice commands (YouTube, Google, Wikipedia, Instagram)
- Tells the current time when asked
- Speaks responses using Windows SAPI voice

## Requirements

The project requires the following Python packages, listed in `requirements.txt`:

- speechrecognition
- openai
- wikipedia
- pywin32
- pyaudio

## Installation

1. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

Speak commands such as:

- "Open YouTube"
- "Open Google"
- "Open Wikipedia"
- "Open Instagram"
- "What is the time?"
- "Quit" to exit the program

## Notes

- This project uses the Windows SAPI for speech output, so it is designed to run on Windows.
- Make sure your microphone is set up and working properly.
- The script uses Google's speech recognition service, so an internet connection is required.

## License

This project is provided as-is without any warranty.
