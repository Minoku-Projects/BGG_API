import requests
import xml.etree.ElementTree as EleTree
from datetime import datetime

BG_PAGES = "https://boardgamegeek.com/sitemap_geekitems_boardgame_page_"


def mytime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    # return now.strftime("%H%M%S%f")


class RoboData:
    # list of all single boardgames
    bg_sites = []
    bg_ids = []

    def __init__(self):
        # Max. 15 pages
        for count, i in enumerate(range(15)):
            # build string for page
            page = BG_PAGES + str(count)
            print(page)
            bgg = requests.get(page)
            if bgg.status_code == 200:
                parsed_xml = EleTree.fromstring(bgg.text)

                # every url gets extraxted
                for x in parsed_xml:
                    # x[0].text = https://boardgamegeek.com/boardgame/21776/jot
                    self.bg_sites.append(x[0].text)

                    # we only want ids and append to our attribute
                    self.__split_url_into_id(x[0].text)
            else:
                print("ERROR: " + str(bgg.status_code) + "Page" + page)

    def get_list_sites(self):
        return self.bg_sites

    def get_id_list(self):
        return self.bg_ids

    def __split_url_into_id(self, url):
        # ['https:', '', 'boardgamegeek.com', 'boardgame', '21776', 'jot']
        # only append ids from url
        self.bg_ids.append(url.split("/")[4])


if __name__ == '__main__':
    robo = RoboData()
    print(len(robo.bg_sites))
    print(len(robo.bg_ids))
