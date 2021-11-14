from asyncio import gather, sleep

from pyrogram import filters
from pyrogram.types import Message

from wbb import (BOT_ID, SUDOERS, USERBOT_ID, USERBOT_PREFIX, USERBOT_USERNAME,
                 app, app2, arq, eor)
from wbb.core.decorators.errors import capture_err
from wbb.utils.filter_groups import chatbot_group
___
