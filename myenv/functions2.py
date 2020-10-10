
# handクラスの作成
class Hand():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

# 両者の出した手を表示する
def show_hands(player1, player2):
    
    # player1の名前と出した手を表示
    hand1 = ""
    # player1の出した手を代入する
    if player1.hand == 0:
        hand1 = "グー"
    elif player1.hand == 1:
        hand1 = "チョキ"
    elif player1.hand == 2:
        hand1 = "パー"
    # 結果を表示
    resulta = f"{player1.name:s}は{hand1:s}を出しました"

    # player2の名前と出した手を表示
    hand2 = ""
    # player2の出した手を代入する
    if player2.hand == 0:
        hand2 = "グー"
    elif player2.hand == 1:
        hand2 = "チョキ"
    elif player2.hand == 2:
        hand2 = "パー"
    # 結果を表示  
    resultb = f"{player2.name:s}は{hand2:s}を出しました"

    return resulta + resultb
    

# プレイヤーとマシンの出した手を比較
def referee(player1, player2):

    result = ""
    # 条件分岐
    # 引き分け
    if player1.hand == player2.hand:
        result = "引き分け"
            
    # player1がグーを出した場合
    elif player1.hand == 0:
        # player2がチョキを出した場合
        if player2.hand == 1:
            result = f"{player1.name:s}の勝ちです"
        # player2がパーを出した場合
        else:
            result = f"{player2.name:s}の勝ちです"

    # player1がチョキを出した場合
    elif player1.hand == 1:
        # player2がパーを出した場合
        if player2.hand == 2:
            result = f"{player1.name:s}の勝ちです"
        # player2がグーを出した場合
        else:
            result = f"{player2.name:s}の勝ちです"

    # player1がパーを出した場合
    elif player1.hand == 2:
        # player2がグーを出した場合
        if player2.hand == 0:
            result = f"{player1.name:s}の勝ちです"
        # player2がチョキを出した場合
        else:
            result = f"{player2.name:s}の勝ちです"

    return result
