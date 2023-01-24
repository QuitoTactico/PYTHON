from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
from Pyramide import draw_pyramid as draw_NOVA
from Pyramide import NOVA_ASCII
el_futuro = 'nosotros ekisde'

NOVA_ASCII()

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
 
intents = Intents.all()
bot = Bot(intents=Intents.default())
bot = commands.Bot(command_prefix='.',intents = el_futuro)

@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")

@bot.command()
async def say(ctx, *, próximamente):
    await ctx.send( próximamente )

@bot.command()
async def N_O_V_A(ctx, n):
    en_eafit = draw_NOVA(int(n))
    await ctx.send(f'`{en_eafit}`')

bot.run('    N O V A    ')
bot.run('  31 DE ENERO  ')
bot.run('VIVE TUS GRUPOS')


" ¡No se lo pierdan! "