import json
import asyncio
import logging

from datetime import datetime
from dataclasses import dataclass
from asyncio import get_running_loop

from aiogram.utils import markdown
from aiogram import Bot, Dispatcher
from aiogram.utils.exceptions import RetryAfter

from config import Config, load_config
from parser import ChatMessage, parse_chat


@dataclass
class MessageLastDate:
    """
    A class that records the last date of a message and saves it in a JSON file.

    Attributes:
        FILE_NAME (str): The name of the JSON file to save the last message date.
        DATE_FORMAT (str): The format of the date in the message.
    """
    FILE_NAME = "data.json"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def _load(cls) -> dict:
        """
        Load the last message date from the JSON file.

        Returns:
            dict: A dictionary containing the last message date.
        """
        with open(cls.FILE_NAME, "r") as f:
            return json.loads(f.read())

    @classmethod
    def _save(cls, last_date) -> None:
        """
        Save the last message date to the JSON file.

        Args:
            last_date: The last message date to be saved.
        """
        with open(cls.FILE_NAME, "w") as f:
            f.write(json.dumps({"last_date": last_date}))

    @classmethod
    def get(cls) -> datetime:
        """
        Get the last message date.

        Returns:
            datetime: The last message date.
        """
        string = cls._load()["last_date"]
        return datetime.strptime(string, cls.DATE_FORMAT)

    @classmethod
    def update(cls, last_date: str) -> None:
        """
        Update the last message date.

        Args:
            last_date: The last message date to be updated.
        """
        cls._save(last_date=last_date)


async def send_messages(messages: list[ChatMessage]) -> None:
    """
    Send new messages to the group chat.

    Args:
        messages: A list of new messages to be sent.
    """
    loop = get_running_loop()

    bot: Bot = loop.__getattribute__("bot")
    config: Config = loop.__getattribute__("config")

    for message in messages:
        try:
            text = (
                f"{message.user_country} "
                f"{markdown.hlink(message.user_name, message.user_link)}\n\n"
                f"💬 {markdown.hcode(message.text)}\n\n"
                f"{markdown.hspoiler('🗺 ', message.map)}\n"
                f"{markdown.hspoiler('📅 ', message.date)}"
            )
            await bot.send_message(
                text=text,
                chat_id=config.GROUP_ID,
                message_thread_id=config.LIVE_CHAT_ID,
                disable_web_page_preview=True,
            )

        except RetryAfter as e:
            logging.error(e)

            seconds = int(e.args[0].split()[-2])
            await asyncio.sleep(seconds)

        await asyncio.sleep(1)


async def send_new_message() -> None:
    """
    Check for new messages and send them to the group chat if there are any.

    Returns:
        bool: True if new messages were sent, False otherwise.
    """
    base_url = "https://toma92.myarena.site"
    messages = await parse_chat(base_url)
    if not messages:
        return

    last_date = MessageLastDate.get()

    messages = [
        message for message in messages if
        datetime.strptime(message.date, MessageLastDate.DATE_FORMAT) > last_date
    ]

    if messages:
        last_date = messages[0].date
        await send_messages(messages[::-1])
        MessageLastDate.update(last_date)


async def schedule_task() -> None:
    """
    Schedule a task to check for new messages and send them to the group chat.
    """
    while True:
        await send_new_message()
        await asyncio.sleep(3)


async def main():
    logging.basicConfig(level=logging.INFO)
    config: Config = load_config()

    bot = Bot(config.TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot)

    loop = asyncio.get_event_loop()

    loop.__setattr__("bot", bot)
    loop.__setattr__("config", config)

    tasks = [
        asyncio.create_task(schedule_task()),
        asyncio.create_task(dp.start_polling())
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
