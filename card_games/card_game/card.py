class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9]
    suits = ['♠', '♣', '♦', '♥']

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        '''Hiển thị lá bài'''
        r = self.rank
        if(self.rank  == 10):
            r = 'A'
        s = self.suit
        if (s == 0) :
            s = '♠'
        if (s == 1) :
            s = '♣'
        if (s == 2) :
            s = '♦'
        if (s == 3) :
            s = '♥'
        return f'{r}{s}'

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 > t2