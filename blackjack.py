import numpy as np

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.deck = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
        ]
        np.random.shuffle(self.deck)
    
    def deal(self, cards: int = 1):
        return [self.deck.pop() for card in range(0, cards)]
   
class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = list()

    def getName(self) -> str: return self.name

    def drawCards(self, cards):
        self.cards.extend(cards)

    def getValue(self, index: int = -1):
        if index == -1:
            return sum(self.cards)
        else: return self.cards[index]
    
    def __str__(self) -> str:
        return f"{self.name} har summan: {self.getValue()} med korten: [{", ".join(str(v) for v in self.cards)}]"
    
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.restart()

    def restart(self):
        self.deck.shuffle()
        self.player = Player('Du')
        self.player.drawCards(self.deck.deal(2))
        self.computer = Player('Dator')
        self.computer.drawCards(self.deck.deal(2))

    def play(self) -> bool:
        print(self.player)
        print(f"{self.computer.getName()} har summan: {self.computer.getValue(0)}")
        
        while 'j' == input("Vill du ta ett kort till? (j/N)"):
            self.player.drawCards(self.deck.deal())
            print(self.player)

            if self.player.getValue() > 21:
                print("Du förlorade!")
                return False

        print(self.computer)
        while (self.computer.getValue() < 17):
            self.computer.drawCards(self.deck.deal())
            print(self.computer)

        if self.computer.getValue() > 21:
            print("Du vann!")
        elif self.computer.getValue() > self.player.getValue():
            print("Datorn vann!")
        elif self.player.getValue() > self.computer.getValue():
            print("Du vann!")
        elif self.player.getValue() == self.computer.getValue():
            print("Det blev oavgjort!")
        return True

def main():
    Blackjack().play()
main()

