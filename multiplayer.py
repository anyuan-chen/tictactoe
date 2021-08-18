from game_engine import Game_engine

class Multiplayer(Game_engine):
    def __init__(self):
        super().__init__()
        self.turnNumber = 0;

    def play(self):
        while True:
            self.turnNumber+=1
            if (self.turnNumber%2 == 1):
                print("It is player 1's turn. Please enter the x and y coordinate of where you would like to player your tile with a space between.")
                user_x, user_y = map(int, input().split())
                if (self.move(user_x, user_y, 1)):
                    didWin = self.checkWin(user_x,user_y,1)
                    self.getBoard()
                    if (didWin):
                        print("Player 1 has won. The game will now exit.")
                        break
            if (self.turnNumber%2 == 0):
                print("It is player 2's turn. Please enter the x and y coordinate of where you would like to player your tile with a space between.")
                user_x, user_y = map(int, input().split())
                if (self.move(user_x, user_y, 2)):
                    didWin = self.checkWin(user_x,user_y,2)
                    self.getBoard()
                    if (didWin):
                        print("Player 2 has won. The game will now exit.")
                        break
                else:
                    print("Tile already taken. Please enter another tile")
            print(self.getBoard())
