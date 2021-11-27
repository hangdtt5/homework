from card import Card

class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, id, name):  # dễ
        self._id = id
        self._name = name
        self.cards = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        points = 0
        for card in self.cards:
            points+=card.rank
        point = points%10
        if point == 0:
            point = 10
        return point

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        biggest = self.cards[0]
        for card in self.cards:
            if card > biggest:
                biggest = card
        return biggest

    def add_card(self, card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.cards.append(card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards = []

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        cards = ''
        for card in self.cards:
            cards += str(card) +' '
        print(f'{self._name}\t{cards}\tDiem:{self.point}\tla lon nhat:{self.biggest_card}')
