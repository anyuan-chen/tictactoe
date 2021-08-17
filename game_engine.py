class Game_engine:
    def __init__(self):
        self.turn = "p1"
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
    def move(self, x, y):
        if self.board[x][y] == 1:
            print("Invalid move. There is already a piece at that location.")
            return False
        


game = Game_engine()
