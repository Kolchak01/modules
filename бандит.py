from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)


@loader.tds
class AutoInfoMod(loader.Module):
    """1"""
    strings = {"name": "банд"}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()


    async def watcher(self, message):
        if ('Рулетка' in message.raw_text.split()) or ('Бандит' in message.raw_text.split()):
            reply = await message.get_reply_message()
            fromid = message.from_id
            await message.respond(f".mute {message.sender_id} 5m в бандита и рулетку играй в нашем <a href='https://t.me/casinopermafia\'>казино</a>")
