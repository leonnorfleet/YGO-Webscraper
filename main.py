import argparse
from methods import productsLink, banlistLink, scrapeBoosterPacks, scrapeBanList

def main():

    parser = argparse.ArgumentParser(
        prog='PROG',
        description='Inspect the card contents of Booster Packs, Tins, etc. and check a card\'s current banlist status',
        usage='%(prog)s [options] [PRODUCTNAME/CARDNAME]',
        epilog='Made by Le\'on Norfleet',
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-cl', '--cardlist', action='store', nargs='+', help='argument to inspect the card list of a YGO product', metavar='PRODUCTNAME')
    group.add_argument('-bl', '--banlist', action='store', nargs='+', help='argument to check the banlist status of a YGO card', metavar='CARDNAME')

    args = parser.parse_args()

    if args.cardlist:
        packName = ' '.join(args.cardlist)
        scrapeBoosterPacks(productsLink, packName)
    elif args.banlist:
        cardName = ' '.join(args.banlist)
        scrapeBanList(banlistLink, cardName)


if __name__ == '__main__':
    main()
    