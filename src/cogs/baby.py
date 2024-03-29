import config
import discord
import utils
from discord.ext import commands


def setup(bot: commands.Bot):
    bot.add_cog(Baby(bot))


class Baby(commands.Cog, name="Baby Shark"):
    def __init__(self, bot):
        self.bot = bot
        self.doos = 6
        self.family = [
            'Baby',
            'Mommy',
            'Daddy',
            'Grandma',
            'Grandpa',
        ]
        self.repetitions = 3
    
    @commands.command(brief="Sings the baby shark song")
    async def baby(self, ctx: commands.Context, *args):
        name = ' '.join(args) or 'Violet'
        sections = []
        for role in self.family:
            section = []
            line = f'{role} {name}, ' + ', '.join(['doo'] * self.doos)
            for _ in range(self.repetitions):
                section.append(line)

            section.append(f'{role} {name}!')
            sections.append('\n'.join(section))

        await ctx.send('\n\n'.join(sections))

