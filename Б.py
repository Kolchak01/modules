from .. import loader		
from asyncio import sleep

class IrisBotMod(loader.Module):
	"""Я рекомендую создать вам чат ,где вы будете использовать данный модуль, чтобы вас не беспокоили лишнии уведомления и тд. Так же можно это делать в лс Iris-а."""
	strings = {"name": "рднофарм"}
	
	def __init__(self):
		self.farm = True
		self.virys = True
		
	async def бcmd(self, message):
		"""Включает команду "бфарм". Чтобы остановить, используйте "бфарм стоп"."""
		while self.farm:
			await message.reply("б")
			await sleep(43500)
		
	async def watcher(self, message):
		me = (await message.client.get_me())
		if message.sender_id == me.id:
			if message.text.lower() == "бфарм стоп":
				self.farm = False
				await message.reply("<b>Бфарм остановлен.</b>")
			
				
			
