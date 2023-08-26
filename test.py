from twitchio.ext import commands

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(
            token='oe5zzmr7rwvbolgqcd9fgnkiz2jfjv',
            prefix='!',
            initial_channels=['jaggerv'])
    
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hola(self, ctx: commands.Context):
        await ctx.send(f'Hola {ctx.author.name}!')

bot = Bot()
bot.run()