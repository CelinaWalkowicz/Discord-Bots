# Various Discord Bots
* [Get-Happy](https://github.com/CelinaWalkowicz/Discord-Bots/blob/main/README.md#get-happy)
* [Occult](https://github.com/CelinaWalkowicz/Discord-Bots/blob/main/README.md#occult)

---

## **Get-Happy**
### • Description 
> This bot monitors a Discord Guild's (Server) messages, and returns positive messages and images.
> Additionally, each Guild will have their private database of encouraging messages along with a dozen
> prepacked messages that can be returned to offer words of encouragement to their fellow members.
> Guild Administrators will need to: 
>   - select which channels this bot has access to view, and reply. 
>   - create a channel named "submit-encouragements" 

### • Requirements
  - asyncio, discord, dotenv, json, os, random, requests, sqlite3

### • Commands

#### Quotes:
  - `$inspire` returns messages of inspiration
  - `$affirmation` returns affiramations
  - `$encouragement` returns words of encouragement from fellow Guild Members
  - `$new_encouragement` adds words of encouragement to the database.*

###### *Without this channel users will not be able to add new words of encouragement.

#### Jokes of the Day
Sourced from [jokes.io](https://jokes.one/api/joke/#python)
  - `$joke` returns the joke of the day
  - `$knock` returns the knock knock joke of the day
  - `$animal` returns the animal joke of the day

#### Images:
  - `$dog` returns a random image of a dog. 
    -  Source: [The Dog API (dog.ceo)](https://dog.ceo)
  - `$corgi` returns a random image of a corgi. 
    - Source: [The Dog API (dog.ceo)](https://dog.ceo)
  - `$cat` returns a random image of a cat.
    - Source: [The Cat API](https://thecatapi.com/)

---

## Occult
### • Description 
> This bot monitors a specific channels in a Discord Guild (Server), and allows members to retrieve their daily
> horoscope, and pull one or three tarot cards. Moonphase announcements are under works, and will be coming soon!
> Guild Administrators will need to create the following channels
>   - "horoscope"
>   - "tarot"
>   - "moon-phases"....coming soon!

### • Requirements
  - asyncio, discord, dotenv, geopy's Nominatim, json, os, random, requests, sqlite3

### • Commands
- In the horoscope channel: `$[Your Zodiac Sign Here]`....for example `$gemini`
  - This bot will react to the command with the specified zodiac's emoji, and return its daily horoscope. 
  - [The Unifficial Astrology.com API](https://ohmanda.com/api/horoscope/)
- In the tarot channel: `$draw1` and `$draw3` for one and three card tarot draws, respectively.
  - Source: [Tarot API](https://github.com/ekelen/tarot-api)

---

# Get the Bots!
- Coming Soon...
