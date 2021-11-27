'''Kết nối CSDL'''
from pymysql import connect, cursors,Error
import card 
import player 
import game 
from datetime import datetime

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "game",
    "cursorclass": cursors.DictCursor
}


def log(players, winner):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''

    play_at = datetime.now()
    # To connect MySQL database
    conn = connect(
        host='127.0.0.1',
        user='root', 
        password = "",
        db='game',
        cursorclass=cursors.DictCursor
    )
    
    with conn:
        last_id = -1
        with conn.cursor() as cur:
            sql = ''' 
                INSERT INTO games (play_at, winner)
                VALUES (%s, %s)
                '''
            cur.execute(sql, (play_at, winner))
            last_id = cur.lastrowid

        if last_id != -1:
            for player in players:
                with conn.cursor() as cur:
                    sql = ''' 
                        INSERT INTO logs (play_at, games_winer_id, name, card1, card2, card3, point, biggest_card)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        '''
                    cur.execute(sql, (play_at, last_id, player._name, str(player.cards[0]), str(player.cards[1]), str(player.cards[2]), player.point, str(player.biggest_card)))
                
        conn.commit()

def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    conn = connect(
        host='127.0.0.1',
        user='root', 
        password = "",
        db='game',
        cursorclass=cursors.DictCursor
    )
    with conn:
        last_id = -1
        with conn.cursor() as cur:
            sql = 'SELECT * FROM `games` WHERE id=(SELECT MAX(id) FROM `games`)'
            cur.execute(sql)
            result = cur.fetchone()
            if result != None:
                print ("latest game result")
                last_id = result['id']
                print("Play at: {}, name of winder: {}".format(result['play_at'], result['winner']))
        if last_id != -1:
            with conn.cursor() as cur:
                sql = 'SELECT * FROM `logs` WHERE games_winer_id = %s'
                cur.execute(sql, (last_id))
                for row in cur:
                    print ("\tPlayer: {}\n\t\t point: {}, biggest card: {}, card list: ({}, {}, {})".format(row['name'], row['point'], row['biggest_card'], row['card1'], row['card2'], row['card3']))
    pass


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    print ("game statistics !!!!! ")

    conn = connect(
         host='127.0.0.1',
        user='root', 
        password = "",
        db='game',
        cursorclass=cursors.DictCursor
    )

    with conn:
        with conn.cursor() as cur:
            sql = 'SELECT COUNT(*) as total FROM games '
            cur.execute(sql)
            result = cur.fetchone()
            print ("Number of Boards: {}".format(result['total']))

        with conn.cursor() as cur:
            sql = 'SELECT winner, COUNT(*) as win_count FROM games GROUP BY winner ORDER BY win_count desc limit 10'
            cur.execute(sql)
            print ("Top 10 Players:")
            for row in cur:
                print ("\tName: {} \t\tnumber of win: {}".format(row['winner'], row['win_count']))

