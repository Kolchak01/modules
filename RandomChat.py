from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
import asyncio

def register(cb):
    cb(chatMod())
class chatMod(loader.Module):
    """Модуль может кинуть рандомный чат"""
    strings = {'name': 'RandomChat'}
    async def чатcmd(self, message):
        """.чат чтобы получить ссылку на чат"""
        state = "🔀 Случайная беседа"
        await message.reply("<b>by tio...</b>")
        chat = '@iris_cm_bot'
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=707693258))
                bot_send_message = await message.client.send_message(chat, format(state))
                bot_response = response = await response
            except YouBlockedUserError:
                await message.edit('<b>Убери из ЧС:</b> ' + chat)
                return
            await bot_send_message.delete()
            await message.reply(response.text)
            await bot_response.delete()
