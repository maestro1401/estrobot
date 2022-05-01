import disnake
from disnake.ext import commands

class tech(commands.Cog): #Имя класса (обычно с большой буквы по PEP8) можно называть как угодно.
    def __init__(self, Bot):
        self.bot = Bot

    @commands.command() # Так обозначаются команды.
    async def ping(self, ctx): # Обязательно в каждой команду и событии впереди писать self!
        await ctx.send("PONG!")

    @commands.command() # Так обозначаются команды.
    async def test(self, ctx): # Обязательно в каждой команду и событии впереди писать self!
            await ctx.send("Ну тест и тест ну за то работает")

# Везде перед командами нажен 1 таб, т. к. это класс.

    @commands.Cog.listener() # Так обозначаются события.
    async def on_ready(self):
        print("Коги загружены!")

    @commands.command(
        aliases=['е', 'e', 'евал']
    )
    async def eval(
        self,
        ctx,
        *,
        code = None
    ):
        if ctx.author.id in [786621039789998121]:
            if code is None:
                e = disnake.Embed(
                    title=f':x: Вы не ввели параметр:',
                    description='> Код',
                )
                await ctx.send(embed=e)
            else:
                language_specifiers = ["python", "py"]
                loops = 0
                while code.startswith("`"):
                    code = "".join(list(code)[1:])
                    loops += 1
                    if loops == 3:
                        loops = 0
                        break
                for language_specifier in language_specifiers:
                    if code.startswith(language_specifier):
                        code = code.lstrip(language_specifier)
                while code.endswith("`"):
                    code = "".join(list(code)[0:-1])
                    loops += 1
                    if loops == 3:
                        break
                code = "\n".join(f"    {i}" for i in code.splitlines())
                code = f"async def eval_expr():\n{code}"
                env = {
                    "b": self.bot,
                    "self.bot": self.bot,
                    "Bot": self.bot,
                    "bot": self.bot,
                    "client": self.bot,
                    "Client": self.bot,
                    "ctx": ctx
                }
                env.update(globals())
                try:
                    exec(code, env)
                    eval_expr = env["eval_expr"]
                    result = await eval_expr()
                    if result:
                        await ctx.reply(f'\n{result}')
                except Exception as e:
                    await ctx.send(f":x: Класс: {e.__class__}\nОшибка: {e}")

def setup(Bot): 
    Bot.add_cog(tech(Bot)) #Вот здесь имя класса!