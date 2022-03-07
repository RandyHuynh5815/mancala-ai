class Player:
    def __init__(self):
        self.score = 0
        self.board = [4 for i in range(6)]
    
    def gather(self, choice: int) -> None:
        assert 0 <= choice <= 5, "Option chosen out of bounds"
        pebbles = self.board[choice]
        self.board[choice] = 0
        return pebbles

    def drop(self, pebbles, start=0, isPlayer=True):
        i = start
        while i < 6 and pebbles > 0:
            self.board[i] += 1
            pebbles -= 1
            i += 1
        go_again = False
        if pebbles > 0 and isPlayer:
            self.score += 1
            pebbles -= 1
            go_again = pebbles == 0
        return pebbles, go_again
            
        
