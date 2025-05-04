# Jarvis AI Voice Assistant

Jarvis AI is an intelligent voice assistant built with Python that listens to your voice commands and performs a variety of tasks to make your life easier. Whether you want to open popular websites, get the current time or date, or have an interactive chat with an AI, Jarvis AI is here to assist you seamlessly.

## Features

- **Voice Recognition:** Uses your microphone to understand spoken commands.
- **Website Launcher:** Open popular websites like YouTube, Google, Wikipedia, and Instagram with simple voice commands.
- **Time and Date:** Get the current time, date, or day spoken back to you.
- **AI Chat:** Engage in interactive conversations powered by OpenAI's GPT-3.5-turbo model.
- **Response Saving:** When you start your prompt with "Using AI", the AI's response is saved as a `.txt` file in the `OpenAI` directory.
- **Speech Output:** Uses Windows SAPI for natural-sounding voice responses.
- **Easy to Use:** Simple setup and intuitive voice commands.

## Requirements

The project depends on the following Python packages, all listed in the `requirements.txt` file:

- `speechrecognition`
- `openai`
- `pywin32`
- `pyaudio`

## Getting Started

### Installation

1. **Clone the repository** or download the source code.

2. **Create and activate a virtual environment** (recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

### Configuration

- **OpenAI API Key:**  
  To enable the AI chat feature, you need a valid OpenAI API key.  
  Replace the placeholder API key in `main.py` with your own key:

```python
client = OpenAI(
    api_key="your_openai_api_key_here",
    base_url="https://api.chatanywhere.tech/v1"
)
```

### Usage

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
- "What is the date?"
- "What day is it?"
- Use phrases starting with **"Using AI"** to interact with the AI chat feature and save the response to a text file (e.g., "Using AI, write a poem about nature")
- Speak normally without "Using AI" to chat with Jarvis via voice commands and receive spoken responses
- "Quit" to exit the program

### Response Saving

When you use the **"Using AI"** prefix in your prompt, Jarvis will save the AI's response as a `.txt` file inside the `OpenAI` directory. The filename is derived from your prompt text following "Using AI".

### Example Interaction

```
User: Open YouTube
Jarvis: Opening YouTube

User: What is the time?
Jarvis: The time is 3:45 PM

User: Using AI, tell me a joke
Jarvis: (Saves the joke response to OpenAI/tell me a joke.txt)

User: Hello Jarvis
Jarvis: Hello! How can I assist you today?
```

## Notes

- This project is designed to run on Windows due to its use of Windows SAPI for speech output.
- Ensure your microphone is properly configured and accessible.
- An active internet connection is required for Google's speech recognition and OpenAI API.
- The AI chat feature depends on the OpenAI API and may incur usage costs depending on your plan.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Jarvis AI.

## Support

If you encounter any issues or have questions, please open an issue on the repository or contact the maintainer.

## License

This project is provided as-is without any warranty.
