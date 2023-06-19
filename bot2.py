import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import youtube_dl
import requests
import json
import random
import glob
import face_recognition
import os, time
import urllib.request
import urllib
import requests
import face_recognition
import os, time

jpeg = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.jpeg")
png = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.png")
PNG = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.png")
jpg = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.jpg")
JPG = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.JPG")
gif = glob.glob("/root/discord-bots/hahahayoucantkillme/memes/*.gif")


myMemberID = 403982408573124619
juzeistID = 232492888833916938
warrenID = 252778671444721666

total = []
for i in range(0,len(jpeg)):
    total.append(jpeg[i])

for i in range(0,len(png)):
    total.append(png[i])

for i in range(0,len(PNG)):
    total.append(PNG[i])

for i in range(0,len(jpg)):
    total.append(jpg[i])

for i in range(0,len(JPG)):
    total.append(JPG[i])

for i in range(0,len(gif)):
    total.append(gif[i])

jpeg2 = glob.glob('/root/darkHumor/*.jpeg')
png2 = glob.glob('/root/darkHumor/*.png')
PNG2 = glob.glob('/root/darkHumor/*.PNG')
jpg2 = glob.glob('/root/darkHumor/*.jpg')
JPG2 = glob.glob('/root/darkHumor/*.JPG')
gif2 = glob.glob('/root/darkHumor/*.gif')

total2 = []
for i in range(0,len(jpeg2)):
    total2.append(jpeg2[i])

for i in range(0,len(png2)):
    total2.append(png2[i])

for i in range(0,len(PNG2)):
    total2.append(PNG2[i])

for i in range(0,len(jpg2)):
    total2.append(jpg2[i])

for i in range(0,len(JPG2)):
    total2.append(JPG2[i])

for i in range(0,len(gif2)):
    total2.append(gif2[i])


client = discord.Client()

players = {}
#client = commands.Bot(command_prefix = "!")
myToken = "your token"
"""
if not discord.opus.is_loaded():
    discord.opus.load_opus("opus")
"""
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@client.event
async def on_ready():
        try:
            print(client.user.name)
            print(client.user.id)

        except Exception as e:
            print(e)


async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def on_message(message):
    if message.context.startswith("hi"):
        print("h geldi")
    else:
        print("h gelmedi ?!")

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()
    @commands.command()
    async def ip(self,ctx):
            print("ipdeki ctx is :", ctx )
            args = ["88.230.129.17"]
            try:
                req = requests.get('http://ip-api.com/json/{}'.format(args[0]))
                resp = json.loads(req.content.decode())
                if req.status_code == 200:
                    if resp['status'] == 'success':
                        template = '**{}**\n**IP: **{}\n**City: **{}\n**State: **{}\n**Country: **{}\n**Latitude: **{}\n**Longitude: **{}\n**ISP: **{}'
                        out = template.format(args[0], resp['query'], resp['city'], resp['regionName'], resp['country'], resp['lat'], resp['lon'], resp['isp'])
                        print(out)
                        return out
                    elif resp['status'] == 'fail':
                        print("failed api req")
                        return 'API Request Failed'
                    else:
                        return 'HTTP Request Failed: Error {}'.format(req.status_code)
            except Exception as e:


                print(e)
    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(ctx.author.voice.channel)

        await ctx.author.voice.channel.connect()

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()



    @commands.command()
    async def ohyeahyeah(self, ctx):
        async with ctx.typing():
            player = await YTDLSource.from_url("https://www.youtube.com/watch?v=7fFSupGfZME", loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def kick(self, ctx, member:discord.Member):
        #if ctx.message.author.has_permissions.administrator and ctx.message.server.me.has_permissions.kick_members:
        if ctx.message.channel.permissions_for(ctx.message.author).kick_members:
            await ctx.guild.kick(member)
            await ctx.send("{} İsimli orospu evladi discorddan kick yedi".format(member))
        else:
            await ctx.send("{} Ya orospu evladı sen kimsin ki kickleme yetkin olacak bir de aq".format(ctx.message.author))
    @commands.command()
    async def aq(self,ctx):
        await ctx.send(file=discord.File('/root/discord-bots/hahahayoucantkillme/memes/'+"1.jpeg"))
    @commands.command()
    async def send(self,ctx):
        if ctx.message.author.id == juzeistID:
            await ctx.send(file=discord.File("/root/discord-bots/hahahayoucantkillme/memes/ismailkardesi.jpeg"))
        else:
            rand = random.randint(0,len(total))
            await ctx.send(file=discord.File(total[rand]))
    @commands.command()
    async def ananisikim(self,ctx):
        await ctx.send("bende senin anani sikim")
    @commands.command()
    async def dark(self,ctx):
        rand = random.randint(0,len(total2))
        await ctx.send(file=discord.File(total2[rand]))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'haha' in  message.content:
        await message.channel.send("hehe")


    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("send"):
        await message.channel.send('Hello', file=discord.File('/usr/local/lib/python3.7/site-packages/discord/yeah.jpeg'))

    """
    TODO : Birden fazla file göndermek için kullan ->
    my_files = [
        discord.File('cool.png', 'testing.png'),
        discord.File(some_fp, 'cool_filename.png'),
    ]

    await channel.send('Your images:', files=my_files)
    """
    """
    TODO : Bombos bisey ama kalsın.
    if message.content.startswith("messages"):
        messages = await message.channel.history().flatten()
        for message in messages:
            print(message)
    """
    if message.content.startswith("play"):
        try:
            vc = await message.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="https://www.youtube.com/watch?v=wmZmRxKSCtE"), after=lambda e: print('done', e))
            #vc.is_playing()
            #vc.pause()
            #vc.resume()
            #vc.stop()
        except Exception as e:
            print("exception e:",e)
    if message.content.startswith("h"):
        #server = message.server
        try:
            vc = await message.author.voice.channel.connect()
            player = await vc.create_ffmpeg_player("https://www.youtube.com/watch?v=wmZmRxKSCtE")
            #vc.play(discord.FFmpegPCMAudio('chopin.mp3'), after=lambda e: print('done', e))
            #player = vc.play(discord.PCMAudio("https://www.youtube.com/watch?v=wmZmRxKSCtE"))
            #players[server.id] = player
            #player = discord.FFmpegPCMAudio(source ="https://www.youtube.com/watch?v=wmZmRxKSCtE")
            player.start()
        except Exception as e:
            print("exception e: ",e)

    if message.content.startswith("q"):
        author = message.author
        voice_channel = await author.voice.channel.connect()

        player = await voice_channel.create_ytdl_player(url)
        player.start()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                description='Relatively simple music bot example')
