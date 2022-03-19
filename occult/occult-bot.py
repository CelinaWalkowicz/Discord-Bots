'''
Occult Bot for Discord
* Moon Phase Announcements
* Users Are Able to Request:
    -Tarot Card Readings
    -Daily Horoscopes

Structure
1. Import Dependancies & Load .env
2. Discord Connection
3. Variables
    - Horoscope
    - Tarot
4. Functions
    - Misc
    - Horoscope
    - Tarot
    - Moonphase
5. Callbacks
    - Horoscope
    - Tarot
    - Moonphase
'''

# 1. Imports & .env

# Imports
import os, asyncio, discord
import requests, json
import random, time
import emoji
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 2. Discord Connection

# load env file
load_dotenv()

# Connections

# Discord
TOKEN = os.getenv('OCCULT_TOKEN')
client = discord.Client()

# Geocode
geolocator = Nominatim(user_agent = 'cantankerous_pfifferling_occult_bot')

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 3. Variables

# Horoscope
aries = emoji.emojize(':aries:')
taurus = emoji.emojize(':taurus:')
gemini = emoji.emojize(':gemini:')
cancer = emoji.emojize(':cancer:')
leo = emoji.emojize(':leo:')
virgo = emoji.emojize(':virgo:')
libra = emoji.emojize(':libra:')
scorpio = emoji.emojize(':scorpius:')
sagittarius = emoji.emojize(':sagittarius:')
capricorn = emoji.emojize(':capricorn:')
aquarius = emoji.emojize(':aquarius:')
pisces = emoji.emojize(':pisces:')

# Tarot
# Tarot Card Data from https://github.com/ekelen
# Thank ekelen for putting this all together!
tarot_json = 'https://raw.githubusercontent.com/CelinaWalkowicz/tarot-api/master/static/card_data.json'
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
def month_num_to_name(month_num):
    """
    Takes a String or Int input of a Month's Number, and returns
    a string of the the name of the corresponding Month.
    """

    month_names = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'Novemeber', 'December',
    ]

    # Save Month Index to Determine Month Name
    idx = int(month_num) - 1
    month = month_names[idx]

    return month

def zip_to_latlon(city, state=0, country=0 ):
    'Returns the latitude and longitude for a zipcode using geopy'
    if state != 0:
        location = geolocator.geocode(city, state)
    else:
        location = geolocator.geocode(city, country)

    return location.latitude, location.longitude

def get_moonphase():
    'Gets the Moonphases'

# Horoscopes
def horo_date(json_data):
    'Converts YYYY-MM-DD date to MonthName DD, YYYY'

    # Separate Parts of the Date
    year = json_data['date'][:4]
    month_num = json_data['date'][5:7]
    day = json_data['date'][8:]

    month = month_num_to_name(month_num)

    return f'{month} {day}, {year}'


def get_horoscope_aquarius():
    'Retrieves Daily Aquarius Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/aquarius")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{aquarius} {json_data['sign'].upper()} {aquarius}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_pisces():
    'Retrieves Daily Pisces Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/pisces")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{pisces} {json_data['sign'].upper()} {pisces}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_aries():
    'Retrieves Daily Aries Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/aries")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{aries} {json_data['sign'].upper()} {aries}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_taurus():
    'Retrieves Daily Taurus Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/taurus")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{taurus} {json_data['sign'].upper()} {taurus}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_gemini():
    'Retrieves Daily Gemini Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/gemini")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{gemini} {json_data['sign'].upper()} {gemini}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_cancer():
    'Retrieves Daily Cancer Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/cancer")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{cancer} {json_data['sign'].upper()} {cancer}


