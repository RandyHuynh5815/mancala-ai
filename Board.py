from Player import Player

class Board:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.p1_turn = True

    def turn(self, choice):
        player = self.p1 if self.p1_turn else self.p2
        opponent = self.p2 if self.p1_turn else self.p1
        pebbles = player.gather(choice)
        go_again = False
        while pebbles > 0:
            pebbles, go_again = player.drop(pebbles, start=choice+1)
            pebbles, _ = opponent.drop(pebbles, isPlayer=False)
        self.p1_turn = self.p1_turn if go_again else not self.p1_turn

    def print_board(self):
        print(f"P1 Score: {self.p1.score}\nP2 Score: {self.p2.score}\n")
        print(" 5, 4, 3, 2, 1, 0")
        print([self.p2.board[i] for i in range(len(self.p2.board)-1,-1,-1)])
        print(self.p1.board)
        print(" 0, 1, 2, 3, 4, 5")
        print()