#client.run(myToken)
@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

async def send_cmd_help(ctx):
    print("noluyo burda")
    await bot.send_message("hehe")


@bot.listen()
async def on_message(message):
    print("message is : ",message)

    if not message.attachments:
        print("no attachments")
    else:
        print("type1 : ",type(message.attachments))
        print("type2 : ",type(message.attachments[0]))
        print("message.url? : ",message.attachments[0])
        print("message.url? : ",message.attachments[0].url)
        try:
            img_data = requests.get(message.attachments[0].url).content
            with open('image_name.jpg', 'wb') as handler:
                handler.write(img_data)
            try:
                path = "/Users/kaancaglan/development/discord/discord-bot/hahahayoucantkillme/"
                filename="cat.jpeg"
                picture_of_filename = face_recognition.load_image_file(filename)
                #picture_of_filename = face_recognition.load_image_file(myFile)
                my_face_encoding_filename = face_recognition.face_encodings(picture_of_filename)[0]
                filename2 = "pp.png"
                picture_of_filename2 = face_recognition.load_image_file(filename2)
                unknown_face_encoding = face_recognition.face_encodings(picture_of_filename2)[0]
                result = face_recognition.compare_faces([my_face_encoding_filename], unknown_face_encoding, tolerance=0.55)
                print("result is : ",result)
            except Exception as exc:
                print("encodingte haatalar:",exc)
        except Exception as e:
            print("errrrr is : ",e)
        
    if 'fna.fbcdn.net' in message.content:
        await message.channel.send("{} İsimli orospu evladi facebook linki paylaşmaktan dolayı discorddan kick yedi".format(message.author))
        await message.guild.kick(message.author)
    if "apex" in message.content:
        if message.author.id != 568136052678721576:
            print("apex deme aq")
            #await bot.send_message(message.channel, "Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))
            await message.channel.send("Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))

    elif "apx" in message.content:
        if message.author.id != 568136052678721576:
            #await bot.send_message(message.channel, "Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))
            await message.channel.send("Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))

    elif "aepx" in message.content:
        if message.author.id != 568136052678721576:
            #await bot.send_message(message.channel, "Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))
            await message.channel.send("Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))

    elif "apexx" in message.content:


        if message.author.id != 568136052678721576:
            #await bot.send_message(message.channel, "Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))
            await message.channel.send("Bu discordda apex ile ilgili yazılan yazıları hoş karşılamayız sayın orospu evladi {}".format(message.author))
    print("message is : ",message.content)
    """
@bot.event(pass_context=True)
async def on_message(message, ctx):
    if ctx.content.startswith("!dark"):
        print("e dark geldi iste")
        await ctx.send("hahahaha")

@bot.event
async def on_message(message):
    print("message was :  ",message.content)
    print("author : ", message.author)
    print("wholeMes: ",message)
    #await bot.send_message("{} napiyon aq evladi".format(message.author))
"""
@bot.command()
async def add(ctx, a: int, b: int):
    print("brreaHh     ctx is : ",ctx)
    await ctx.send(a+b)


bot.add_cog(Music(bot))
bot.run(myToken)
