from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import google.generativeai as genai
import sys

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


class Reference:
    '''
    A class to store previously response from the Gemini API and the chat history.
    '''

    def __init__(self) -> None:
        self.response = ""
        self.chat_sessions = {} # Stores chat sessions for each user_id


reference = Reference()

model_name = "gemini-2.5-flash"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past(user_id: int):
    """A function to clear the previous conversation and context for a specific user.
    """
    reference.response = ""
    if user_id in reference.chat_sessions:
        del reference.chat_sessions[user_id]


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past(message.from_user.id)
    await message.reply("I've cleared the past conversation and context.")


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am Tele Bot!\nCreated by Anwar. How can I assist you?")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm Telegram bot created by Anwar! Please follow these commands -
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)


@dispatcher.message_handler()
async def gemini_chat(message: types.Message):
    """
    A handler to process the user's input and generate a response using the Gemini API.
    """
    print(f">>> USER: \n\t{message.text}")
    user_id = message.from_user.id
    model = genai.GenerativeModel(model_name)

    if user_id not in reference.chat_sessions:
        reference.chat_sessions[user_id] = model.start_chat(history=[])

    chat = reference.chat_sessions[user_id]
    response = chat.send_message(message.text)
    reference.response = response.text
    print(f">>> Gemini: \n\t{reference.response}")
    # Split the response into chunks if it's too long
    max_message_length = 4096
    response_text = reference.response
    if len(response_text) > max_message_length:
        for i in range(0, len(response_text), max_message_length):
            await bot.send_message(chat_id=message.chat.id, text=response_text[i:i + max_message_length])
    else:
        await bot.send_message(chat_id=message.chat.id, text=response_text)


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
