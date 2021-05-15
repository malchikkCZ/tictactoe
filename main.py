import random


class Player():
    def __init__(self, stone):
        self.stone = stone

    def get_move(self, game):
        try:
            move = int(input(self.stone + "'s turn >>> "))
            if move < 0 or move > 8:
                raise ValueError
            if move not in game.possible_moves():
                print("Cell already taken.")
                self.get_move(game)
        except ValueError:
            print("Invalid entry, try again.\n")
            self.get_move(game)
        else:
            return (move // 3, move % 3)

    def put_stone(self, game):
        r, c = self.get_move(game)
        game.board[r][c] = self.stone




class EasyComputer(Player):
    def __init__(self, stone):
        super().__init__(stone)

    def get_move(self, game):
        move = random.choice(game.possible_moves())
        return (move // 3, move % 3)


class HardComputer(Player):
    def __init__(self, stone):
        super().__init__(stone)

    def get_move(self, game):
        if len(game.possible_moves()) == 9:
            move = random.choice(game.possible_moves())
        else:
            move = self.find_best_move(game)
        return move // 3, move % 3

    def find_best_move(self, game):
        best_move = -1
        best_score = -999
        other_stone = "O" if self.stone == "X" else "X"
        
        for move in game.possible_moves():
            r, c = move // 3, move % 3
            game.board[r][c] = self.stone
            score = self.minimax(game, 0, False)
            game.board[r][c] = "_"

            if score > best_score:
                best_move = move
                best_score = score
        
        return best_move

    def minimax(self, game, depth, is_max):
        other_stone = "O" if self.stone == "X" else "X"
        empty_squares = len(game.possible_moves())

        if game.evaluate(self.stone):
                return (10 - depth)
        elif game.evaluate(other_stone):
                return (-10 + depth)
        elif empty_squares == 0:
            return 0
        
        if is_max:
            best_score = -999

            for move in game.possible_moves():
                r, c = move // 3, move % 3
                game.board[r][c] = self.stone
                best_score = max(best_score, self.minimax(game, depth+1, not is_max))
                game.board[r][c] = "_"
                
            return best_score

        else:
            best_score = 999

            for move in game.possible_moves():
                r, c = move // 3, move % 3
                game.board[r][c] = other_stone
                best_score = min(best_score, self.minimax(game, depth+1, not is_max))
                game.board[r][c] = "_"

            return best_score 


class Game:
    def __init__(self):
        self.board = [["_" for c in range(3)] for r in range(3)]
        self.hints = [[(c + r*3) for c in range(3)] for r in range(3)]
        # self.print_board()

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


    
x_wins = 0
o_wins = 0
draws = 0

for i in range(100):

    players = [EasyComputer("X"), HardComputer("O")]

    game = Game()

    is_game_on = True
    while is_game_on:
        for player in players:
            player.put_stone(game)
            # game.print_board()
            if game.evaluate(player.stone):
                # print(player.stone, "is a winner!")
                if player.stone == "X":
                    x_wins += 1
                else:
                    o_wins += 1 
                is_game_on = False 
                break
            elif len(game.possible_moves()) == 0:
                # print("It's a draw!")
                draws += 1
                is_game_on = False
                break


print("X wins:", x_wins, "O wins:", o_wins, "Draws:", draws)