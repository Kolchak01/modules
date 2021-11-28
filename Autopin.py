import asyncio

from .. import loader, utils


class AutoPinMod(loader.Module):
    """Автопин регистрации"""
    strings = {'name': 'AutoPin'}

    async def watcher(self, message):
        """почему это называется watcher???"""
        baku_id = [1520369962, 1050428643]
        if message.sender_id in baku_id:
            if ('ветров' in message.raw_text.split()) or ('Недостаточно' in message.raw_text.split()):
                x = await message.client.get_messages(message.chat_id, limit=30, from_user=baku_id)
                for msg in x:
                    if 'набор' in msg.raw_text.split():
                        await msg.delete()