import csv
import os

from .. import loader, utils


class GetUsersMod(loader.Module):
    """АвтоДжоин для бота Мафии"""
    strings = {'name': 'ParseUsers'}

    async def getcmd(self, message):
        """.get"""
        await message.delete()
        CHATID = message.chat_id
        counter = 0
        users = await message.client.get_participants(CHATID)
        with open(f'users_{str(CHATID).strip("-")}.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for user in users:
                if user.bot or user.deleted:
                    continue
                writer.writerow((user.id, user.first_name, user.username))
                counter += 1
        await message.client.send_file('me', f'users_{str(CHATID).strip("-")}.csv',
                                       caption=f"<b>Всего в таблице: </b><code>{counter}</code> <b>юзеров</b>")
        os.remove(f'users_{str(CHATID).strip("-")}.csv')
