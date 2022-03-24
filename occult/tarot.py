'''
Tarot Attributes of the Occult Bot
'''

# 1. Imports
import requests, json
import random

# 2.  Variables

# Tarot Card Data from https://github.com/ekelen
# Thank ekelen for putting this all together!
tarot_json = 'https://raw.githubusercontent.com/CelinaWalkowicz/tarot-api/master/static/card_data.json'


# 2.  Functions

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