{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_leo():
    'Retrieves Daily Leo Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/leo")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{leo} {json_data['sign'].upper()} {leo}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_virgo():
    'Retrieves Daily Virgo Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/virgo")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{virgo} {json_data['sign'].upper()} {virgo}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_libra():
    'Retrieves Daily Libra Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/libra")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{libra} {json_data['sign'].upper()} {libra}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_scorpio():
    'Retrieves Daily Scorpio Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/scorpio")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{scorpio} {json_data['sign'].upper()} {scorpio}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_sagittarius():
    'Retrieves Daily Sagittarius Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/sagittarius")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{sagittarius} {json_data['sign'].upper()} {sagittarius}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


def get_horoscope_capricorn():
    'Retrieves Daily Capricorn Horoscope'
    response = requests.get("https://ohmanda.com/api/horoscope/capricorn")
    json_data = json.loads(response.text)
    date = horo_date(json_data)
    horoscope = f'''
{capricorn} {json_data['sign'].upper()} {capricorn}

{date}
{json_data['horoscope']}
    '''
    return(horoscope)


# Tarot
def retrieve_cards():
    'Retrieves Card JSON Data'

    response = requests.get(tarot_json)
    json_data = json.loads(response.text)
    cards = json_data['cards']

    return cards


def shuffle_cards():
    'Randomly Shuffles Cards'

    # Retrieve Card Data
    cards = retrieve_cards()

    # Random Shuffle
    shuffled_cards = random.sample(cards, len(cards))

    return shuffled_cards


def draw(idx):
    'Draws One Card and Returns Card Information'

    # Shuffle Cards and Draw 1
    cards = shuffle_cards()
    draw = cards[idx]

    # Card Information
    name = draw['name']
    typ = draw['type']
    typ = typ.capitalize()
    mean_up = draw['meaning_up']
    mean_down = draw['meaning_rev']
    description = draw['desc']

    # Determine Card Orientation & Meaning
    meaning = ''
    orientation = ''
    chance = random.randint(0, 1)
    if chance == 0:
        meaning = mean_down
        orientation = 'reversed'
    else:
        meaning = mean_up
        orientation = 'upright'

    return name, typ, meaning, orientation, description


def read_one():
    'Returns Tarot Card Information and Message'

    # Draw Card
    name, typ, meaning, orientation, description = draw(0)

    typ_msg = f'''
A {typ} Arcana appears before you...
{name}...
    '''
    draw_info = f'''
{description}
     '''
    orientation_msg = f'''
Upon further reflection, you notice the card is {orientation}...
    '''
    meaning_msg = f'''
Reflect upon the card's meaning...
{meaning}
     '''

    return typ_msg, draw_info, orientation_msg, meaning_msg


def read_three():
    'Returns Messages for Three Tarot Cards'

    # Draw 1st Card
    name1, typ1, meaning1, orientation1, description1 = draw(0)
    # Draw 2nd Card
    name2, typ2, meaning2, orientation2, description2 = draw(1)
    # Draw 3rd Card
    name3, typ3, meaning3, orientation3, description3 = draw(2)


    # First Card Messages
    typ_msg1 = f'''
A {typ1} Arcana appears before you...
{name1}...
    '''
    draw_info1 = f'''
{description1}
    '''

    # Second Card Messages

    typ_msg2 = f'''
A {typ2} Arcana appears before you...
{name2}...
    '''
    draw_info2 = f'''
{description2}
    '''

    # Third Card Messages
    typ_msg3 = f'''
A {typ3} Arcana appears before you...
{name3}...
    '''
    draw_info3 = f'''
{description3}
    '''

    # Meaning Message
    three_meanings = f'''
Reflect upon the meanings of your cards...

{name1}, {orientation1}...
*{meaning1}*

{name2}, {orientation2}...
*{meaning2}*

{name3}, {orientation3}...
*{meaning3}*
    '''

    return (
        typ_msg1, draw_info1, typ_msg2, draw_info2,
        typ_msg3, draw_info3, three_meanings,
        )


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
            aq_horo = get_horoscope_aquarius()
            await message.channel.send(aq_horo)

        elif message.content.startswith('$pisces'):
            pi_horo = get_horoscope_pisces()
            await message.channel.send(pi_horo)

        elif message.content.startswith('$aries'):
            ar_horo = get_horoscope_aries()
            await message.channel.send(ar_horo)

        elif message.content.startswith('$taurus'):
            taur_horo = get_horoscope_taurus()
            await message.channel.send(taur_horo)

        elif message.content.startswith('$gemini'):
            gem_horo = get_horoscope_gemini()
            await message.channel.send(gem_horo)

        elif message.content.startswith('$cancer'):
            can_horo = get_horoscope_cancer()
            await message.channel.send(can_horo)

        elif message.content.startswith('$leo'):
            leo_horo = get_horoscope_leo()
            await message.channel.send(leo_horo)

        elif message.content.startswith('$virgo'):
            vir_horo = get_horoscope_virgo()
            await message.channel.send(vir_horo)

        elif message.content.startswith('$libra'):
            lib_horo = get_horoscope_libra()
            await message.channel.send(lib_horo)

        elif message.content.startswith('$scorpio'):
            scor_horo = get_horoscope_scorpio()
            await message.channel.send(scor_horo)

        elif message.content.startswith('$sagittarius'):
            sag_horo = get_horoscope_sagittarius()
            await message.channel.send(sag_horo)

        elif message.content.startswith('$capricorn'):
            cap_horo = get_horoscope_capricorn()
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
