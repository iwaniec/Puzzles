import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

import random
import time

cards = ['$500', '$500',
        '$1000', '$1000',
        '$1500', '$1500',
        '$2000', '$2000',
        'Curtain 1', 'Curtain 1',
        'Curtain 3', 'Curtain 3',
        'Box', 'Box',
        'Envelope', 'Envelope',
        'ZONK', 'ZONK', 'ZONK', 'ZONK', 'ZONK', 'ZONK', 'ZONK', 'ZONK']

ids = ['r1c1', 'r1c2','r1c3','r1c4','r1c5','r1c6',
        'r2c1', 'r2c2','r2c3','r2c4','r2c5','r2c6',
        'r3c1', 'r3c2','r3c3','r3c4','r3c5','r3c6',
        'r4c1', 'r4c2','r4c3','r4c4','r4c5','r4c6']



class MainDisplay(BoxLayout):
    def shuffle(self):
        random.shuffle(cards)
        self.ids['reveal_btn'].state = 'down'
        self.ids['reveal_btn'].text = 'Hide'

        card = 0
        for id in ids:
            if cards[card] == 'ZONK':
                self.ids[id].color = (1, 1, 0, 1)
            else:
                self.ids[id].color = (1, 1, 1, 1)
            self.ids[id].font_size = 30
            self.ids[id].text = cards[card]
            card +=1
            self.ids[id].state = 'normal'

    def reveal_all(self):
        # Reveal the cards
        if self.ids['reveal_btn'].state == 'down':
            self.ids['reveal_btn'].text = 'Hide'

            for i in range(1, 25):
                self.single_reveal(i)
        # Hide the cards
        else:
            self.ids['reveal_btn'].text = 'Reveal'

            n = 1
            for id in ids:
                self.ids[id].state = 'normal'
                self.ids[id].text = str(n)
                self.ids[id].color = (1, 1, 1, 1)
                self.ids[id].font_size = 40
                n += 1

    def single_reveal(self, text):
        try:
            index = int(text)-1
            flip = [5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7, 6, 17, 16, 15, 14, 13, 12, 23, 22, 21, 20, 19, 18]
            self.ids[ids[index]].text = cards[flip[index]]
            if cards[flip[index]] == 'ZONK':
                self.ids[ids[index]].color = (1, 1, 0, 1)
            else:
                self.ids[ids[index]].color = (1, 1, 1, 1)
                self.ids[ids[index]].font_size = 30
        except:
            pass

class StrikeApp(App):
    def build(self):
        return MainDisplay()

StrikeApp().run()
