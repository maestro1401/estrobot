from typing import Text
import disnake
from disnake import mentions
from disnake.ext import commands
import os


bot = commands.Bot( command_prefix = '*', Intents= disnake.Intents.all())

@bot.event

async def on_ready():
    print('Estro Bot Готов к работе')

    await bot.change_presence( status = disnake.Status.online, activity = disnake.Game( 'Stream Server♥' ) )
	
@bot.event

async def on_member_join(member):
    channel = disnake.utils.get(member.guild.channels, id = 959895222073057301)
    
    role = disnake.utils.get(member.guild.roles, id = 959870570609143901) 

    await member.add_roles( role )
    await channel.send( embed = disnake.Embed( description = f"Добро пожаловать { member.mention } устраивайся по удобней и добрейшого тебе вечерочка!", color = 0x0c0c0c) )

@bot.command()
@commands.has_permissions( administrator = True )

async def text(ctx, *, text ):
        await ctx.send(embed = disnake.Embed(description = text, color = 0x4f0))

@bot.command()
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount)
	await ctx.send( embed = disnake.Embed(description = f"Чат успешно очищен✅") )

@bot.command()
@commands.has_permissions( administrator = True )

async def kick( ctx, arg, member: disnake.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason )
	await ctx.send( embed = disnake.Embed(description = f'{ member.mention } был выгнан по причнине {reason}' ) )

@bot.command()
@commands.has_permissions( administrator = True )

async def ban( ctx, member: disnake.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason )
	await ctx.send(embed = disnake.Embed(description = f'Игрок {member.mention} был забанен по причине {reason} '))

@bot.command()

async def command( ctx ):
	await ctx.send( embed = disnake.Embed(description = "**Команды:\n-------------------\n ** *clear - Очистка чата (Для Администраторов)**\n** *ban - Выгоняет участника навсегда (Для Администраторов)**\n** *kick - Выгоняет участника**\n** *mute - Глушит игрока на определённый срок**\n** *text - Ваш текст только в Embed**\n** *profile - Ваш профиль.**\n** *report - Жалоба на какого либо человека.**\n** *idea - Написать что сделать на сервере или что доработать боту Estro Bot.**", color = 0xfffff) )

@bot.command()

async def profile(ctx, member: disnake.Member, reason = None):
	emb = disnake.Embed(title='Профиль', colour= 0x2f3136)
	emb.set_thumbnail(url = member.avatar)
	emb.add_field(f'Ник:', value=member.mention, inline=False)
	emb.add_field('Уровень:', value=1, inline=False)
	emb.add_field('EXP:', value=0, inline=False)
	emb.add_field("Время:", value="В разработке", inline=False)
	await ctx.send(embed = emb)

@bot.command()

async def report(ctx, member: disnake.Member, *, reason: str = None):
    if reason is None:
      reason = "Причина не указана"
    guild = ctx.guild
    channel = guild.get_channel(960194522036449311)
    await channel.send(embed = disnake.Embed(description = f"**🚨Жалоба на: {member}🚨**\n🚧-----------------------------🚧\n**🚥по причине: {reason}🚥**", color = 0x553bff))

@bot.command()

async def idea(ctx, member: disnake.Member, *, reason: str = None):
    if reason is None:
      reason = "Не указана идея"
    guild = ctx.guild
    channel = guild.get_channel(960226231176007710)
    await channel.send(embed = disnake.Embed(description = f"**🔑Предложена идея кем: {member}🔑**\n**🔑-------------------------------------🔑**\n🔑**Идея: {reason}🔑**", color = 0xffde3b    ))

@bot.command()

async def timeout(ctx, member: disnake.Member, reason = None):
    await ctx.channel.purge( limit = 1 )

    await member.timeout(duration=3000)
    
    await ctx.send(embed = disnake.Embed(description = f"**Пользователь {member.mention} получил тайм-аут по причине: {reason}**"))

@bot.command()

async def untime(ctx, member: disnake.Member, reason = None):
    await ctx.channel.purge( limit = 1 )

    await member.timeout(duration=None)
    
    await ctx.send(embed = disnake.Embed(description = f"**У Пользователя {member.mention} был снят тайм-аут по причине: {reason}**"))

@bot.command()

async def invite(ctx):
    await ctx.channel.purge( limit = 1 )

    await ctx.send(embed = disnake.Embed(description = f"**INVITE \n BOT:||https://discord.com/api/oauth2/authorize?client_id=959885468785324072&permissions=8&scope=bot|| \n SERVER: ||dsc.gg/livephantom или https://discord.gg/DPF4CZB8gE|| \n**"))  

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       bot.load_extension(f'cogs.{filename[:-3]}')
	   
bot.run(process.env.BOT_TOKEN)