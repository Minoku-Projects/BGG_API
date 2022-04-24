import requests
import xml.etree.ElementTree as EleTree
from datetime import datetime


BG_PAGES = "https://boardgamegeek.com/sitemap_geekitems_boardgame_page_"




def mytime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    #return now.strftime("%H%M%S%f")

class robo_data():

    # list of all single boardgames
    bg_sites = []
    bg_ids = []

    def __init__(self):
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
                self.bg_sites.append(x[0].text)

                #we only want ids and append to our attribute
                self.__split_url_into_id(x[0].text)

    def get_list_sites(self):
        return self.bg_sites

    def get_id_list(self):
        return self.bg_ids

    def __split_url_into_id(self, url):
        #['https:', '', 'boardgamegeek.com', 'boardgame', '21776', 'jot']
        #only append ids from url
        self.bg_ids.append(url.split("/")[4])



if __name__ == '__main__':

        robo = robo_data()
        print(len(robo.bg_sites))
        print(len(robo.bg_ids))


