from random import shuffle

from card import Card

class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    def build(self):
        '''Tạo bộ bài'''
        self.cards = []

        for rank in range (10):
            for suit in range (4):
                self.cards.append(Card(suit,rank))

        self.shuffle_card()

    def shuffle_card(self):
        '''Trộn bài'''
        self.shuffled_cards = shuffle(self.cards)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards) == 0:
            return
        return self.cards.pop()

        