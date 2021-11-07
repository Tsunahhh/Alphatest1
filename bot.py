from discord.ext import commands
import random

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print("Le bot est prêt à fonctionner :D")


@bot.command(name="aide")
async def aide(ctx):
    await ctx.channel.send("""**Help**
    __**prefix**__: **"."**
    __**Commandes:**__
    .help - Affiche les commandes avc les expliquations
    .ping - Revoie pong ??
    .tsuna - Renvoie Atsu
    .atsu - Renvoie Tsuna
    .dé - Revoie un chiffre aléatoire entre 1 - 6
    .hz d f - Commdande pour choisir un chiffre entre d et f
    .infinite - Commande de spam jusqu a 100
    .+ *args - Somme des chiffres/nombres séparé d'un espace
    .delta a b c - Trouve le x d'une éq du 2e degré
    .moy *args - Fait la moyenne des chiffres séparés d'un espace
    """)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(name="tsuna")
async def tsuna(ctx):
    await ctx.channel.send("Atsu")


@bot.command(name="atsu")
async def atsu(ctx):
    await ctx.channel.send("Tsuna")


@bot.command(name="dé")
async def de6(ctx):
    await ctx.channel.send(random.randint(1, 6))


@bot.command(name="hz")
async def hz(ctx, d: int, f: int):
    await ctx.channel.send(random.randint(d, f))


@bot.command(name="infinite")
async def infinite(ctx):
    x = 0
    while x < 101:
        await ctx.channel.send(f"SPAMMMMMMM {x}")
        x += 1


@bot.command(name="+")
async def som(ctx, *args: int):
    s = 0
    for i in args:
        s += i
    await ctx.channel.send(s)


@bot.command(name="delta")
async def delta(ctx, *args: int):
    a = args[0]
    b = args[1]
    c = args[2]
    delta = b**2 - 4*a*c
    if delta < 0:
        await ctx.channel.send("Pas de solutions possible")
    elif delta == 0:
        await ctx.channel.send(f"Une solution x: {-b/2*a}")
    else:
        racine = delta**0.5
        x1 = (-b + racine) / (2*a)
        x2 = (-b - racine) / (2*a)
        await ctx.channel.send(f"x1 = {x1}, x2 = {x2}")


@bot.command(name="moy")
async def moy(ctx, *args: int):
    long = len(args)
    res = 0
    for i in args:
        res += i
    await ctx.channel.send(f"Moyenne: {res/long}")


bot.run("TOKEN")
