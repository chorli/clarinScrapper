from bs4 import BeautifulSoup
import requests
import pandas as pd
from utils.clarinParser import parseText
from utils.clearScreen import screen_clear
from dbLayer.connection import create_connection, checkIfNoticeHasBeenImported, insertNewNotice
import constants.constants as constants

url = constants.CONST_SITE_URL

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all('p', {"class":"volanta"})

list_titles = list()

count=0
for i in titles:
    if count < constants.CONST_NUMBER_OF_NOTICES_TO_SCRAP:
        if i.parent.text.startswith("\n"):
            list_titles.append(i.parent.text)
        else:
            list_titles.append(i.parent.parent.text)
    else:
        break
    count += 1

screen_clear()

conn = create_connection(constants.CONST_SITE_DB_FILE)

for title in list_titles:
    entity = parseText(title, "\n")
    noticeHasBeenImported = checkIfNoticeHasBeenImported(constants.CONST_CLARIN_DB_ID, entity, conn)
    if not noticeHasBeenImported:
        insertNewNotice(entity, conn)

print("Process finished...")


