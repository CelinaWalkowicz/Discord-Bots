'''
Occult Bot for Discord
* Moon Phase Announcements
* Users Are Able to Request:
    -Tarot Card Readings
    -Daily Horoscopes

Structure
1. Import Dependancies & Load .env
2. Connections
    - Env
    - Discord
    - Geopy
3. Variables
    - Emojis
    - Tarot Messages
4. Functions
5. Callbacks
    - Horoscope
    - Tarot
        - Draws
        - Information
    - Moonphase
'''

# 1. Imports & .env

# Imports
import os, asyncio, discord
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

# Local Imports

# Horoscope
from horoscopes import get_horoscope

# Tarot
from tarot import read_one
from tarot import read_three

# Moon Phase
# from  moonphase

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 2. Discord Connection

# load env file
load_dotenv()

# Connections

# Discord
TOKEN = os.getenv('OCCULT_TOKEN')
client = discord.Client()

# Geocode
GEOPY = os.getenv('GEOPY_USER')
geolocator = Nominatim(user_agent=GEOPY)

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 3. Variables

# Emoji Reactions
aries_emoji = '\N{ARIES}'
taurus_emoji = '\N{TAURUS}'
gemini_emoji = '\N{GEMINI}'
cancer_emoji = '\N{CANCER}'
leo_emoji = '\N{LEO}'
virgo_emoji = '\N{VIRGO}'
libra_emoji = '\N{LIBRA}'
scorpio_emoji = '\N{SCORPIUS}'
sagittarius_emoji = '\N{SAGITTARIUS}'
capricorn_emoji = '\N{CAPRICORN}'
aquarius_emoji = '\N{AQUARIUS}'
pisces_emoji = '\N{PISCES}'

# Tarot Messages
shuffle_msg = '''
    Ruminate upon your question while your cards are shuffled...
    '''
draw_msg1 = 'A card is placed before you...'
draw_msg2 = 'And another...'
draw_msg_fin = 'Your final card is drawn...'
draw3_msg = 'A fan of cards waits before you...'
turn_msg1 = 'Your card turns...'
turn_msg_first = 'You first card turns...'
turn_msg_nxt = 'Your next card turns...'
turn_msg_fin = 'Your final card turns...'

# Thank you https://giphy.com/rhiannamoon
tarot_gif = 'https://i.giphy.com/media/SrWh9peE9r1MTVr8aQ/giphy.webp'

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 4. Functions


# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 5. Callbacks

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_guild_join(guild):
    print('occult-bot has joined.')

@client.event
async def on_guild_remove(guild):
    print('occult-bot has been removed.')


