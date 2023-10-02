class Card:
    def __init__(self, color="white", number=0, power=None): 
        self.color = color
        self.number = number
        self.power = power

    def __str__(self):
        return f"{self.get_card_text()} - {self.color}"

    def __repr__(self):
        return f"{self.get_card_text()} - {self.color}"
    
    def get_card_text(self):
        if self.number == 0:
            return self.power
        else:
            return self.number