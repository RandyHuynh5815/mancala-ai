from Board import Board

if __name__ == "__main__":
    board = Board()
    i = 0
    while i < 10:
        board.print_board()
        current_player = 'P1' if board.p1_turn else 'P2'
        option = int(input(f"{current_player}. It's your turn: "))
        board.turn(option)
        i += 1