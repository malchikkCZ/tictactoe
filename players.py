import random


class Player:

    def __init__(self, stone):
        self.stone = stone

    def get_move(self, game):
        try:
            move = int(input(self.stone + "'s turn >>> "))
            if move not in game.possible_moves():
                raise ValueError
        except ValueError:
            print("Invalid move, try again.\n")
            move = self.get_move(game)
        finally:
            return move

    def put_stone(self, game):
        move = self.get_move(game)
        r, c = move // 3, move % 3
        game.board[r][c] = self.stone


class EasyComputer(Player):

    def __init__(self, stone):
        super().__init__(stone)

    def get_move(self, game):
        move = random.choice(game.possible_moves())
        print(self.stone + "'s turn >>>", move)
        return move


class HardComputer(Player):

    def __init__(self, stone):
        super().__init__(stone)

    def get_move(self, game):
        if len(game.possible_moves()) == 9:
            move = random.choice(game.possible_moves())
        else:
            move = self.find_best_move(game)
        print(self.stone + "'s turn >>>", move)
        return move

    def find_best_move(self, game):
        # best_move = -1
        best_score = -999
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
