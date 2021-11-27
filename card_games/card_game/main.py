from deck import Deck
from game import Game

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game()
    game.setup()
    # game.guide()
    while True:
            print(f"""
                    1.Danh sach nguoi choi
                    2.Them nguoi choi
                    3.Xoa nguoi choi
                    4.Chia bai
                    5.Lat bai
                    6.Xem lai game
                    7.Lich su choi
                    8.Thoat""")
            print("Mời chọn chức năng: ")
            f = input('Nhap:')
            if f == '1':
                game.list_players()
            elif f == '2':
                game.add_player()
            elif f == '3':
                game.remove_player()
            elif f == '4':
                game.deal_card()
            elif f == '5':
                game.flip_card()
            elif f == '6':
                game.last_game()
            elif f == '7':
                game.game_history()
            else:
                return

if __name__ == '__main__':
    main()
