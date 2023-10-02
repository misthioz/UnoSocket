class Card:
    def __init__(self, color="black", number=0, power=None): 
        self.color = color
        self.number = number
        self.power = power

    def __str__(self):
        return f"{self.number} {self.power}"
    
    def __repr__(self):

        return f"{self.number} {self.color} {self.power}"
    
    