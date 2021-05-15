class Board:

    def __init__(self):
        self.board = [["_" for c in range(3)] for r in range(3)]
        self.hints = [[(c + r*3) for c in range(3)] for r in range(3)]
        self.print_board()

    def print_board(self):
        for r in range(3):
            print("[", end=" ")
            for c in range(3):
                print(self.board[r][c], end = " ")
            print("]   ", self.hints[r])
        print()

    def possible_moves(self):
        moves = []
        for move in range(9):
            r, c = move // 3, move % 3
            if self.board[r][c] == "_":
                moves.append(move)
        return moves

    def evaluate(self, player):
        # check rows
        for row in self.board:
            if row.count(player) == 3:
                return True
        # check cols
        reversed = [[self.board[r][c] for r in range(3)] for c in range(3)]
        for row in reversed:
            if row.count(player) == 3:
                return True
        # check diags
        diag1 = [self.board[i][i] for i in range(3)]
        diag2 = [self.board[i][2-i] for i in range(3)]
        if diag1.count(player) == 3 or diag2.count(player) == 3:
            return True
        return False


class Game:

    def __init__(self, board, players):
        self.is_game_on = True
        self.board = board
        self.players = players

    def game_on(self):
        while self.is_game_on:      
            for player in self.players:
                player.put_stone(self.board)
                self.board.print_board()
                if self.board.evaluate(player.stone):
                    print(player.stone, "is a winner!")
                    self.is_game_on = False 
                    break
                elif len(self.board.possible_moves()) == 0:
                    print("It's a draw!")
                    self.is_game_on = False
                    break
