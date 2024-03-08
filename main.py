from scraptrawler.extractor import get_deck_from_url


def main():
    url = input("Enter a decklist URL: ")
    deck = get_deck_from_url(url)
    print(deck.export())


if __name__ == "__main__":
    main()
