# Telegram Chatbot with Gemini Integration

This project demonstrates a Telegram chatbot integrated with Gemini's API, allowing for interactive conversations.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.11**: Make sure Python 3.11 is installed on your system.
- **Telegram Account**: A Telegram account and a smartphone to interact with the bot.
- **Gemini Account**: An Gemini account and an API key.

## Setup and Installation

Follow these steps to set up and run the bot:

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/Telegram-chatbot.git
cd Telegram-chatbot
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

**For macOS/Linux:**

```bash
python3.11 -m venv botEnv
source botEnv/bin/activate
```

**For Windows:**

```bash
python3.11 -m venv botEnv
.\botEnv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Alternatively, you can run the `init_setup.sh` script to perform steps 2 and 3 automatically:

```bash
bash init_setup.sh
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your Gemini API key and Telegram Bot Token. Replace the placeholder values with your actual keys.

```ini
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TELEGRAM_BOT_TOKEN=xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Telegram Bot Setup (BotFather)

To get your `TELEGRAM_BOT_TOKEN`:

1.  Open Telegram and search for `@BotFather`.
2.  Start a chat with BotFather and send the command `/newbot`.
3.  Follow the prompts:
    - Enter a name for your bot (e.g., `telebot2025`).
    - Enter a username for your bot (e.g., `telebot2025_bot`). This must end with `_bot`.
4.  BotFather will provide you with an HTTP API Token. Copy this token and paste it into your `.env` file as `TELEGRAM_BOT_TOKEN`.

### 6. Run the Bot

Once everything is set up, start the bot:

```bash
python3 main.py
```

### 7. Interact with Your Bot

1.  Open Telegram and search for your bot's username (e.g., `telebot2025_bot`).
2.  Start a conversation with your bot and enjoy!

## AIogram Documentation

For more detailed information on the AIogram framework, refer to its official documentation:

[https://docs.aiogram.dev/en/latest/](https://docs.aiogram.dev/en/latest/)
