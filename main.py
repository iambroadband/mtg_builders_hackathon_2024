from scooze.card import Card
from scooze.deck import Deck
import re
from bs4 import BeautifulSoup
import requests

# function to extract html document from given url
def getHTMLdocument(url):

    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


def main():
    url = input("Enter a Goldfish URL: ")
    deck_id = re.findall("\d{5,10}", url)
    deck_id = deck_id[0] if len(deck_id) > 0 else "ERR"
    print(f"Deck ID is {deck_id}")
    goldfish_target_url = f"https://www.mtggoldfish.com/deck/arena_download/{deck_id}"
    html = getHTMLdocument(goldfish_target_url)
    soup = BeautifulSoup(html, 'html.parser')

    copy_paste_box_text = soup.find('textarea', {'class': 'copy-paste-box'}).text.strip()
    print(copy_paste_box_text)

    # for each line that starts with a number, create a card with that name, then add it to a deck


if __name__ == "__main__":
    main()
