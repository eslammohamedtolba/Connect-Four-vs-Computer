
class Player:
    def __init__(self):
        self.Name = input("Enter your name: ")
        while True:
            self.Symbol = input("Enter your symbol R or B: ")
            if self.Symbol in ['R','B']:
                break
    def play(self,board):
        y = int(input("Enter Y-axis of your play: "))
        return y

class ComputerPlayer:
    def __init__(self,otherPlayerSymbol):
        self.Name = "Computer Player"
        self.Symbol = "B" if otherPlayerSymbol=="R" else "R"

    # The state method checks the current state of the game if winning or draw or still the game is running 
    def state(self,board,IsComputer,symbol):
        if board.IsWinner(symbol):
            if IsComputer:
                # winning for computer player
                return 1
            else:
                # losing for computer player
                return -1
            
        elif board.IsDraw():
            # drawing for both players
            return 0
        else:
            # still game continuing 
            return -2
        
    # The ChooseSuit method chooses the best move for the computer player by backtracking and minmax algorithms
    def ChooseSuit(self,board,IsComputer):
        playing=[0,-2 if IsComputer==1 else 2]
        for Y in range(1,board.ColSize+1):
            if board.UpdateBoard(Y,self.Symbol if IsComputer==1 else ('B' if self.Symbol=='R' else 'R')):
                currentstate = self.state(board,IsComputer,self.Symbol if IsComputer==1 else ('B' if self.Symbol=='R' else 'R'))
                # still running 
                if currentstate==-2:
                    againstPlaying = self.ChooseSuit(board,0 if IsComputer==1 else 1)
                    if IsComputer==1:
                        if againstPlaying[1]>playing[1]:
                            playing=[Y,againstPlaying[1]]
                    else:
                        if againstPlaying[1]<playing[1]:
                            playing=[Y,againstPlaying[1]]
                # winning or draw is happen
                else:
                    if IsComputer==1:
                        if currentstate>playing[1]:
                            playing=[Y,currentstate]
                    else:
                        if currentstate<playing[1]:
                            playing=[Y,currentstate]

                X = board.X_axis(Y)
                board.Board[X][Y-1]=' '
        board.PrintBoard()
        return playing

    def play(self,board):
        Y= self.ChooseSuit(board,1)[0]
        return Y