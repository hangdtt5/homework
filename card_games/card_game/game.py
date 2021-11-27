import db
from deck import Deck
from player import Player


class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self._playerList = []
        self.deck = Deck()
        self.winner = None
        self._is_deal = False

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        self._playerList = []
        inputPlayer = input('Nhap so luong nguoi choi:')
        inputPlayer = int(inputPlayer)
        for i in range(1,inputPlayer+1):
            player_name = input(f'Nhap ten nguoi choi {i}:')
            self._playerList.append(Player(i,player_name))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print("1.Danh sách người chơi"+ "(" + str(len(self._playerList)) +")")
        print("2.Thêm người chơi (có thể thêm)")
        print("3.Loại người chơi (Số người chơi tối thiểu rồi)")
        print("4.Chia bài")
        print("5.Lật bài")
        print("6.Xem lại game vừa chơi")
        print("7.Xem lịch sử chơi hôm nay")
        print("8.Công an tới, tốc biến!!!")

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print('ID\tPlayer Name')
        for player in self._playerList:
            print(f'{player._id}\t{player._name}')

    def add_player(self):
        '''Thêm một người chơi mới'''
        idx = len(self._playerList) +1
        name = input(f'Nhap ten nguoi choi thu {idx}:')
        self._playerList.append(Player(idx,name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Nhập ID người chơi muốn xóa: ")
        index_player = int(input())
        del self._playerList[index_player-1]

    def deal_card(self):
        '''Chia bài cho người chơi'''
        self._deck = Deck()
        self._deck.build()
        self._deck.shuffle_card()
        for p in self._playerList:
            p.remove_card()
        
        numberPlayer = len(self._playerList)
        cardNumber = 3
        for i in range(numberPlayer*cardNumber):
            playerIndex = i%numberPlayer
            card = self._deck.deal_card()
            self._playerList[playerIndex].add_card(card)
        print('Da chia xong!')
        self._is_deal = True
        self._is_logged = False

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        if self._is_deal:
            winner = None
            for player in self._playerList:
                player.flip_card()
                if winner == None:
                    winner = player
                else:
                    if winner.point == player.point:
                        if player.biggest_card > winner.biggest_card:
                            winner = player
                    elif player.point > winner.point:
                        winner = player
            print(f'Nguoi chien thang:{winner._name}')
            self._winner = winner._name
            self._is_fliped = True

            ''' Ghi log vào database '''
            if self._is_logged == False:
                self._is_logged = True
                db.log(self._playerList, self._winner)

        else:
            print ("Chua chia bai !!!")

    def last_game(self):
        db.get_last_game()
        pass
    
    def game_history(self):
        db.history()
        pass