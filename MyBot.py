import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import logging
import time
import datetime
import random
import asyncio


Client = discord.Client() #Starts the client/Starts discord.
client = commands.Bot(command_prefix = '!')#Initialises the client bot/Runs the client bot.
start_time = datetime.datetime.utcnow()
startup_extensions=['Music']

@client.event
async def auto_run():
    while True:
        print('Keeping bot up')
        await asyncio.sleep(900)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='!Menu'))
    print('Bot is loaded') #This will be called when the bot connects to the server.
client.loop.create_task(auto_run())

class Main_Commands():
    def __init__(self, bot):
        self.bot=bot

@client.event
async def on_message(message):
    if message.content.startswith('!'):#FOR CMDS.
        if message.content.upper().startswith('!MENU'):#PUBLIC, MENU.
            userID=message.author.id
            emb=(discord.Embed(description='Welcome! This is Milo\'s bot, this was honestly created for no reason other than to mess around, honestly. There are many different commands you can use, try, and have fun with. You can get started on any server which contains this bot by typing `!Menu` in any channel. You will get a series of commands and such which was said, you could mess about with. There is nothing really more to say, really, as this bot is honestly just a WIP (Work In Progress). Have fun! \n \n If you need to contact the owner of the bot: `Milo#5695`',colour=0x8B008B))
            emb.set_author(name='Milo\'s bot.', icon_url='https://cdn.discordapp.com/attachments/466983189198405642/515220774609485833/unknown.png')
            emb.add_field(name='Basic commands!', value='''
    !Menu - Brings up the menu into your DM's!
    !Owner - Tells you who the owner is!
    !Ping - Makes the bot say Pong!
    !Pong - Makes the bot say Ping!
    !6Dice - Rolls a six sided dice!
    !20Dice - Rolls a twenty sided dice!
    !Ultradice - Rolls a random number of dice with a random number of sides!
    !Whoami - Just in-case you forget who you are!
    !Coinflip - Flips a coin, that's it!
    !Russian - Plays russian roulette!
    !Communism - Sends a random image, filled with communist pride!
    !LMao - Sends a picture of Mao Zedong, the greatest leader in China's history!
    !GoodBot - Calls the bot a good bot!
    !BadBot - Calls the bot a bad boy!
    !Uptime - Tells you how much the bot has been running for!
    !Updog - Asks you whats updog!''')
            emb.add_field(name='Complex Commands!', value='''!Rand - Generates a random number between one and the number you type after!
    !Fizzbuzz - Plays the game of fizzbuzz!
    !Echo - Makes the bot say whatever you have said!
    !Delecho - Makes the bot say whatever you have said, doesn\'t show your message!
    !8Ball - Replies to the question asked by you!
    !Match - Tells you the compatability of two things!
    !SmashorPass - Asks the bot if it would smash or pass!
    !Pick - Makes the bot pick something out of the given list!

    Note, to use the complex commands, you need something after it:
    !Echo, !Delecho, !8Ball, !SmashorPass, !Pick or !Match need characters in-order to work, a question or two objects.
    !Fizzbuzz and !Rand needs a number in-order to work.''')
            await client.send_message(message.channel,'The list of commands has been sent to you, <@%s>!'%(userID))
            await client.send_message(message.author, embed=emb)

        elif message.content.upper().startswith('!UPTIME'):#PUBLIC, USED FOR UPTIME.
            now=datetime.datetime.utcnow()
            delta=now-start_time
            hours,remainder=divmod(int(delta.total_seconds()),3600)
            minutes,seconds=divmod(remainder,60)
            days,hours=divmod(hours,24)
            if days:
                time_format='**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds.'
            else:
                time_format='**{h}** hours, **{m}** minutes, and **{s}** seconds.'
            uptime_stamp=time_format.format(d=days,h=hours,m=minutes,s=seconds)
            await client.send_message(message.channel,'{} has been up for: {}'.format(client.user.name, uptime_stamp))

        elif message.content.upper().startswith('!UPDOG'):#PUBLIC, WHATS UP DOG?
            userID=message.author.id
            await client.send_message(message.channel,'What\'s up dog? <@%s>!'%(userID))

        elif message.content.upper().startswith('!RUSSIAN'):#PUBLIC, RUSSIAN ROULETTE.
            userID=message.author.id
            chamber=random.randint(1,6)
            if chamber==6:
                await client.send_message(message.channel,'You have been shot! :gun: <@%s>!'%(userID))
                return
            else:
                await client.send_message(message.channel,'You have lived to tell the tale, <@%s>!'%(userID))
            
        elif message.content.upper().startswith('!WHOAMI'):#PUBLIC, WHO AM I.
            userID=message.author.id
            await client.send_message(message.channel,'You are <@%s>!'%(userID))

        elif message.content.upper().startswith('!GOODBOT'):#PUBLIC, CALLS BOT A GOOD BOY.
            await client.add_reaction(message,u'\U0001F917')

        elif message.content.upper().startswith('!BADBOT'):#PUBLIC, CALLS BOT A BAD BOY.
            await client.add_reaction(message,u'\U0001F622')

        elif message.content.upper().startswith('!PING'):#PUBLIC, PING PONG.
            randomping=random.randint(1,10)
            userID=message.author.id
            if randomping==9:
                await client.send_message(message.channel,'<@%s> Po- oh no...I missed..'%(userID))
            elif randomping==10:
                await client.send_message(message.channel,'<@%s> Hah, you missed!'%(userID))
            else:
                await client.send_message(message.channel,'<@%s> Pong! :ping_pong:'%(userID))

        elif message.content.upper().startswith('!PONG'):#PUBLIC, PONG PING.
            randompong=random.randint(1,10)
            userID=message.author.id
            if randompong==9:
                await client.send_message(message.channel,'<@%s> Pi- oh no...I missed..'%(userID))
            elif randompong==10:
                await client.send_message(message.channel,'<@%s> Hah, you missed!'%(userID))
            else:
                await client.send_message(message.channel,'<@%s> Ping! :ping_pong:'%(userID))

        elif message.content.upper().startswith('!FIZZBUZZ'):#PUBLIC, FIZZBUZZ
            try:
                num=message.content.split()
                number=''
                for word in num[1:]:
                    number+=word
                    number=float(number)
                    if number%3==0 and number%5==0:
                        await client.send_message(message.channel,'Fizzbuzz.')
                    elif number%3==0 and not number%5==0:
                        await client.send_message(message.channel,'Fizz.')
                    elif number%5==0 and not number%3==0:
                        await client.send_message(message.channel,'Buzz.')
                    else:
                        await client.send_message(message.channel,number)
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!6DICE'):#PUBLIC, 6 SIDED DICE ROLL.
            await client.send_message(message.channel,'You got the number: {}!'.format(random.randint(1,6)))

        elif message.content.upper().startswith('!20DICE'):#PUBLIC, 20 SIDED DICE ROLL.
            await client.send_message(message.channel,'You got the number: {}!'.format(random.randint(1,20)))

        elif message.content.upper().startswith('!ULTRADICE'):#PUBLIC, A FUCK TON OF DICE.
            swap=0
            dicerolls=random.randint(1,1000)
            dicenumst=random.randint(1,1000000000)
            dicenumed=random.randint(1,1000000000)
            if dicenumst>dicenumed:
                swap=dicenumed
                dicenumed=dicenumst
                dicenumst=swap
            for i in range(dicerolls):
                add=random.randint(dicenumst,dicenumed)
                swap=swap+add
            await client.send_message(message.channel,'You got the number: {}. Using the start position of {}, end position of {}, and the number of rolls: {}!'.format(swap,dicenumst,dicenumed,dicerolls))

        elif message.content.upper().startswith('!EXPLODINGDICE'):#PUBLIC, EXPLODING DICE.
                explode=0
                rollnum=1
                roll=random.randint(1,6)
                while roll==6:
                    explode=explode+6
                    rollnum=rollnum+1
                    roll=random.randint(1,6)
                roll=roll+explode
                await client.send_message(message.channel,'You have gotten {} with {} rolls!'.format(roll,rollnum))

        elif message.content.upper().startswith('!MATCH'):#PUBLIC, TESTS THE COMPATABILITY OF IDK.
            try:
                matchperf=0
                msg=message.content.split()
                firstthing=msg[1]
                secondthing=msg[2]
                comp=random.randint(1,100)
                if firstthing.upper()=='MIWO' or firstthing.upper()=='MILO' or firstthing.upper()=='SWEN' or firstthing.upper()=='SWENNO' or firstthing.upper()=='SEN' or firstthing.upper()=='SENNO' or firstthing.upper()=='SENS' or firstthing.upper()=='MILOS' or firstthing.upper()=='SENNOS' or firstthing.upper()=='SWENS' or firstthing.upper()=='MIWOS' or firstthing.upper()=='SWENNOS':
                    matchperf=matchperf+1
                if secondthing.upper()=='SWEN' or secondthing.upper()=='SWENNO' or secondthing.upper()=='SEN' or secondthing.upper()=='SENNO' or secondthing.upper()=='MIWO' or secondthing.upper()=='MILO'or secondthing.upper()=='SENS' or secondthing.upper()=='MILOS' or secondthing.upper()=='SENNOS' or secondthing.upper()=='SWENS' or secondthing.upper()=='MIWOS' or secondthing.upper()=='SWENNOS':
                    matchperf=matchperf+1
                if matchperf==2:
                    await client.send_message(message.channel,'You two match better than another else! <3')
                else:
                    if 20>comp:
                        await client.send_message(message.channel,'You two really, really don\'t match...Sorry!')
                        return
                    elif 40>comp:
                        await client.send_message(message.channel,'You two match a bit...')
                        return
                    elif 60>comp:
                        await client.send_message(message.channel,'You two match well!')
                        return
                    elif 80>comp:
                        await client.send_message(message.channel,'You two match very well!')
                        return
                    elif 100>comp:
                        await client.send_message(message.channel,'Just do it already!!')
                        return
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!RAND'):#PUBLIC, RANDOM NUMBER GENERATOR
            try:
                num=message.content.split(' ')
                number1=''
                for word in num[1]:
                    number1+=word
                await client.send_message(message.channel,'You got the number: {}!'.format(random.randint(1,(float(number1)))))
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!ECHO'):#PUBLIC, BOT WRITES WHAT USER WROTE.
            try:
                msg=message.content.split()
                output=''
                for word in msg[1:]:
                    output+=word
                    output+=' '
                await client.send_message(message.channel,output)
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!DELECHO'):#PUBLIC, BOT WRITES WHAT USER WROTE AND DELETES MESSAGE.
            try:
                msg=message.content.split()
                output=''
                for word in msg[1:]:
                    output+=word
                    output+=' '
                await client.delete_message(message)
                await client.send_message(message.channel,output)
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!COINFLIP'):#PUBLIC, HEADS OR TAILS.
            Choice=['Heads','Tails']
            await client.send_message(message.channel,'You have gotten: '+random.choice(Choice))

        elif message.content.upper().startswith('!OWNER'):#PUBLIC, JUST FOR HELP OR ANY INFO.
            await client.send_message(message.channel,'If you want to contact the owner of the bot: Milo#5695')

        elif message.content.upper().startswith('!COMMUNISM'):#PUBLIC, COMMUNISM IMAGES/MUSIC.
            commiecounter=random.randint(1,4)
            if commiecounter==1:
                await client.send_file(message.channel, 'C:/MilosBot/Images/HammerandSickleRedCircle.png')
                return
            elif commiecounter==2:
                await client.send_file(message.channel, 'C:/MilosBot/Images/HammerandSickleYellow.png')
                return
            elif commiecounter==3:
                await client.send_file(message.channel, 'C:/MilosBot/Images/USSRflag.png')
                return
            elif commiecounter==4:
                await client.send_file(message.channel, 'C:/MilosBot/Images/StalinFace.png')
                return

        elif message.content.upper().startswith('!SLAP'):#PUBLIC, SLAPS A RANDOM PERSON IN THE SERVER.
            memberlist=[]
            x = message.server.members
            for member in x:
                memberlist.append(member.name)
            person=random.choice(memberlist)
            if person=="Milo's bot or something.":
                await client.send_message(message.channel,'Oh no, I slapped myself...')
            else:
                await client.send_message(message.channel,'You have been slapped, {}!'.format(person))

        elif message.content.upper().startswith('!SMASHORPASS'):#PUBLIC, SMASH OR PASS.
            try:
                Choice=['Smash.','Pass.']
                msg=message.content.split()
                person=msg[1]
                if person.upper()=='MIWO' or person.upper()=='MILO':
                    await client.send_message(message.channel,'I can\'t smash my owner!')
                elif person.upper()=='SEN' or person.upper()=='SWEN' or person.upper()=='SENNO' or person.upper()=='SWENNO':
                    await client.send_message(message.channel,'Only my owner can smash them!')
                else:
                    await client.send_message(message.channel,random.choice(Choice))
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!LMAO'):#PUBLIC, SHOWS A PICTURE OF MAO.
            await client.send_file(message.channel, 'C:/MilosBot/Images/LMao.png')

        elif message.content.upper().startswith('!8BALL'):#PUBLIC, IT'S A MAGIC 8BALL.
            try:
                Choice=['It is certain.','As I see it, yes.','Reply hazy, try again.',' Don\'t count on it.','It is decidedly so.','Most likely.','Ask again later.','My reply is no.','Without a doubt.','Outlook good.','Better not tell you now.','My sources say no.','Yes - definitely.','You may rely on it.','Yes.','Signs point to yes.','Cannot predict now.','Concentrate and ask again.','Outlook not so good.','Very doubtful.']
                await client.send_message(message.channel,random.choice(Choice))
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!PICK'):#PUBLIC, MAKES BOT CHOOSE AN OPTION
            try:
                msg=message.content.split()
                del msg[0]
                if msg[0[1]]=='':
                    await client.send_message(message.channel,'oof')
                await client.send_message(message.channel,random.choice(msg))
            except Exception as exc:
                await client.send_message(message.channel, "An error has occured, oof. ```{ttt}```".format(ttt=exc))

        elif message.content.upper().startswith('!DEFINECUTE'):#PRIVATE, ONLY USE WITH SENNO <333
            await client.send_message(message.channel,'Senno! <3')

        elif message.content.upper().startswith('!DEFINESNUGGLY'):#PRIVATE, ONLY USE WITH SENNO <333
            await client.send_message(message.channel,'Squishy Senno! <3')

        elif message.content.upper().startswith('!DEFINEBESTESTBOYER'):#PRIVATE, ONLY USE WITH SENNO <333
            await client.send_message(message.channel,'Their name starts with S and ends in N...Sen! <3')

        elif message.content.upper().startswith('!SEN'):#PRIVATE, ONLY USE WITH SENNO <333
            await client.send_file(message.channel, 'C:/MilosBot/Images/Sen.png')
            return

        elif message.content.upper().startswith('!NUDES'):#PRIVATE, IDK, USE ONLY WITH SENNO <333
            await client.send_message(message.channel,'**Insert nudes of one of you two here.**')

        elif message.content.upper().startswith('!IMALREADY'):#PRIVATE, ONLY USE WITH OVERWATCH SERVER.
            characters=['Ana','Ashe','Bastion','Brigitte','D.va','Doomfist','Genji','Hanzo','Junkrat','Lúcio','Mccree','Mei','Mercy','Moira','Orisa','Pharah','Reaper','Reinhardt','Roadhog','Soldier: 76','Sombra','Symmetra','Torbjörn','Tracer','Widowmaker','Winston','Wrecking Ball','Zarya','Zenyatta']
            await client.send_message(message.channel,random.choice(characters))

        elif message.content.upper().startswith('!POLL'):#PRIVATE, ONLY USE WITH OVERWATCH SERVER.
            msg=message.content.split()
            output=''
            for word in msg[1:]:
                output+=word
                output+=' '
            await client.delete_message(message)
            message=await client.send_message(message.channel,output)
            await client.add_reaction(message,u'\U0001F44D')
            await client.add_reaction(message,u'\U0001F44E')

        elif message.content.upper().startswith('!SHUT'):#PRIVATE, ONLY FOR MY USE.
            if message.author.id=='207871573842067456':
                await client.delete_message(message)
                await client.send_message(message.channel,'The bot is shutting off, see you next time!')
                await client.logout()
            else:
                await client.delete_message(message)

        elif message.content.upper().startswith('!KS'):#PRIVATE, ONLY FOR MY USE.
            if message.author.id=='207871573842067456':
                await client.delete_message(message)
                await client.send_message(message.channel,'The bot has been killswitched, oof.')
                await client.logout()
            else:
                await client.delete_message(message)
    else:
        if message.author.id=='454669634965209088':
            return message
        else:
            emote=random.randint(0,1000)
            if emote>800:
                await client.add_reaction(message,u'\U0001F3A9')
            elif 100>emote:
                await client.add_reaction(message,u'\U0001F575')
            elif emote==500:
                await client.add_reaction(message,u'\U0001F40D')
        
    

if __name__=='__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc='{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


bot token:client.run(str(os.environ.get('NDU0NjY5NjM0OTY1MjA5MDg4.DrYjPQ.jYOjH-Bfzg-L3dvpdl4p6hQ9Uvo'))) #Bot token
