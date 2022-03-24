'''
Get Happy Bot allows users to
- Submit Words of Encouragement
- Request Words of Encouragement
- Request an Insipirational Quote

Structure
1. Import Dependancies & Load .env
2. Connections
    - Discord
    - SQLite
3. Variables
4. Functions
5. Callbacks
'''

# 1. Imports
import os, asyncio, discord
import requests, json, sqlite3
import random, datetime
from dotenv import load_dotenv

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 2. Connections

# load env file
load_dotenv()

# Discord
TOKEN = os.getenv('GET_HAPPY_TOKEN')
client = discord.Client()
embed = discord.Embed()

# SQLite
conn = sqlite3.connect('encouragement.sqlite3')

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 3. Variables

line_break = '''

✧.*◌·͡˔·ོ◌ *·✧✧.*◌·͡˔·ོ◌ *·✧✧.*◌·͡˔·ོ◌ *·✧

'''

# Jokes
# Source https://jokes.one/api/joke/#python
# Thank you jokes.one for free daily jokes!
jod_url = 'https://api.jokes.one/jod'
knock_url = f'{jod_url}?category=knock-knock'
animal_url = f'{jod_url}?category=animal'
jod_instantiate = 'Your Daily Jokes of the Day will be sent every 24 hours from activation.'
jod_credit = 'Your Joke is Brought to You By: joke.one'

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 4. Functions

# SQLite

def execute_query(connection, query):
    'Executes SQLite Queries'

    curs = connection.cursor()
    curs.execute(query)
    connection.commit()

    return 'Query Executed and Commited'

def execute_query2(connection, query):
    '''
    This function creates a cursor, executes a query, and returns the results
    '''

    curs = connection.cursor()
    curs.execute(query)
    result = curs.fetchall()
    return result

# Quotes
def get_inspired():
    'Retrieves an Inspirational Quote'

    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def get_affirmation():
    'Retrieves an Affirmation'

    response = requests.get("https://www.affirmations.dev/")
    json_data = json.loads(response.text)
    quote = json_data['affirmation']
    return quote


# Pictures
# Dogs and Corgis are from https://dog.ceo/ Thank you!
# Give these goodest of bois some treatos https://www.paypal.com/paypalme/dogapi
def get_dogs():
    'Retrieves a Picture of Dog'

    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    dog = json_data['message']
    return dog


def get_corgi():
    'Retrieves Pictures of Corgis'

    response = requests.get("https://dog.ceo/api/breed/pembroke/images/random")
    json_data = json.loads(response.text)
    corgi = json_data['message']
    return corgi

# Because everday is Caturday we can thank the Cat API for these.
def get_kittykittykitty():
    'Retrieves Pictures of Cool Cats and Kittens'

    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(response.text)
    meow = json_data[0]['url']
    return meow


def get_keanu():
    'Retrieves a Random Picture of Keanu'

    # Main URL
    url = 'https://placekeanu.com'
    # Options for Young, Greyscale, or Young & Greyscale Keanu
    options = ['y', 'g', 'yg']
    # URL with Random Int for Size to Increase Randomness, and Options Above
    random_url = f'{url}/{random.randint(250, 501)}/{random.choice(options)}'

    return random_url


# Jokes
def get_jods():
    'Retrieves the jokes of the day from jokes.one REST API (Thank you!)'

    # Joke of the Day
    jod_response = requests.get(jod_url)
    jod_data = jod_response.json()['contents']['jokes'][0]
    jod = jod_data['joke']['text']

    # Knock Knock Joke of the Day
    knock_response = requests.get(knock_url)
    knock_data = knock_response.json()['contents']['jokes'][0]
    knock_knock = knock_data['joke']['text']

    # Animal Joke of the Day

    animal_response = requests.get(animal_url)
    animal_data = animal_response.json()['contents']['jokes'][0]
    animal_jod = animal_data['joke']['text']

    return jod, knock_knock, animal_jod


# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 5. Callbacks
@client.event
async def on_ready():

    # Create SQLite Table, IF Non-Existant
    create_encourage_table = '''
    CREATE TABLE IF NOT EXISTS encourage (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "guild_id" TEXT NOT NULL,
        "message" TEXT NOT NULL
        );
    '''
    execute_query(conn, create_encourage_table)
    print(f'{client.user} has connected to Discord')


# Message Replies
@client.event
async def on_message(message):
        # Checks Author is not bot
        if message.author == client.user:
            return

        # Inspiration
        # Returns an Inspirational Quote
        if message.content.startswith('$inspire'):
            insp_quote = get_inspired()
            await message.channel.send(insp_quote)

        # Encouragement
        # Returns a Random Encouraging Message from User Submissions
        if message.content.startswith('$encouragement'):

            # Get Guild ID
            guild_id = message.guild.id

            # Query
            encouragement_query = f'''
            SELECT *
            FROM encourage
            WHERE guild_id is "1701-D" or {guild_id}
            '''
            encouragements = execute_query2(conn, encouragement_query)

            # Select Random
            random_encouragement = random.choice(encouragements)
            encouragement_msg = random_encouragement[2]

            await message.channel.send(encouragement_msg)

        # Add User Submissions to Encouraging Messages
        if message.channel.name == 'submit-encouragements':
            if message.content.startswith('$new_encouragement'):

                await message.channel.send("Your ecouraging message is being added.")

                # Get Guild ID
                guild_id = message.guild.id

                # Get Message Content
                message_content = message.content
                encourage_split = message_content.split('$new_encouragement')
                encourage_msg = encourage_split[1].lstrip()

                # Query
                insert_enc_msg_query = f'''
                INSERT INTO encourage ("guild_id", "message")
                VALUES ("{guild_id}", "{encourage_msg}");
                '''
                execute_query(conn, insert_enc_msg_query)

                await asyncio.sleep(3)
                await message.channel.send("Your encouraging message has been added.")

        # # Delete User Submissions to Encouraging Messages
        # if message.content.startswith('$del_encouragement'):
        #     encouragements = []
        #     if "encouragements" in db.
        #         index = int(msg.split('$del_encouragement', 1)[1])
        #         delete_encouragement(index)
        #         encouragements = db["encouragements"]
        #     await message.channel.send(encouragements)


        if message.content.startswith('$affirmation'):
            aff_quote = get_affirmation()
            await message.channel.send(aff_quote)

        if message.channel.name == 'pawsitive':
            # pictures
            if message.content.startswith('$dog'):
                dog = get_dogs()
                await message.channel.send(dog)

            if message.content.startswith('$corgi'):
                corgi = get_corgi()
                await message.channel.send(corgi)

            if message.content.startswith('$cat'):
                cat = get_kittykittykitty()
                await message.channel.send(cat)

            if message.content.startswith('$keanu'):
                keanu_url = get_keanu()
                await message.channel.send(keanu_url)

        # Jokes from jokes.io
        if message.channel.name == 'jokes-of-the-day':

            # Trigger Command
            if message.content.startswith('$joke'):

                # One time opening message
                await message.channel.send(jod_instantiate)

                # Infiinite Loop
                while 1 == True:

                    # Pull Jokes of the Day
                    jod, knock_knock, animal_jod = get_jods()

                    # Credit
                    await message.channel.send(line_break)
                    await message.channel.send(jod_credit)
                    await message.channel.send(line_break)
                    await asyncio.sleep(5)
                    # Joke of the Day
                    await message.channel.send(jod)
                    await message.channel.send(line_break)
                    await asyncio.sleep(5)

                    # Knock Knock Joke of the Day
                    await message.channel.send(knock_knock)
                    await message.channel.send(line_break)
                    await asyncio.sleep(5)

                    # Animal Joke of the Day
                    await message.channel.send(animal_jod)
                    await message.channel.send(line_break)

                    # Wait 24 Hours
                    await asyncio.sleep(86400)




# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

client.run(TOKEN)
