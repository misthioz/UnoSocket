from termcolor import colored

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def print_cards(self):
        for card in self.cards:
            print(colored(card.get_card_text(), card.color))


    def prompt_card(self, previous_card):
        card = input("Type the card you want to play (format: number/name - color): ")
        while not self.check_card(card, previous_card):
            print("Card not valid or not found!")
            card = input("Type the card you want to play (format: number/name - color): ")
        
        self.remove_card(card)
        return card
        

    def check_card(self, card: str, previous_card):
        for c in self.cards:
            if previous_card != None:
                if str(c) == card and (previous_card.color == c.color or previous_card.number == c.number):
                    return True
            else:
                if str(c) == card:
                    return True
        return False


    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                break
        