import random
import numpy as np

class Hangman:
    def __init__(self, words, max):
        self.max = max
        self.words = words

    def create(self): 
        self.answer = list(self.words[random.randint(0, len(self.words) -1)])
        self.word = np.repeat("_", len(self.answer))
        self.chars = []
    
    def render(self) -> bool:
        ''' Limit guesses '''
        if len(self.chars) >= self.max:
            print(f"Beklagar! Du har gissat för många gånger")
            return False

        ''' Collect input'''
        char = input(f"[{len(self.chars) +1} / {self.max}] - Ange ett tecken: ")
        
        ''' Sanitize input '''
        if len(char) != 1:
            print("Du kan bara gissa en bokstav åt gången!")
            return True
        
        ''' Check if repeated '''
        if self.chars.count(char)> 0:
            print (f"Du har redan gissat på {char}!")
        self.chars.append(char)

        ''' Check if character exists in answer '''
        arr = np.array(self.answer)
        (found,) = np.where(arr == char)

        ''' Reveal characters in guessed word '''
        arr = np.array(self.word)
        arr.put(found, char)
        self.word = arr

        ''' Print '''
        print("Ord: [ " + "".join(self.word) + " ]", end=" ")

        if len(found) > 0:
            print (f"{char} fanns på {len(found)} ställe(n)")
        else:
            print (f"{char} fanns inte")

        if np.array_equal(self.word, self.answer):
            print(f"{"".join(self.answer)} är rätt gissat!")
            return False

        return True
   
def main():
    game = Hangman([
        "måndag",
        "tisdag",
        "onsdag",
        "torsdag",
        "fredag",
        "lördag",
        "söndag"
    ], 10)

    game.create()

    while 1:
        if not game.render():
            break

main()