# Message Replies
@client.event
async def on_message(message):
    # Checks Author is not bot
    if message.author == client.user:
        return

    # Check Messages Are from Horoscope Channel
    if message.channel.name == 'horoscope':

        if message.content.startswith('$aquarius'):
            aq_horo = get_horoscope('aquarius')
            await message.add_reaction(aquarius_emoji)
            await asyncio.sleep(2)
            await message.channel.send(aq_horo)

        elif message.content.startswith('$pisces'):
            pi_horo = get_horoscope('pisces')
            await message.add_reaction(pisces_emoji)
            await asyncio.sleep(2)
            await message.channel.send(pi_horo)

        elif message.content.startswith('$aries'):
            ar_horo = get_horoscope('aries')
            await message.add_reaction(aries_emoji)
            await asyncio.sleep(2)
            await message.channel.send(ar_horo)

        elif message.content.startswith('$taurus'):
            taur_horo = get_horoscope('taurus')
            await message.add_reaction(taurus_emoji)
            await asyncio.sleep(2)
            await message.channel.send(taur_horo)

        elif message.content.startswith('$gemini'):
            gem_horo = get_horoscope('gemini')
            await message.add_reaction(gemini_emoji)
            await asyncio.sleep(2)
            await message.channel.send(gem_horo)

        elif message.content.startswith('$cancer'):
            can_horo = get_horoscope('cancer')
            await message.add_reaction(cancer_emoji)
            await asyncio.sleep(2)
            await message.channel.send(can_horo)

        elif message.content.startswith('$leo'):
            leo_horo = get_horoscope('leo')
            await message.add_reaction(leo_emoji)
            await asyncio.sleep(2)
            await message.channel.send(leo_horo)

        elif message.content.startswith('$virgo'):
            vir_horo = get_horoscope('virgo')
            await message.add_reaction(virgo_emoji)
            await asyncio.sleep(2)
            await message.channel.send(vir_horo)

        elif message.content.startswith('$libra'):
            lib_horo = get_horoscope('libra')
            await message.add_reaction(libra_emoji)
            await asyncio.sleep(2)
            await message.channel.send(lib_horo)

        elif message.content.startswith('$scorpio'):
            scor_horo = get_horoscope('scorpio')
            await message.add_reaction(scorpio_emoji)
            await asyncio.sleep(2)
            await message.channel.send(scor_horo)

        elif message.content.startswith('$sagittarius'):
            sag_horo = get_horoscope('sagittarius')
            await message.add_reaction(sagittarius_emoji)
            await asyncio.sleep(2)
            await message.channel.send(sag_horo)

        elif message.content.startswith('$capricorn'):
            cap_horo = get_horoscope('capricorn')
            await message.add_reaction(capricorn_emoji)
            await asyncio.sleep(2)
            await message.channel.send(cap_horo)

    # Check Messages are from Tarot Channel
    if message.channel.name == 'tarot':

        if message.content.startswith('$draw1'):

            # Retrieve Card Information
            typ_msg, draw_info, orientation_msg, meaning_msg = read_one()

            # Reading.exe
            # Shuffle, Draw, and Turn
            await message.channel.send(shuffle_msg)
            await message.channel.send(tarot_gif)
            await asyncio.sleep(20)
            await message.channel.send(draw_msg1)
            await asyncio.sleep(3)
            await message.channel.send(turn_msg1)
            await asyncio.sleep(3)
            # Return Card Info
            await message.channel.send(typ_msg)
            await asyncio.sleep(3)
            await message.channel.send(draw_info)
            await asyncio.sleep(15)
            await message.channel.send(orientation_msg)
            await asyncio.sleep(3)
            await message.channel.send(meaning_msg)

        if message.content.startswith('$draw3'):

            # Retrieve Card Information
            (
            typ_msg1, draw_info1, typ_msg2, draw_info2,
            typ_msg3, draw_info3, three_meanings,
            ) = read_three()

            # Reading.exe
            # Shuffle and Draw
            await message.channel.send(shuffle_msg)
            await message.channel.send(tarot_gif)
            await asyncio.sleep(20)
            await message.channel.send(draw_msg1)
            await asyncio.sleep(3)
            await message.channel.send(draw_msg2)
            await asyncio.sleep(3)
            await message.channel.send(draw_msg2)
            await asyncio.sleep(3)
            await message.channel.send(draw3_msg)
            await asyncio.sleep(3)
            # Turn Cards
            await message.channel.send(turn_msg_first)
            await asyncio.sleep(3)
            await message.channel.send(typ_msg1)
            await asyncio.sleep(3)
            await message.channel.send(draw_info1)
            await asyncio.sleep(15)
            await message.channel.send(turn_msg_nxt)
            await asyncio.sleep(3)
            await message.channel.send(typ_msg2)
            await asyncio.sleep(3)
            await message.channel.send(draw_info2)
            await asyncio.sleep(15)
            await message.channel.send(turn_msg_fin)
            await asyncio.sleep(3)
            await message.channel.send(typ_msg3)
            await asyncio.sleep(3)
            await message.channel.send(draw_info3)
            await asyncio.sleep(5)
            await message.channel.send(three_meanings)


# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

client.run(TOKEN)
