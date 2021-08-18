from multiplayer import Multiplayer
import sys
from singleplayer import Singleplayer

print("Welcome to Tic Tac Toe!")
print("Enter 1 to play against the AI")
print("Enter 2 to play against another player")

selection = int(sys.stdin.readline())

if selection == 1:
    s_instance = Singleplayer()

if selection == 2:
    m_instance = Multiplayer()
    m_instance.play();
    