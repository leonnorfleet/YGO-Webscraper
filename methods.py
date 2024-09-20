import requests
import sys
from bs4 import BeautifulSoup

productsLink = 'https://www.db.yugioh-card.com/yugiohdb/card_list.action'
banlistLink = 'https://www.db.yugioh-card.com/yugiohdb/forbidden_limited.action#list_forbidden'

def breakline():
    print('-----------------------------------------------------')

def scrapeCardList(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    setName = soup.find(id='broad_title').find('strong')
    print('Set:', setName.text)
    breakline()

    allCards = soup.find(id='card_list').find_all('span', {'class':'card_name'})
    monsters = list()
    spells = list()
    traps = list()

    #Filter cards into the 3 types (Monster, Spell, Trap)

    for card in allCards:
        cardName = card.text
        cardType = card.find_parent('div').find('span', {'class':'box_card_attribute'}).find('span').text
        if cardType == 'SPELL':
            spells.append(cardName)
        elif cardType == 'TRAP':
            traps.append(cardName)
        else:
            monsters.append(cardName)

        monsters.sort()
        spells.sort()
        traps.sort()

    print('Monster Cards:', len(monsters))
    breakline()
    for card in monsters:
        print(card)


    breakline()
    print('Spell Cards:', len(spells))
    breakline()
    for card in spells:
        print(card)

    breakline()
    print('Trap Cards:', len(traps))
    breakline()
    for card in traps:
        print(card)

    total = len(monsters) + len(spells) + len(traps)
    
    breakline()
    print('Cards in set:', total)
    breakline()
        

def scrapeBoosterPacks(url, title):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    productList = soup.find(class_='card_list')

    # Try to find the pack with the supplied title

    try:
        cardPackLink = productList.find('strong', string=title.upper()).find_parent('div').find('input', {'class':'link_value'})
        scrapeCardList('https://www.db.yugioh-card.com' + cardPackLink['value'])
    except:
        print('An error has occured. Try again or verify the product name.')
        sys.exit

def scrapeBanList(url, myCard):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    forbiddenList = soup.find('div', {'id':'list_forbidden'}).find_all('span', {'class':'name'})
    limitedList = soup.find('div', {'id':'list_limited'}).find_all('span', {'class':'name'})
    semiLimitedList = soup.find('div', {'id':'list_semi_limited'}).find_all('span', {'class':'name'})

    breakline()

    if myCard.lower() in [card.text.lower() for card in forbiddenList]:
        print('Status: Forbidden')

    elif myCard.lower() in [card.text.lower() for card in limitedList]:
        print('Status: Limited')

    elif myCard.lower() in [card.text.lower() for card in semiLimitedList]:
        print('Status: Semi-Limited')

    else:
        print('Status: Not on Banlist')

    breakline()
