from termcolor import colored

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def print_cards(self):
        for card in self.cards:
            print(colored(card.get_card_text(), card.color))


    def prompt_card(self):
        card = input("Type the card you want to play (format: number/name - color): ")
        while not self.check_card(card):
            print("Card not found!")
            card = input("Type the card you want to play (format: number/name - color): ")
        
        self.remove_card(card)
        return card
        

    def check_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                return True
        return False


    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                break
        