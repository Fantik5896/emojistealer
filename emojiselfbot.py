import discord
import colorama
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', self_bot = True, intents=intents)

@client.event
async def on_ready():
    print("Emoji-Stealer Запущен.\n---\nEmoji-Stealer is launch.")
    print(f"Команда !getemoji отправляет запрашиваемое эмодзи прямо \nв чат сервера." + colorama.Fore.RED + " Вас могут забанить. Будьте осторожны и используйте команду !getemojicmd. \nОна отправляет ссылки на эмодзи (затем вы переходите по ним и скачиваете их.)" + colorama.Fore.RESET + "\n---\nThe !getemoji command sends the requested emoji \ndirectly to the server chat." + colorama.Fore.RED + " You may be banned. Be careful and use command !getemojicmd. \nThis send links directly  in this console. (Sorry for my english)" + colorama.Fore.RESET)

@client.command()
async def getemoji(ctx, emoji: discord.Emoji = None):
    if  emoji is None:
        await ctx.send("Введите эмодзи")
    else:
        await ctx.send(f"{emoji.url}")
        
@client.command()
async def getemojicmd(ctx, emoji: discord.Emoji = None):
    await ctx.message.delete()
    if emoji is None:
        print("Введите эмодзи")
    else:
        print(f"Название эмодзи/Emoji name: {emoji.name}; Ссылка/link: {emoji.url}")

client.run("your-token-here", bot = False) #You token account