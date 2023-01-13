from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
from Pyramide import draw_pyramid

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
 
intents = Intents.all()
bot = Bot(intents=Intents.default())
bot = commands.Bot(command_prefix='.',intents=intents)
 
@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
 
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")



#--------------------------------------------------------------------------------------------------



@bot.command()
async def say(ctx, *, mensaje):
    await ctx.send(mensaje)

@bot.command()
async def feo(ctx, *, mensaje):
    if mensaje.lower() == 'esteban':
        await ctx.send(f'Falsísimo, Esteban es lindo')
    else:
        await ctx.send(f'{mensaje} es fea srjahbefgv')

@bot.command()
async def piramide(ctx, n):
    resultado = draw_pyramid(int(n))
    await ctx.send(f'`{resultado}`')
        
 
bot.run("MTA2MjU4MjM1OTAyMDUzOTk1Ng.Gop3uZ.ofz1WhIaN-Aj1SLNIFm2iAUJRfHthzEO5RQW0s")

'''
INVITACIÓN
https://discord.com/api/oauth2/authorize?client_id=1062582359020539956&permissions=137654361088&scope=bot%20applications.commands

CLIENT ID
1062582359020539956



'''