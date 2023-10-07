from Board import *
from Player import *

class Game:
    def __init__(self):
        self.Players = [Player()]
        while True:
            typeSplayer = int(input("Do you want to play with another player(0) or with computer(1): "))
            if typeSplayer == 0:
                self.Players.append(Player())
                break
            elif typeSplayer == 1:
                self.Players.append(ComputerPlayer(self.Players[0].Symbol))
                break
        self.board = Board()
        self.GameRunning=True

    def StartGame(self):
        self.board.PrintBoard()
        while self.GameRunning:
            for player in self.Players:
                while True:
                    if type(player)==Player:
                        print(f"please {player.Name} with symbol {player.Symbol} enter One index between 1 and {self.board.ColSize} in empty places")
                    playing = player.play(self.board)
                    if type(player)==ComputerPlayer:
                        print(f"the computer player played on ({playing})")
                    if self.board.UpdateBoard(playing,player.Symbol):
                        break

                self.board.PrintBoard()
                if self.board.IsWinner(player.Symbol):
                    print(f"the player {player.Name} won!")
                    self.GameRunning=False
                    break
                elif self.board.IsDraw():
                    print("it's draw")
                    self.GameRunning=False
                    break
