from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)


@loader.tds
class AutovahtaMod(loader.Module):
    """1"""
    strings = {"name": "Autolog"}

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()


    async def watcher(self, message):
        if  ('Да' in message.raw_text.split()) or ('да' in message.raw_text.split()):
            reply = await message.get_reply_message()
            fromid = message.from_id
            if reply:
                await message.respond(f"!поезда")
                return
            await message.respond(f"!поезда")
