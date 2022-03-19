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
import random
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
{aquarius_emoji} {json_data['sign'].upper()} {aquarius_emoji}

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
{pisces_emoji} {json_data['sign'].upper()} {pisces_emoji}

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
{aries_emoji} {json_data['sign'].upper()} {aries_emoji}

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
{taurus_emoji} {json_data['sign'].upper()} {taurus_emoji}

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
{gemini_emoji} {json_data['sign'].upper()} {gemini_emoji}

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
{cancer_emoji} {json_data['sign'].upper()} {cancer_emoji}


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
{leo_emoji} {json_data['sign'].upper()} {leo_emoji}

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
{virgo_emoji} {json_data['sign'].upper()} {virgo_emoji}

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
{libra_emoji} {json_data['sign'].upper()} {libra_emoji}

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
{scorpio_emoji} {json_data['sign'].upper()} {scorpio_emoji}

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
{sagittarius_emoji} {json_data['sign'].upper()} {sagittarius_emoji}

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
{capricorn_emoji} {json_data['sign'].upper()} {capricorn_emoji}

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

    # Fix Inaccurate Meanings & Implement Requested
    # Changes from Testers
    # Some changes are from https://www.biddytarot.com/

    # The Magician
    magic_desc = '''
The Magician card is numbered One – the number of new beginnings and opportunities – and associates with the planet of Mercury. He stands with one arm stretched upwards towards the Universe, and the other pointing down to the earth. His positioning represents his connection between the spiritual realms and the material realms. The Magician uses this relationship to create and manifest his goals in the physical realm. He is the conduit that converts energy into matter. The Magician’s robe is white, symbolising purity, and his cloak is red, representing worldly experience and knowledge.

On the table in front of him are the four symbols of the Tarot suits – a cup, pentacle, sword and wand – each symbolising one of the four elements – water, earth, air and fire. It is also a sign that he has all the tools (and elements) he needs to manifest his intentions into being. Above his head is the infinity symbol, and around his waist is a snake biting its own tail – both of which signal that he has access to unlimited potential. And in the foreground is an array of foliage and flowers, symbolising the blossoming and fruition of his ideas and aspirations.
    '''
    if name.lower() == 'the magician':
        description = magic_desc
        mean_up = 'Manifestation, resourcefulness, power, inspired action'
        mean_down = 'Manipulation, poor planning, untapped talents'

    # High Priestess
    hp_desc = '''
The High Priestess sits in front of a thin veil decorated with pomegranates. The veil represents the separate conscious and subconscious realms, the seen and the unseen, and serves to keep casual onlookers out. Only the initiated may enter. The pomegranates on the veil are a symbol of abundance, fertility and the divine feminine, and are sacred to Persephone who ate a pomegranate seed in the underworld and was forced to return every year.

On either side of The High Priestess stand two pillars, marking the entrance to this sacred, mystical temple (also associated with the Temple of Solomon). One pillar is black with the letter B (Boaz, meaning ‘in his strength’) and the other is white with the letter J (Jachin, meaning ‘he will establish’). The black and white colors of the pillars symbolize duality – masculine and feminine, darkness and light – stating that knowledge and acceptance of duality are required to enter this sacred space.

The High Priestess wears a blue robe with a cross on her chest and a horned diadem (or crown), both a symbol of her divine knowledge and her status as a divine ruler. In her lap, she holds a scroll with the letter TORA, signifying the Greater Law (according to A. E. Waite). It is partly covered, signifying that this sacred knowledge is both explicit and implicit, it will only be revealed when the student is ready to look beyond the material realm. The crescent moon at her feet symbolizes her connection with the divine feminine, her intuition and subconscious mind, and the natural cycles of the moon.
    '''

    if name.lower() == 'the high priestess':
        description = hp_desc
        mean_up = 'Intuition, sacred knowledge, divine feminine, the subconscious mind'
        mean_down = 'Secrets, disconnected from intuition, withdrawal and silence'

    # Fortitude: Description
    fort_remove = 'These higher meanings are, however, matters of inference, and I do not suggest that they are transparent on the surface of the card. They are intimated in a concealed manner by the chain of flowers, which signifies, among many other things, the sweet yoke and the light burden of Divine Law, when it has been taken into the heart of hearts. The card has nothing to do with self-confidence in the ordinary sense, though this has been suggested--but it concerns the confidence of those whose strength is God, who have found their refuge in Him.'
    if name.lower() == 'fortitude':
        description = description.replace(fort_remove, '')

    # The Tower: Description, Reverse Meaning
    tower_desc = '''
The Tower shows a tall tower perched on the top of a rocky mountain. Lightning strikes set the building alight, and two people leap from the windows, head first and arms outstretched. It is a scene of chaos and destruction.

The Tower itself is a solid structure, but because it has been built on shaky foundations, it only takes one bolt of lightning to bring it down. It represents ambitions and goals made on false premises.

The lightning represents a sudden surge of energy and insight that leads to a break-through or revelation. It enters via the top of the building and knocks off the crown, symbolizing energy flowing down from the Universe, through the crown chakra. The people are desperate to escape from the burning building, not knowing what awaits them as they fall. Around them are 22 flames, representing the 12 signs of the zodiac and 10 points of the Tree of Life, suggesting that even in times of disaster, there is always divine intervention.
    '''
    if name.lower() == 'the tower':
        # Description
        description = tower_desc
        # Reverse Meaning
        mean_down = 'Personal transformation, fear of change, averting disaster'

    # The World: Description
    world_desc = '''
The World card shows a naked woman wrapped in a purple cloth, dancing inside a large laurel wreath. She looks behind her to the past, while her body moves forward to the future. In her hands are two wands or batons, like the one The Magician holds. It is a symbol that what was manifested with The Magician has now come to completion with The World. The wreath is circular, symbolizing a continual cycle of successful completion and new beginnings because, as the woman steps through the wreath, she is completing one phase but beginning another one almost straight away.

Around the wreath are four figures (a lion, bull, cherub and eagle), similar to those in the Wheel of Fortune. Both The World and the Wheel of Fortune speak to the cyclical nature of your life and your progression through its cycles. The four figures represent the four fixed signs of the Zodiac—Leo, Taurus, Aquarius, and Scorpio. They are symbolic of the four elements, the four suits of Tarot, four compass points, four seasons, and the four corners of the Universe. They are here to guide you from one phase to the next, bringing balance and harmony to your journey.
    '''
    if name.lower() == 'the world':
        description = world_desc

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
            await message.add_reaction(aquarius_emoji)
            await asyncio.sleep(2)
            await message.channel.send(aq_horo)

        elif message.content.startswith('$pisces'):
            pi_horo = get_horoscope_pisces()
            await message.add_reaction(pisces_emoji)
            await asyncio.sleep(2)
            await message.channel.send(pi_horo)

        elif message.content.startswith('$aries'):
            ar_horo = get_horoscope_aries()
            await message.add_reaction(aries_emoji)
            await asyncio.sleep(2)
            await message.channel.send(ar_horo)

        elif message.content.startswith('$taurus'):
            taur_horo = get_horoscope_taurus()
            await message.add_reaction(taurus_emoji)
            await asyncio.sleep(2)
            await message.channel.send(taur_horo)

        elif message.content.startswith('$gemini'):
            gem_horo = get_horoscope_gemini()
            await message.add_reaction(gemini_emoji)
            await asyncio.sleep(2)
            await message.channel.send(gem_horo)

        elif message.content.startswith('$cancer'):
            can_horo = get_horoscope_cancer()
            await message.add_reaction(cancer_emoji)
            await asyncio.sleep(2)
            await message.channel.send(can_horo)

        elif message.content.startswith('$leo'):
            leo_horo = get_horoscope_leo()
            await message.add_reaction(leo_emoji)
            await asyncio.sleep(2)
            await message.channel.send(leo_horo)

        elif message.content.startswith('$virgo'):
            vir_horo = get_horoscope_virgo()
            await message.add_reaction(virgo_emoji)
            await asyncio.sleep(2)
            await message.channel.send(vir_horo)

        elif message.content.startswith('$libra'):
            lib_horo = get_horoscope_libra()
            await message.add_reaction(libra_emoji)
            await asyncio.sleep(2)
            await message.channel.send(lib_horo)

        elif message.content.startswith('$scorpio'):
            scor_horo = get_horoscope_scorpio()
            await message.add_reaction(scorpio_emoji)
            await asyncio.sleep(2)
            await message.channel.send(scor_horo)

        elif message.content.startswith('$sagittarius'):
            sag_horo = get_horoscope_sagittarius()
            await message.add_reaction(sagittarius_emoji)
            await asyncio.sleep(2)
            await message.channel.send(sag_horo)

        elif message.content.startswith('$capricorn'):
            cap_horo = get_horoscope_capricorn()
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
