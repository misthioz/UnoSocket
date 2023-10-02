from card import Card

def create_all_cards():
    deck = []
    for _ in range(4):
        for color in ["red", "green", "blue", "yellow"]:
            for number in range (0,10):
                deck.append(Card(color, number, None))
            
            for power in ["+2","reverse","skip"]:
                deck.append(Card(color, power=power))

    deck.append(Card(power="+4"))
    deck.append(Card(power="+4"))
    deck.append(Card(power="everything"))
    deck.append(Card(power="everything"))

    return deck