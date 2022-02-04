from .. import loader, utils
import random

class RandomNumbMod(loader.Module):
	strings = {"name": "RandNumb"}
	
	async def рмcmd(self, message):
		args = utils.get_args_raw(message)
		arg = args.split(" ")
		numb1 = int(arg[0])
		numb2 = int(arg[1])
		await message.reply("<b>Рандомное число: </b>" + str(random.randint(numb1,numb2)))