'''Zian Kang, Homework 9: Classes'''

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        

    def get_rank(self):
        return self.rank


    def get_suit(self):
        return self.suit

    def bj_value(self):
        if self.rank <= 10:
            return self.rank
        else:
            return 10

    def __repr__(self):
        number=["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        if self.suit=="s":
            return f"{number[self.rank-1]} of Spades"
        if self.suit=="d":
            return f"{number[self.rank-1]} of Diamonds"
        if self.suit=="c":
            return f"{number[self.rank-1]} of Clubs"
        if self.suit=="h":
            return f"{number[self.rank-1]} of Hearts"