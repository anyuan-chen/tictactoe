class Game_engine:
    def __init__(self):
        self.turn = 1
        self.board = [[0,0,0], [0,0,0], [0,0,0]]

    def move(self, x, y, player):
        if self.board[x][y] != 0:
            print("Invalid move. There is already a piece at that location.")
            return False
        self.board[x][y] = player

    def checkWin(self, x, y, player):
        def checkVerticalWin():
            flag = True
            for i in range(3):
                if self.board[i][y] != player:
                    #print(self.board[i][y])
                    flag = False
            if (flag):
                return True
            return False
        def checkHorizontalWin():
            for i in self.board[x]:
                if i != player:
                    return False
            return True
        def checkDiagonalWin():
            flag = True
            for i in [[0,0],[1,1],[2,2]]:
                if (self.board[i[0]][i[1]] != player):
                    flag = False
                    break
            if flag:
                return True
            for i in [[0,2],[1,1],[2,0]]:
                if (self.board[i[0]][i[1]] != player):
                    flag = False
                    break
            if flag:
                return True
            return False
        
        if (checkHorizontalWin() or checkVerticalWin() or checkDiagonalWin()):
            return True
        return False


        
        
        
        
        


game = Game_engine()
print(game.checkWin(0,1,1))
