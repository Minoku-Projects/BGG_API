import requests
import xml.etree.ElementTree as EleTree
from datetime import datetime


BG_PAGES = "https://boardgamegeek.com/sitemap_geekitems_boardgame_page_"

#list of all single boardgames
BG_SINGLE_SITES = []


def mytime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    #return now.strftime("%H%M%S%f")

def get_single_sites():

    # Max. 15 pages
    for i in range(15):
        #range starts with 0 but site starts with 1, so we have to increase
        number = i + 1
        #build string for page
        page = BG_PAGES + str(number)
        bgg = requests.get(page)
        print(bgg.status_code)
        parsed_xml = EleTree.fromstring(bgg.text)

        #every url gets extraxted
        for x in parsed_xml:
            #x[0].text = https://boardgamegeek.com/boardgame/21776/jot
            BG_SINGLE_SITES.append(x[0].text)


if __name__ == '__main__':

        get_single_sites()
        print(len(BG_SINGLE_SITES))

