import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio

bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

list_ranks = {
    "dst": 877668744749522977,
    "lol": 877672350076768268,
    "gta 5": 877672293923454987
}

channel_name = "bot_commands"


def get_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = get_token()


@bot.event
async def on_ready():
    print(f"{bot.user} se připojil.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def role(ctx):
    if not str(ctx.channel) == channel_name:
        return

    emb = discord.Embed(title="Role\n", color=discord.Color.blue())
    emb.add_field(name="Seznam rolí:  ", value='DST\n'
                                               'GTA 5'
                  )

    await ctx.send(embed=emb)


@bot.command()
async def help(ctx):
    if not str(ctx.channel) == channel_name:
        return

    emb = discord.Embed(title="Použití příkazů a pomoc\n", color=discord.Color.blue())
    emb.add_field(name="Seznam rolí:", value=
                       "DST \n"
                       "LoL\n"
                       "GTA 5", inline=True)
    emb.add_field(name="Příkazy: ", value='!rank "role"\n'
                                          '!rank_remove "role"'
                  )

    await ctx.send(embed=emb)


@bot.command()
@has_permissions(ban_members=True)
async def help_admin(ctx):
    if not str(ctx.channel) == channel_name:
        return

    emb = discord.Embed(title="Použití příkazů pro administrátory(slouží hlavně pro úpravu bota)",
                        color=discord.Color.blue())

    emb.add_field(name="Příkazy: ", value='!check_server_roles\n'
                                          ''
                  )

    await ctx.send(embed=emb)


@bot.command()
@has_permissions(ban_members=True)
async def check_server_roles(ctx):
    ranks = ctx.guild.roles
    list_ranks_id = [i.id for i in ranks]
    list_ranks_name = [i.name.lower() for i in ranks]
    zip_lists = zip(list_ranks_name, list_ranks_id)
    ranks = dict(zip_lists)
    await ctx.message.author.send(ranks)


@bot.command()
async def rank(ctx, *, name=""):
    global list_ranks, channel_name
    rank_id = None
    name = name.lower()
    help_text = (f"Pro odstranění role použij příkaz: !remove_rank 'rank'\n"
                 f"Na výběr je z těchto rolí: {', '.join([i.upper() for i in list_ranks])}")
    list_users_ranks = [i.id for i in ctx.author.roles]
    rank_object = None
    # Deklarování proměnných

    # Pokud nepíše do specifického kanálu
    if not str(ctx.channel) == channel_name:
        return

    # Pokud je jméno prázdné, pošleme nápovědu
    if name == "":
        await ctx.send(help_text)

    # Pokud je jméno ranku v listu ranků, pokračujeme dál a jdeme najít jeho id
    if name in list_ranks:
        pass
    else:
        return

    # Hledání ranku v seznamu ranků
    for rank_name in list_ranks:
        if name == str(rank_name):
            rank_id = list_ranks[name]
            rank_object = ctx.guild.get_role(rank_id)

    # Pokud uživatel má roli, tak mu ji nepřidáme, protože ji nechceme přidat znovu
    if rank_id in list_users_ranks:
        await ctx.send(f"{ctx.author.mention} Danou roli už máš nastavenou.")
        return
    else:
        pass

    # Přidávání ranku
    await ctx.author.add_roles(rank_object)
    await ctx.send(f"{ctx.author.mention} Role {name.upper()} byla přidána.")


@rank.error
async def rank_error(ctx, error):
    await ctx.send(f"Nastala chyba s: {error}")


@bot.command()
async def rank_remove(ctx, *, name=""):
    global list_ranks, channel_name
    rank_id = None
    name = name.lower()
    help_text = (f"Pro odstranění role použij příkaz: !rank_remove 'rank'\n"
                 f"Na výběr je z těchto rolí: {', '.join([i.upper() for i in list_ranks])}")
    list_users_ranks = [i.id for i in ctx.author.roles]
    rank_object = None
    # Deklarování proměnných

    # Pokud nepíše do specifického kanálu
    if not str(ctx.channel) == channel_name:
        return

    # Pokud je jméno ranku prázdné, pošleme nápovědu
    if name == "":
        await ctx.send(help_text)

    # Pokud je jméno ranku v listu ranků, pokračujeme dál a jdeme najít jeho id
    if name in list_ranks:
        pass
    else:
        return

    # Hledání ranku v seznamu ranků
    for rank_name in list_ranks:
        if name == str(rank_name):
            rank_id = list_ranks[name]
            rank_object = ctx.guild.get_role(rank_id)

    # Pokud uživatel nemá roli, tak mu ji nesmažeme, protože nemáme co smazat
    if rank_id in list_users_ranks:
        pass
    else:
        await ctx.send(f"{ctx.author.mention} Nemáš patřičnou roli.")
        return

    # Přidávání ranku
    await ctx.author.remove_roles(rank_object)
    await ctx.send(f"{ctx.author.mention} Role {name.upper()} byla odstraněna.")


@rank_remove.error
async def rank_remove_error(ctx, error):
    await ctx.send(f"Nastala chyba s: {error}")


@bot.command()
@has_permissions(ban_members=True)
async def inf(ctx):
    if not str(ctx.channel) == channel_name:
        return
    await ctx.send(ctx.message.author)
    pass


asyncio.run(bot.run(token))