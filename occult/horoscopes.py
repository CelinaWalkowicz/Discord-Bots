'''
Horoscope Attributes of the Occult Bot
'''

# Imports
import requests, json

# Variables

# Emojis
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


# Functions

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


def horo_date(json_data):
    'Converts YYYY-MM-DD date to MonthName DD, YYYY'

    # Separate Parts of the Date
    year = json_data['date'][:4]
    month_num = json_data['date'][5:7]
    day = json_data['date'][8:]

    month = month_num_to_name(month_num)

    return f'{month} {day}, {year}'


def get_horoscope(zodiac):
    'Retrieves Daily Horoscopes for Specified Zodiac'

    # Aquarius
    if zodiac == 'aquarius':
        response = requests.get("https://ohmanda.com/api/horoscope/aquarius")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{aquarius_emoji} {json_data['sign'].upper()} {aquarius_emoji}

{date}
{json_data['horoscope']}
        '''

    # Pisces
    elif zodiac == 'pisces':
        response = requests.get("https://ohmanda.com/api/horoscope/pisces")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{pisces_emoji} {json_data['sign'].upper()} {pisces_emoji}

{date}
{json_data['horoscope']}
        '''

    # Aries
    elif zodiac == 'aries':
        response = requests.get("https://ohmanda.com/api/horoscope/aries")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{aries_emoji} {json_data['sign'].upper()} {aries_emoji}

{date}
{json_data['horoscope']}
        '''

    # Taurus
    elif zodiac == 'taurus':
        response = requests.get("https://ohmanda.com/api/horoscope/taurus")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{taurus_emoji} {json_data['sign'].upper()} {taurus_emoji}

{date}
{json_data['horoscope']}
    '''

    # Gemini
    elif zodiac == 'gemini':
        response = requests.get("https://ohmanda.com/api/horoscope/gemini")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{gemini_emoji} {json_data['sign'].upper()} {gemini_emoji}

{date}
{json_data['horoscope']}
        '''

    # Cancer
    elif zodiac == 'cancer':
        response = requests.get("https://ohmanda.com/api/horoscope/cancer")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{cancer_emoji} {json_data['sign'].upper()} {cancer_emoji}


{date}
{json_data['horoscope']}
        '''

    # Leo
    elif zodiac == 'leo':
        response = requests.get("https://ohmanda.com/api/horoscope/leo")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{leo_emoji} {json_data['sign'].upper()} {leo_emoji}

{date}
{json_data['horoscope']}
        '''

    # Virgo
    elif zodiac == 'virgo':
        response = requests.get("https://ohmanda.com/api/horoscope/virgo")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{virgo_emoji} {json_data['sign'].upper()} {virgo_emoji}

{date}
{json_data['horoscope']}
        '''

    # Libra
    elif zodiac == 'libra':
        response = requests.get("https://ohmanda.com/api/horoscope/libra")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{libra_emoji} {json_data['sign'].upper()} {libra_emoji}

{date}
{json_data['horoscope']}
        '''

    # Scorpio
    elif zodiac == 'scorpio':
        response = requests.get("https://ohmanda.com/api/horoscope/scorpio")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{scorpio_emoji} {json_data['sign'].upper()} {scorpio_emoji}

{date}
{json_data['horoscope']}
        '''

    # Sagittarius
    elif zodiac == 'sagittarius':
        response = requests.get("https://ohmanda.com/api/horoscope/sagittarius")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{sagittarius_emoji} {json_data['sign'].upper()} {sagittarius_emoji}

{date}
{json_data['horoscope']}
        '''

    # Capricorn
    elif zodiac == 'capricorn':
        response = requests.get("https://ohmanda.com/api/horoscope/capricorn")
        json_data = json.loads(response.text)
        date = horo_date(json_data)
        horoscope = f'''
{capricorn_emoji} {json_data['sign'].upper()} {capricorn_emoji}

{date}
{json_data['horoscope']}
        '''

    return(horoscope)